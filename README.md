
# RNet -Generating and Analyzing of Chemical Reaction Network-

The chemical formula of the reactant are considered as a graph, and chemical reaction networks are constructed by bonding and breaking chemical bonds. The generated network is analyzed to determine the reaction pathway leading to the correct product. By learning the structures of reaction intermediates, the model can predict the product and the reaction pathway for many chemical reactions.

## Feature

 These codes consist of the generator and analyzer for the chemical reaction network. `Generator.py` construct the chemical reaction network from reactant formula as input (`mydata.py`). The generator output `prop.pkl` and `path.pkl` from the generated networks. If `point.pkl` is in parent directory, the generator also predict the product and reaction pathway. The `point.pkl` is a set of weights for the fragment structures included in the intermediates. `Analyzer.py` learn the reaction network through the `prop.pkl` and `path.pkl` and create the `point.pkl`.

## Requirement

 * Python 3.6
 * PyTorch
 * NetworkX
 * Pickle

## Usage

### Generation
     For generation of reaction network, three files put in same directory as follows;
     generator.py ( main program)
     myclass.py   ( faunction and class )
     mydata.py    ( input data ).

     the generator.py construct the chemical reaction network, and prop.pkl, path.pkl.

     job.sh is batch script for multiple generation of the networks.

### Analyzation (Learning)
     For analyzation of the network, the analyzer.py in the parent directory learn all prop.pkl and path.pkl in each directory. 
     It learns until the loss reaches a specified value and generates a point.pkl file.

## License
All rights reserved 2023 Created by Tomonori Ida.

Please contact me, ida@se.kanazawa-u.ac.jp


