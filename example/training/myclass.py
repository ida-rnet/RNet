##################
#
# Setting Parameters, Functions and Class
#
import mydata as md

##################
#
# Parameters
#
# Parameters dictionary is 
# { "particle": ( val_electron, max_charge, min_charge, max_valence, min_valence ) }
#
v_para = { 'Ph' : (  3,  1,  0,  4,  4 ),
	   'X'  : (  7,  0, -1,  8,  8 ),
	   'M'  : (  1,  1,  0,  2,  0 ),
	   'MgX': (  1,  1,  0,  2,  0 ),
	   'O'  : (  6,  1, -1,  8,  8 ),
	   'N'  : (  5,  1, -1,  8,  6 ),
	   'CH3': (  1,  1,  0,  2,  0 ),
	   'CH2': (  2,  1,  0,  4,  2 ),
	   'C'  : (  4,  1, -1,  8,  6 ),
	   'H'  : (  1,  1, -1,  2,  0 ) }

species = md.species
fixvec  = md.fixvec 
inivec  = md.inivec 
golvec  = md.golvec 
natom   = len( species )
num_H   = species.index( 'H' )

val_ele= []
max_chg= []
min_chg= []
max_val= []
min_val= []

for atom in species:
	val_ele.append( v_para[ atom ][0] )
	max_chg.append( v_para[ atom ][1] )
	min_chg.append( v_para[ atom ][2] )
	max_val.append( v_para[ atom ][3] )
	min_val.append( v_para[ atom ][4] )

##################
#
# Functions
#
def addperm(x,l):
	return [ l[0:i] + [x] + l[i:]  for i in range(len(l)+1) ]

def perm(l):
	if len(l) == 0:
		return [[]]
	return [x for y in perm(l[1:]) for x in addperm(l[0],y) ]

def perm_map(l):
	x = [ a for a in range( sum(l) ) ]
	y = []
	for n in range( len(l) ):
		n1 = sum( l[:n] )
		n2 = sum( l[:n+1] )
		if n == 0:
			y = perm( x[n1:n2] )
		else:
			z = list( y )
			y.clear()
			y = [ a + b for a in z for b in perm( x[n1:n2] ) ]
	return y[1:]

def set_dict( x, m ):
	m.setdefault( x, 0 )
	m[x] += 1

###############
#
# CLASS : Bond-Electron Vector
#
class BEV:
	def __init__( self, vec ):
		self.bevec = sorted( vec )
		self.edge = []
#
	def set_id( self, id ):
		self.id = id
#
	def set_iso( self, isoset ):
		self.iso = isoset
#
	def set_point( self, pt ):
		self.pt = pt
#
	def set_edge( self, id ):
		if id not in self.edge:
			self.edge.append( id )
			self.edge.sort()
#
	def charge( self ):
		fullvec = self.bevec + fixvec
		tmpvec = [0] * natom
		for be in fullvec:
			tmpvec[ be[0] ] += 1
			tmpvec[ be[1] ] += 1
		return [ x - y for x, y in zip( val_ele, tmpvec ) ]
#
	def charge_check( self ):
		tmp = self.charge()
		if tmp.count( 1 ) > 2:
			return False
		return all( x <= y <= z for x, y, z in zip( min_chg, tmp, max_chg ) )
#
	def valence( self ):
		fullvec = self.bevec + fixvec
		tmpvec = [0] * natom
		for be in fullvec:
			tmpvec[ be[0] ] += 2
			if be[0] != be[1]:
				tmpvec[ be[1] ] += 2
		return tmpvec
#
	def valence_check( self ):
		tmp = self.valence()
		return all( x <= y <= z for x, y, z in zip( min_val, tmp, max_val ) )
#
	def bond_order( self ):
		fullvec = self.bevec + fixvec
		fulltup = [ tuple( x ) for x in fullvec ]
		tempset = set( fulltup )
		tdict = dict()
		for bond in tempset:
			if bond[0] != bond[1]:
				tdict[ bond ] = fulltup.count( bond )
		return tdict
#
	def bonder_check( self ):
		tdict = self.bond_order()
		for x in tdict.values():
			if x > 3:
				return False
		return True
#
	def goal_check( self ):
		ion = self.charge()
		if not any( ion ):
			val = self.valence()
			valc = [ y - x for x, y in zip( val, max_val ) ]
			if not any( valc ):
				return True
		return False

#
	def reaction( self ):
		reacvec = []
		for i, be in enumerate( self.bevec ):
			tmpvec = list( self.bevec )
			del tmpvec[ i ]
			if be[0] == be[1]:
				seq = [ k for k in range( natom ) if k != be[0] ]
				for j in seq:
					tmp = list( tmpvec )
					tmp.append( sorted( [be[0], j] ) )
					tmp.sort()
					if tmp not in reacvec:
						reacvec.append( tmp )
			else:
				for j in range(2):
					tmp = list( tmpvec )
					tmp.append( [be[j], be[j]] )
					tmp.sort()
					if tmp not in reacvec:
						reacvec.append( tmp )
		return reacvec
#
	def isomorph( self, pmap ):
		ini = tuple( [ tuple( be ) for be in self.bevec ] )
		iso = [ ini ]
		for p in pmap:
			tmp = []
			for be in self.bevec:
				be2 = sorted( [ p[ be[0] ], p[ be[1] ] ] )
				tmp.append( tuple( be2 ) )
			tmp2 = tuple( sorted( tmp ) )
			if tmp2 not in iso:
				iso.append( tmp2 )
		return sorted( iso )
#
	def get_prop( self ):
		prop_dict = {}
		bond = self.bond_order()
		chrg = self.charge()
		vale = self.valence()
		b22 = sum( [ list(k) for k, v in bond.items() if v==2 ], [] )
		qb22 = [ x for x in set( b22 ) if b22.count(x) > 1]
		for nn in qb22:
			set_dict( species[ nn ][0] + '22', prop_dict )
		for be in bond:
			name = species[ be[0] ][0] + species[ be[1] ][0]
			if name == 'OC':
				if chrg[ be[0] ] == -1 and chrg[ be[1] ] == 1:
					set_dict( 'OmCp', prop_dict )
				for x in range( num_H ):
					nm2 = species[ x ][0]
					be2 = tuple( sorted( [ be[1], x ] ) )
					ch2 = chrg[ x ]
					if nm2 == 'C' and be2 in bond and ch2 == -1:
						set_dict( 'CmCO', prop_dict )
			if bond[ be ] > 1:
				name += str( bond[ be ] )
				if name == 'NC3' and chrg[ be[1] ] == -1:
					set_dict( 'NC3m', prop_dict )
			set_dict( name, prop_dict )
		for i, ch in enumerate( chrg ):
			if ch == 0: continue
			if ch == 1:
				if species[ i ][0] == 'C':
					be = [ tuple( sorted( [ i , x ] ) ) for x in range( num_H ) ]
					num_cr = 0
					for b in be:
						if b in bond:
							num_cr +=1
					name = 'CpR' + str( num_cr )
					set_dict( name, prop_dict )
				else:
					name = species[ i ][0] + 'p'
					set_dict( name, prop_dict )
			else:
				name = species[ i ][0] + 'm'
				set_dict( name, prop_dict )
		for i, vl in enumerate( vale ):
			if vl == min_val[ i ]:
				if species[ i ][0] == 'C':
					set_dict( 'Cd', prop_dict )
				elif species[ i ][0] == 'N':
					set_dict( 'Nd', prop_dict )
		return prop_dict
