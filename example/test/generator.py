#################
#
# PROGRAM : Genrating Organic Reaction Network
#
import myclass  as mc
import numpy    as np
import networkx as nx
import pickle
import os
#
# Print initial setting
#
#max_graph = 800       # For training data
max_graph = 3000    # For test data

print( 'Nomber of atoms = ', mc.natom )
print( 'Atoms = ', mc.species )
print( 'Valence electrons = ', mc.val_ele)
print( 'Fixed electrons = ', mc.fixvec)

groups = []
gl = sorted( set( mc.species ), key=mc.species.index )
for nn in gl:
	groups.append( mc.species.count( nn ) )
pmap = mc.perm_map( groups )

mother = mc.BEV( mc.inivec )
if ( mother.valence_check() and
     mother.charge_check()  and
     mother.bonder_check() ):
	print( "Initial graph is stable." )
else:
	print( "Initial graph is NOT stable." )

child = mc.BEV( mc.golvec )
if ( child.valence_check() and
     child.charge_check()  and
     child.bonder_check() and
     child.goal_check() ):
	print( "Goal graph can be used for prediction." )
else:
	print( "Goal graph canNOT be used for prediction!" )
gv = sorted( mc.golvec )
goliso = tuple( [ tuple( be ) for be in gv ] )

#################
#
# Main routine
#
seed = []
next = []
node = []
ini_iso = mother.isomorph( pmap )
ini_bevec = mc.BEV( [ list( be ) for be in ini_iso[0] ] )
ini_bevec.set_id( 0 )
ini_bevec.set_iso( set( ini_iso ) )
seed.append( ini_bevec )

#################
#
# Construction of the reaction network
#
num_id = 1
while len( seed ) != 0 and num_id < max_graph:
	for se in seed:
		revec = se.reaction()
		for re in revec:
			tmp = mc.BEV( re )
			if not tmp.valence_check(): continue
			if not tmp.charge_check():  continue
			if not tmp.bonder_check():  continue
			tiso = tuple( [ tuple( be ) for be in re ] )
			go_next = True
			for nd in next:
				if tiso in nd.iso:
					nd.set_edge( se.id )
					se.set_edge( nd.id )
					go_next = False
			for nd in node:
				if tiso in nd.iso:
					nd.set_edge( se.id )
					se.set_edge( nd.id )
					go_next = False
			if go_next:
				isovec = tmp.isomorph( pmap )
				tmp2 = mc.BEV( [list( be ) for be in isovec[0]] )
				tmp2.set_id( num_id )
				num_id += 1
				tmp2.set_iso( set( isovec ) )
				tmp2.set_edge( se.id )
				se.set_edge( tmp2.id )
				next.append( tmp2 )
	node.extend( seed )
	seed.clear()
	seed.extend( next )
	next.clear()

if len( seed ) != 0:
	node.extend( seed )
	seed.clear()

print( '\n Generated No. and Nodes:')
for nd in node:
	print( f'{nd.id:5d}, ', nd.bevec)

edges = []
for nd in node:
	for x in nd.edge:
		if nd.id < x:
			edges.append( tuple( [ nd.id, x ] ) )
print( 'Total nodes = ', len( node  ) )
print( 'Total edges = ', len( edges ) )

#################
#
# Computing Properties and Paths
#
G = nx.Graph()
G.add_edges_from( edges )
prop_list = []
path_list = []
num_goal = 0
num_id = 0
num_path = 0
for nd in node:
	prop_list.append( nd.get_prop() )
	if nd.id == 0:
		continue
	elif nd.goal_check():
		if goliso in nd.iso:
			print( 'True Goal graph No.', nd.id )
			num_goal = nd.id
		else:
			print( 'Goal candidates No.', nd.id )
		plist = nx.all_shortest_paths(G, source=0, target=nd.id )
		for mm in plist:
			path_list.append( tuple( mm ) )
			num_path += 1
		num_id += 1

print( 'Total Goals = ', num_id, ' and Paths =', num_path, '\n' )
plist = nx.all_shortest_paths(G, source=0, target=num_goal )
num_g = 0
for m in plist:
	num_g += 1
print( 'True paths:', num_g, '/', num_path, '\n' )
prop_list.append( num_goal )

#################
#
# Save DATA
#
with open('prop.pkl', 'wb') as f1:
	pickle.dump( prop_list, f1 )
with open('path.pkl', 'wb') as f2:
	pickle.dump( path_list, f2 )

#################
#
# Prediction of Reaction Path
#
if 'point.pkl' in os.listdir( '../' ):
	with open( '../point.pkl', 'rb' ) as f:
		points = pickle.load( f )

	for nd in node:
		prop = nd.get_prop()
		val = 0.0
		for k, v in prop.items():
			val += points.get( k, 0 ) * v
		nd.set_point( val )

	points_list = []
	for paths in path_list:
		fac = 1./ ( len( paths ) - 1 )
		pval = sum( [ node[ nn ].pt for nn in paths[1:] ] )
		points_list.append( fac * pval )

	pp = sorted( zip( points_list, path_list ), reverse=True )
	num_predict = 5 if num_path > 5 else num_path
	for nn in range( num_predict ):
		m = pp[ nn ][1][-1]
		result = 'Bad result'
		if m == num_goal:
			if nn == 0:
				result = 'Very good result!!'
			else:
				result = 'Good result'
		print( 'Top', nn + 1,':', result )
		for ppp in pp[ nn ][1]:
			print( ppp, ' : ', node[ ppp ].pt )
