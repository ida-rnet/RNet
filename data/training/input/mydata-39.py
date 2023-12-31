###############
#
# IITIAL DATA for training reaction 39
# CH#CH + M+ + NH2- + Ph-CH2-X -> CH#C-CH2-Ph + NH3 + MX
#

species = [ 'Ph','X','M','N','CH2','C','C','H','H','H','H' ]   # Species of Atom
fixvec  = [ [ 1, 1 ], [ 1, 1 ], [ 1, 1 ] ]
inivec  = [ [ 0, 0 ], [ 0, 4 ], [ 1, 4 ], [ 3, 3 ], [ 3, 3 ], [ 3, 7 ], [ 3, 8 ], \
            [ 5, 6 ], [ 5, 6 ], [ 5, 6 ], [ 5, 9 ], [ 6, 10 ] ]
golvec  = [ [ 0, 0 ], [ 0, 4 ], [ 1, 2 ], [ 3, 3 ], [ 3, 7 ], [ 3, 8 ], [ 3, 9 ], \
            [ 4, 5 ], [ 5, 6 ], [ 5, 6 ], [ 5, 6 ], [ 6, 10 ] ]
