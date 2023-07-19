###############
#
# IITIAL DATA for training reaction 40
# Ph(MgX) + CH3-C(=O)-Ph + HX -> CH3-C(OH)(Ph)2 + X(MgX)
# Grignard regent

species = ['Ph','Ph','X','MgX','O','CH3','C','H' ]   # Species of Atom
fixvec  = [ [ 2, 2 ], [ 2, 2 ], [ 2, 2 ], [ 4, 4 ] ]
inivec  = [ [ 0, 0 ], [ 0, 3 ], [ 1, 1 ], [ 1, 6 ], [ 2, 7 ], \
            [ 4, 4 ], [ 4, 6 ], [ 4, 6 ], [ 5, 6 ] ]
golvec  = [ [ 0, 0 ], [ 0, 6 ], [ 1, 1 ], [ 1, 6 ], [ 2, 3 ], \
            [ 4, 4 ], [ 4, 6 ], [ 4, 7 ], [ 5, 6 ] ]
