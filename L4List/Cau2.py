lst = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(f'List ban dau: \n{lst}')
print("----------------------------------------------")
# a/
print(f'a/ Lay 2 items dau tien cua list : \n{lst[:2]}')
# b/
print(f'b/ Lay 2 items cuoi cung cua list : \n{lst[-2:]}')
# c/
print(f'c/ Lay 2 items cuoi cua list : \n{lst[-2]}\t{lst[-1]}')
# d/
lst.pop(0)
lst.pop(-1)
print(f'd/ Loai bo di item dau va item cuoi cua list : \n{lst}')