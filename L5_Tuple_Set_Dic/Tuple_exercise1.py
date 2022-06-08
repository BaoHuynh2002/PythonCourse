tup1 = ("i","l","o","v","e","y","o","u","very","much")
# yeucau1:
print(f"#Yeu cau 1: \n{tup1}")
# yeucau2:
print("#Yeu cau 2:")
idp = int(input("positive index (0..9): "))
while (idp<0 or idp>=10):
    idp = int(input("positive index: "))

idn = int(input("negative index (-10..-1): "))
while (idn<-10 or idn>-1):
    idn = int(input("negative index: "))

print(f"value of index [{idp}] = {tup1[idp]}")
print(f"value of index [{idn}] = {tup1[idn]}")
# yeucau3:
print("#Yeu cau 3:")
st = input("input string to find : ")
print (f"Is '{st}' in tuple ? {st in tup1}")
print (f"The word '{st}' appears {tup1.count(st)} time(s)")