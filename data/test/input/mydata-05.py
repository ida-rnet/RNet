###############
#
# IITIAL DATA for Challenge reaction 05
# Ph-C(=O)H + CH3-C(=O)H -> Ph-CH(OH)-CH2-C(=O)-H
# cross aldol ( no condensation )

species = [ 'Ph','O','O','C','C','C','H','H','H','H','H' ]   # Species of Atom
fixvec  = [ [ 1, 1 ], [ 2, 2 ] ]
inivec  = [ [ 0, 0 ], [ 0, 3 ], [ 1, 1 ], [ 1, 3 ], [ 1, 3 ], [ 2, 2 ], [ 2, 4 ], \
            [ 2, 4 ], [ 3, 6 ], [ 4, 5 ], [ 4, 7 ], [ 5, 8 ], [ 5, 9 ], [ 5, 10 ] ]
golvec  = [ [ 0, 0 ], [ 0, 3 ], [ 1, 1 ], [ 1, 3 ], [ 1, 6 ], [ 2, 2 ], [ 2, 4 ], \
            [ 2, 4 ], [ 3, 5 ], [ 3, 7 ], [ 4, 5 ], [ 4, 8 ], [ 5, 9 ], [ 5, 10 ] ]
