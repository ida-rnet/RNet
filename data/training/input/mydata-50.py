###############
#
# IITIAL DATA for training reaction 50
# CH3-C(=O)-X + CH3-CH2-OH -> CH3-C(=O)-O-CH2-CH3 + HX
# 

species = [ 'X','O','O','CH3','CH3','CH2','C','H' ]   # Species of Atom
fixvec  = [ [ 0, 0 ], [ 0, 0 ], [ 0, 0 ], [ 1, 1 ], [ 2, 2 ] ]
inivec  = [ [ 0, 6 ], [ 1, 1 ], [ 1, 5 ], [ 1, 7 ], [ 2, 2 ], \
            [ 2, 6 ], [ 2, 6 ], [ 3, 5 ], [ 4, 6 ] ]
golvec  = [ [ 0, 7 ], [ 1, 1 ], [ 1, 5 ], [ 1, 6 ], [ 2, 2 ], \
            [ 2, 6 ], [ 2, 6 ], [ 3, 5 ], [ 4, 6 ] ]
