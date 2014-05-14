MatrixFromBasis
===============

Generates the entire matrix from a basis and gives Hamming Distance between all the elements

This code takes input from a file called Input.txt which is basically a generator matrix for a Z2 code (an example generator matrix is already written in file).
Here each codeword of the generator matrix is kept in a new line. This file can be changed as required to calculate for any generator matrix.
The program runs all possible combinations of codewords in generator matrix and returns the codewords of the linear code for the generator matrix in binary as well as decimal form and stores in files BinaryLinearCode.txt and Decimal.txt.
After this, it calculates the Hamming Distance between all the codewords as well as the minimum Hamimng Distance. These are stored in the file HammingDistance.txt.
This program can help to check if the given generator can give a valid code of given Hamming Distance as well as to get the all the codewords for a given generator.
