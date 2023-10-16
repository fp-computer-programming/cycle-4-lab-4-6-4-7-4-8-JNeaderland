#Authro: Jacob Neaderland
dna0 = input("What is the first in the sequence? ")
dna1 = input("What is the second in the sequence? ")
dna2 = input("What is the third in the sequence? ")
dna3 = input("What is the fourth in the sequence? ")
dna4 = input("What is the fifth in the sequence? ")
dna5 = input("What is the last in the sequence? ")

if dna0 == "a":
    fdna0 = "a - t"
elif dna0 == "c":
    fdna0 = "c - g"
elif dna0 == "t":
    fdna0 = "a - t"
elif dna0 == "g":
    fdna0 = "c-g"

if dna1 == "a":
    fdna1 = "a - t"
elif dna1 == "c":
    fdna1 = "c - g"
elif dna1 == "t":
    fdna1 = "a - t"
elif dna1 == "g":
    fdna1 = "c-g"

if dna2 == "a":
    fdna2 = "a - t"
elif dna2 == "c":
    fdna2 = "c - g"
elif dna2 == "t":
    fdna2 = "a - t"
elif dna2 == "g":
    fdna2 = "c-g"

if dna3 == "a":
    fdna3 = "a - t"
elif dna3 == "c":
    fdna3 = "c - g"
elif dna3 == "t":
    fdna3 = "a - t"
elif dna3 == "g":
    fdna3 = "c-g"

if dna4 == "a":
    fdna4 = "a - t"
elif dna4 == "c":
    fdna4 = "c - g"
elif dna4 == "t":
    fdna4 = "a - t"
elif dna4 == "g":
    fdna4 = "c-g"

if dna5 == "a":
    fdna5 = "a - t"
elif dna5 == "c":
    fdna5 = "c - g"
elif dna5 == "t":
    fdna5 = "a - t"
elif dna5 == "g":
    fdna5 = "c-g"

flist = "{0}, {1}, {2}, {3}, {4}, {5}".format(fdna0, fdna1, fdna2, fdna3, fdna4, fdna5)
print (flist)