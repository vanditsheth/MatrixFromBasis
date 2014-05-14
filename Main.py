##Name: Vandit Sheth

##This code takes input from a file called Input.txt which is basically a generator matrix for a Z2 code (an example generator matrix is already written in file).
##Here each codeword of the generator matrix is kept in a new line. This file can be changed as required to calculate for any generator matrix.
##The program runs all possible combinations of codewords in generator matrix and returns the codewords of the linear code for the generator matrix in binary as well
##as decimal form and stores in files BinaryLinearCode.txt and Decimal.txt.
##After this, it calculates the Hamming Distance between all the codewords as well as the minimum Hamimng Distance. These are stored in the file HammingDistance.txt.
##This program can help to check if the given generator can give a valid code of given Hamming Distance as well as to get the all the codewords for a given generator.
##

values = open("Input.txt","r").read().split('\n')
f = open("Decimal.txt","w")
g = open("BinaryLinearCode.txt","w")

for i in range(len(values)):
    if values[i] == "":
        values = values[:i] + values[i+1]

b = 2**len(values)-1

while b >= 0:
    ans = 0
    bb = b
    i = 0
    while i < len(values):
        ans = ans^(bb%2*int(values[i],2))
        i += 1
        bb/=2
        
    if(ans>=2**len(values[0])):
        ans=ans-2**len(values[0])
        
    f.write(str(int(ans)))
    g.write(str(bin(ans))[2:len(bin(ans))])
    f.write("\n")
    g.write("\n")
    b -= 1

f.close()
g.close()

###Hamming Distance calculation starts here
f = open("Decimal.txt","r")
g = open("BinaryLinearCode.txt","r")
h = open("HammingDistance.txt","w")
x = f.read().split("\n")
z = g.read().split("\n")
arr=[]

for i in range(len(x)):
    j = i
    while j < len(x):
        j+=1
        try:
            arr.append(bin(int(x[i])^int(x[j])).count("1"))
            h.write("Hamming Distance Between " + z[i] + " and " + z[j] + " is " + str(bin(int(x[i])^int(x[j])).count("1")) + "\n")
        except:
            pass

h.write('\nMinimum Hamming Distance is: ' + str(min(arr)))
g.close()
f.close()
h.close()
