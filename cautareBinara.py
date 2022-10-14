from array import array
lista=[]
def citeste():
    n=int(input("Cate numere?:"))
    for i in range(0,n):
        element=input("introdu nr: ")
        lista.append(element)
    
def binarySearch(lista, m, low, high):

   while low <= high:

        mid = low + (high - low)//2

        if lista[mid] == m:
            return mid

        elif lista[mid] < m:
            low = mid + 1

        else:
            high = mid - 1

    return -1
       
    

citeste()
m=input("Ce numar cauti?")
rez=binarySearch(lista, m, 0, len(lista)-1)
print("Elementul poate fi gasit la pozitia: ",rez)