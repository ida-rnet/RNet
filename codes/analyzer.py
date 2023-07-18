#################
#
# PROGRAM : Chemical Reaction Analyzer
#
import numpy as np
import torch
import pickle
import os
#
# Read initial setting
#
num_train =  100
max_cycle = 5000
threshold =  0.03

elements = [ 'Pp', 'Xm', 'Mp', 'Om', 'OmCp', 'Op', 'Nm', 'NC3m', 'Np', 'Nd', \
             'Cm', 'CmCO', 'CpR3', 'CpR2', 'CpR1', 'CpR0', 'Cd', 'Hm', 'Hp', \
	     'PM', 'PN2', 'PN', 'PC2', 'PC', 'PH', 'XM', 'XN', 'XC', 'XH', \
	     'MO', 'MN', 'MC', 'MH', 'ON3', 'ON2', 'ON', 'OC3', 'OC2', 'OC', 'OH', \
	     'NC3', 'NC2', 'NC', 'NH', 'N22', 'CC3', 'CC2', 'C22', 'HH' ]
num_elmt = len( elements )
dirs   = []
nodirs = []
for dn in os.listdir():
	if os.path.isdir( dn ):
		dirs.append( dn )
for dn in dirs:
	pr = os.path.join( dn, 'prop.pkl' )
	if os.path.exists( pr ):
		with open( pr, 'rb' ) as fr:
			prop = pickle.load( fr )
		if prop[ -1 ] == 0:
			nodirs.append( dn )
	else:
		nodirs.append( dn )
for nd in nodirs:
	dirs.remove( nd )
num_reac = len( dirs )
#####
#
# Read DATA for Reactions
#
propAs = []   # Correct path
propBs = []   # Incorrect path
for dn in dirs:
	pf1 = os.path.join( dn, 'prop.pkl' )
	pf2 = os.path.join( dn, 'path.pkl' )
	with open( pf1, 'rb') as f1:
		prop_list = pickle.load( f1 )
	goal_node = prop_list.pop()
	with open(  pf2, 'rb') as f2:
		path_list = pickle.load( f2 )
	num_prop = len( prop_list )
	num_path = len( path_list )
	prop1 = np.empty( ( num_prop, num_elmt ) )
	prop2 = np.zeros( ( num_path, num_prop ) )
	prop  = np.empty( ( num_path, num_elmt ) )
	for i, pdict in enumerate( prop_list ):
		row = [ pdict.get( elt, 0. ) for elt in elements ]
		prop1[ i ] = row
	true_path  = []
	for i, path in enumerate( path_list ):
		fac = 1. / ( len( path ) - 1 )
		for j in path[1:]:
			prop2[ i ][ j ] = fac
		if path[-1] == goal_node:
			true_path.append( i )
	prop = prop2.dot( prop1 )
	propA = np.empty( ( len( true_path ), num_elmt ) )
	for i, j in enumerate( true_path ):
		propA[ i ] = prop[ j ]
	propB = np.delete( prop, true_path, 0 )
	propAs.append( propA )
	propBs.append( propB )

#####
#
# Anlyzing Chemical Reaction Network
#
net = torch.nn.Linear( num_elmt, 1, False )
loss_fn = torch.nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam( net.parameters(), lr = 0.01 )
y = torch.ones( num_train * num_reac )
num_iter = 0
inconv = True

for epoc in range( max_cycle ):
	optimizer.zero_grad()
	x = torch.empty( num_train * num_reac, num_elmt )
	num_id = 0
	for n in range( num_reac ):
		ra = propAs[ n ].shape[0]
		na = [ i % ra for i in range( num_train ) ]
		rb = propBs[ n ].shape[0]
		nb = np.random.randint( 0, rb, num_train )
		for i in range( num_train ):
			mm = np.array( propAs[ n ][ na[i] ] - propBs[ n ][ nb[i] ] )
			x[ num_id ] = torch.from_numpy( mm.astype(np.float32) ).clone()
			num_id += 1
	y_pred = net(x)
	loss = loss_fn( y_pred.view_as(y), y )
	loss.backward()
	optimizer.step()
	if loss.item() < threshold:
		print( 'Value of loss function:', loss.item(), 'after', num_iter, 'cycle\n' )
		inconv = False
		break
	num_iter += 1

if inconv:
	print(' Not convergence! in MaxCycle',num_iter, '\n' )
x_final = net.weight.detach().numpy().copy()
x_final = x_final.flatten().tolist()
point_dict = dict( zip( elements, x_final ) )

print( 'Evaluation points' )
for k, v in point_dict.items():
	print( f'{k:5s} : {v:10.5f}' )
with open('point.pkl', 'wb') as f:
	pickle.dump( point_dict, f )
