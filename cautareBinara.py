from array import array
lista=[]
def citeste():
    n=int(input("Cate numere?:"))
    for i in range(0,n):
        element=input("introdu nr: ")
        lista.append(element)

def insertionSort(lista):

    for step in range(1, len(lista)):
        key = lista[step]
        j = step - 1
        
           
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        lista[j + 1] = key




def binarySearch_iterative(lista, m, low, high):

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
insertionSort(lista)
print(lista)
m=input("Ce numar cauti?")
rez=binarySearch_iterative(lista, m, 0, len(lista)-1)
print("Elementul poate fi gasit la pozitia: ",rez)