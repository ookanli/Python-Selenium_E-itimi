database = []

def newCreate():
    database.append(input("Öğrenci Adı Soyadı : "))
    menu()

def lists():
    for index, i in enumerate(database):
        print(index," - ", i) 
    menu()

def delete():
    bul = input("Silinecek Öğrenci : ")
    database.remove(bul)
    menu()

def find():
    bul = input("Öğrenci No : ")
    print(database.index(bul))
    menu()

def multipleDelete():
    deleteDb = []
    deleteDb = input("Toplu öğrenci silme: ").split(",")
    i = 0
    while i < len(deleteDb):
        database.pop(int(deleteDb[i]))
        i = i + 1
    menu()

def menu():
    print("1 : Öğrenci ekle")
    print("2 : Öğrenci listele")
    print("3 : Öğrenci sil")
    print("4 : Toplu Öğrenci sil")
    print("5 : Öğrenci numarası öğren")
    islem = input("Yapılacak işlem : ")
    if islem == "1":
        newCreate()
    elif islem == "2":
        lists()
    elif islem == "3":
        delete()
    elif islem == "4":
        multipleDelete()
    elif islem == "5":
        find()
   
menu()