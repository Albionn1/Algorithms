#marrja e listes nga Perdoruesi
lista = []
n = int(input("Gjatesia e vargut: "))
print("Shtoni permbajtjen e listes duke shtypur enter pas qdo shtimi:")
for i in range(0,n):
    lst = int(input())
    lista.append(lst)
print(lista)
""" ALGORITMET """
def quicksort(lista):
    length = len(lista)     #
    if length <= 1:         #
        return lista        # ==> shikohet gjatesia e array-t qe te sigurohet qe nuk eshte e zbrazet, perkundrazi vazhdohet me pop()
    else:                   #
        pivot = lista.pop() #

    items_greater = []  #
                        # ==> arrays per ruajtjen e vlerave me te madhe ose me te vogel se Pivoti
    items_lower = []    # 

    for item in lista:                  #
        if item > pivot:                #
            items_greater.append(item)  # ==> kontrollohet qdo vlere ne array te marre nga perdoruesi,ne qofte se vlera
        else:                           #   eshte me e madhe se Pivot ateher e shtojme ne array-n items_greater[], nese vlera
            items_lower.append(item)    #   eshte me e vogel e shtojme ne array-n items_lower[]

    return quicksort(items_lower) + [pivot] + quicksort(items_greater) # Kthen arrayn e sortuar

def merge(lista, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    L = [0] * (n1)  #
                    # ==> array-at e perkohshem
    R = [0] * (n2)  #
 
    for i in range(0, n1):      #
        L[i] = lista[l + i]     #
                                # ==> kopjimi i te dhenave ne array-at e perkohshem
    for j in range(0, n2):      #
        R[j] = lista[m + 1 + j] #
 
    # bashkimi i array-ave arr[l...r]
    i = 0     # indeksi fillestar i subArrayt te pare
    j = 0     # indeksi fillestar i subArrayt te dyte
    k = l     # Indeksi fillestar i subArrayt te bashkuar
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            lista[k] = L[i]
            i += 1
        else:
            lista[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        lista[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        lista[k] = R[j]
        j += 1
        k += 1
 
def mergeSort(lista, l, r):
    if l < r:
 
        m = l+(r-l)//2
 
        mergeSort(lista, l, m)
        mergeSort(lista, m+1, r)
        merge(lista, l, m, r)
 
 
    """ n = len(lista)
    print("Given array is")
    for i in range(n):
        print("%d" % lista[i],end=" ") """
 
    """ mergeSort(lista, 0, n-1) """
    """ print("\n\nSorted array is")  """  
    """ for i in range(n):
        print("%d" % lista[i],end=" ") """

def bubblesort(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lista[j] > lista[j + 1] :
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    """ print ("Array i sortuar:") """
    """ for i in range(len(lista)):
        print(lista[i], end=" ") """
"""         print ("% d" % lista[i],end="-")
 """

""" PERFUNDIMI I ALGORITMEVE """

zgjedhja = int(input("""

    Zgjedhni Algoritmin per sortimin e listes

    1.Quicksort

    2.Mergesort

    3.Bubblesort

"""))

if zgjedhja == 1:
    print("Array i sortuar:")
    print(quicksort(lista))
elif zgjedhja == 2:
    mergeSort(lista, 0, n-1)
    print("\n\nArray i sortuar:")
    for i in range(n):
        print("%d" % lista[i],end=" ")
elif zgjedhja == 3:
    bubblesort(lista)
    print ("Array i sortuar:")
    for i in range(len(lista)):
        print(lista[i], end=" ")
