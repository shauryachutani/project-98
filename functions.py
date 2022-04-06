

def swapfile():
    file1 = input("enter file name1: ")
    file2 = input("enter file name2: ")
    with open(file1,"r") as a:
        dataa = a.read()

    with open(file2,"r") as b:
        datab = b.read()

    with open (file1,"w") as a:
        a.write(datab)

    with open (file2,"w") as b:
        b.write(dataa)

swapfile()

