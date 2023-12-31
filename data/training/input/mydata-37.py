###############
#
# IITIAL DATA for training reaction 37
# CH3-CH2-CH2-C(=O)-OH + (CH3)2-NH -> CH3-CH2-CH2-C(=O)-N(CH3)2 + H2O
#

species = [ 'O','O','N','CH3','CH3','CH3','CH2','CH2','C','H','H' ]   # Species of Atom
fixvec  = [ [ 0, 0 ], [ 1, 1 ] ]
inivec  = [ [ 0, 0 ], [ 0, 8 ], [ 0, 8 ], [ 1, 1 ], [ 1, 8 ], [ 1, 9 ], \
            [ 2, 2 ], [ 2, 3 ], [ 2, 4 ], [ 2, 10 ], [ 5, 6 ], [ 6, 7 ], [ 7, 8 ] ]
golvec  = [ [ 0, 0 ], [ 0, 8 ], [ 0, 8 ], [ 1, 1 ], [ 1, 9 ], [ 1, 10 ], \
            [ 2, 2 ], [ 2, 3 ], [ 2, 4 ], [ 2, 8 ], [ 5, 6 ], [ 6, 7 ], [ 7, 8 ] ]
