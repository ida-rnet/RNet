###############
#
# IITIAL DATA for training reaction 45
# CH3-CH2-(MgX) + CH3-C(=O)-O-CH3 -> CH3-CH2-C(=O)-CH3 + (MgX)-O-CH3
# Grignard regent

species = [ 'MgX','O','O','CH3','CH3','CH3','C','C','H','H' ]   # Species of Atom
fixvec  = [ [ 1, 1 ], [ 2, 2 ] ]
inivec  = [ [ 0, 6 ], [ 1, 1 ], [ 1, 7 ], [ 1, 7 ], [ 2, 2 ], [ 2, 3 ], [ 2, 7 ], \
            [ 4, 6 ], [ 5, 7 ], [ 6, 8 ], [ 6, 9 ] ]
golvec  = [ [ 0, 1 ], [ 1, 1 ], [ 1, 3 ], [ 2, 2 ], [ 2, 6 ], [ 2, 6 ], \
            [ 4, 6 ], [ 5, 7 ], [ 6, 7 ], [ 7, 8 ], [ 7, 9 ] ]
