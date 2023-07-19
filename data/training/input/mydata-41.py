###############
#
# IITIAL DATA for training reaction 41
# Ph-NH-CH3 + N(=O)OH (+ HX) -> Ph-CH(CH3)-N=O + H2O
#

species = [ 'Ph','O','O','N','N','CH3','H','H' ]   # Species of Atom
fixvec  = [ [ 1, 1 ], [ 2, 2 ] ]
inivec  = [ [ 0, 0 ], [ 0, 3 ], [ 1, 1 ], [ 1, 4 ], [ 1, 4 ], \
            [ 2, 2 ], [ 2, 4 ], [ 2, 6 ], [ 3, 3 ], [ 3, 5 ], [ 3, 7 ], [ 4, 4 ] ]
golvec  = [ [ 0, 0 ], [ 0, 3 ], [ 1, 1 ], [ 1, 4 ], [ 1, 4 ], \
            [ 2, 2 ], [ 2, 6 ], [ 2, 7 ], [ 3, 3 ], [ 3, 4 ], [ 3, 5 ], [ 4, 4 ] ]