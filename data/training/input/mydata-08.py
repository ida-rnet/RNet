###############
#
# IITIAL DATA for training reaction 08 
# CH3-CH=C=O + CH3-CH2-OH -> CH3-CH2-C(=O)-O-CH2-CH3
#

species = [ 'O','O','CH3','CH3','CH2','C','C','H','H' ]   # Species of Atom
fixvec  = [ [ 0, 0 ], [ 1, 1 ] ]
inivec  = [ [ 0, 0 ], [ 0, 4 ], [ 0, 7 ], [ 1, 1 ], [ 1, 5 ], [ 1, 5 ], \
            [ 2, 4 ], [ 3, 6 ], [ 5, 6 ], [ 5, 6 ], [ 6, 8 ] ]
golvec  = [ [ 0, 0 ], [ 0, 4 ], [ 0, 5 ], [ 1, 1 ], [ 1, 5 ], [ 1, 5 ], \
            [ 2, 4 ], [ 3, 6 ], [ 5, 6 ], [ 6, 7 ], [ 6, 8 ] ]
