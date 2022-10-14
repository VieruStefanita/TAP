from array import array
lista=[]
def citeste():
    n=int(input("Cate numere?:"))
    for i in range(0,n):
        element=input("Introdu nr: ")
        lista.append(element)
    
def LinearSearch(l,m):
    p=-1
    for i in range (0,len(lista)-1):
        if (lista[i] == m ):
            p=i
       
    print("Elementul poate fi gasit la pozitia: ",p)

citeste()
m=input("Ce numar cauti? ")
LinearSearch(lista,m)