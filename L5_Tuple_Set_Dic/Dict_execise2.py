myDict = {
    "I" : ["toi","to","minh","tui","em"],
    "love" : ["yeu","quy","say me","dam say"],
    "you" : ["em","ban","cau","dong chi"]
}
def checkchoose(num):
    if (num>0 and num<=5):
        return True
    else:
        return False
def switch(num):
    if num == 1:
        print("-----------------------------------------------")
        print("In tu dien: ")
        item = myDict.keys()
        for i in item:
            print(f"\t{i} : {myDict[i]}")
        print("-----------------------------------------------")
    elif num==2:
        print("-----------------------------------------------")
        nw = input("Nhap tu tieng Anh moi: ")
        tv = input("Nhap nghia tu tieng Anh \n(Neu nhieu nghia, cach nhau boi dau ','): ")
        listtv = list(tv.split(','))
        x=0
        for i in listtv:
            ni = i.strip()
            listtv[x] = ni
            x+=1
        myDict.update({nw : listtv})
        print(f"# Da luu vao tu dien.")
        print("-----------------------------------------------")
    elif num == 3:
        print("-----------------------------------------------")
        ip = input("Nhap tu tieng Anh can tim: ")
        try:
            print(f"# Ket qua: \n\t{ip} : {myDict[ip]}")
        except:
            print(f"# Khong co tu {ip} trong tu dien.")
        print("-----------------------------------------------")
    elif num == 4:
        print("-----------------------------------------------")
        ip = input("Nhap tu tieng Viet can tim: ")
        listta = list()
        for key in myDict.keys():
            for nghia in myDict[key]:
                if ip == nghia:
                    listta.append(key)
        print("# Ket qua:")
        if not listta:
            print(f"# Khong co trong tu dien.")
        else:
            for key in listta:
                print(f"\t{key} : {myDict[key]}")
        print("-----------------------------------------------")
    elif num == 5:
        ip = input("Nhap tu tieng Anh can xoa: ")
        try:
            myDict.pop(ip)
            print(f"Da xoa tu '{ip}' khoi tu dien")
        except:
            print(f"# Khong co tu {ip} trong tu dien.")
        print("-----------------------------------------------")
print("TU DIEN ANH - VIET:\n\t#1. Hien thi tu dien.\n\t#2. Them tu vao tu dien.\n\t#3. Tim kiem tu dien (tu Tieng Anh).\n\t#4. Tim kiem tu dien (tu Tieng Viet).\n\t#5. Xoa tu trong tu dien (nhap tu tieng Anh).\n\t#6. Thoat.")
choose = int(input("Lua chon (1..6) : "))
while (checkchoose(choose)):
    switch(choose)
    choose = int(input("Lua chon (1..6) : "))
if choose == 6: 
    print("-----------------------------------------------")
    print("#Bye!")
else: 
    print("-----------------------------------------------")
    print("#Out of range [1..6].")