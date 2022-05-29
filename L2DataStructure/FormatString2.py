s = "Python programming is the best course to learn"
print("Cau 3:")
# a
print("a/ Length of string: ",len(s))
# b
print("b/ First 5 chars: ",s[:5])
# c
print("c/ Last 10 chars: ",s[-10:])
# d
print("d/",s.replace('Python','DUT'))
# e
print("e/ Position of 'best': ",s.find('best'))
# f
print("f/ String is fully upper-case letters : ",s.isupper())
# g
print("g/ Split chars on string:")
ls = s.split()
for i in ls:
    for ii in i:
        print(ii,end =' ')