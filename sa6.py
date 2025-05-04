sair = bool
x = int
n = int
op = int
numero = [1,2,3,4,5]

def escrever():
    #este procedimento é para escrever a mensagem
    print("Vetor Ordenado: ")
    for x in range(1,20):
        print(numero[x])

#este procedimento bubble sort para ordenar
def bubbleSort(numero, n):
    for x in range(n - 1): #loop externo de 1 até n-1
        for j in range(n - x - 1): #loop interno de 1 até n-x
         if numero[j] > numero[j+1]: #comparação entre os elementos
            numero[j], numero[j+1] = numero[j+1], numero[j] #troca de elementos

#procedimento para mesclar dois subvetores
def mesclar(numero, ini, meio, fim):
    outro = [0] * len(numero) #criação de um vetor auxiliar
    i = ini
    j = meio + 1
    k = ini

    #mesclar a ordem
    while i <= meio and j <= fim:
        if numero[i] <= numero[j]:
            outro[k] = numero[i]
            i += 1
        else:
            outro[k] = numero[j]
            j += 1
        k += 1
    
    #copiar os elementos restantes do primeiro vetor
    while i <= meio: 
        outro[k] = numero[i]
        i += 1
        k += 1

     #copiar os elementos restantes do segundo valor
    while j <= fim:
        outro[k] = numero[j]
        j += 1
        k += 1

    #copiar os mesclados para o vetor original
    for i in range(ini, fim + 1):
        numero[i] = outro[i]
    
def merge_sort(numero, ini, fim):
    if ini < fim:
        meio = (ini + fim) // 2 
        merge_sort(numero, ini, meio)
        merge_sort(numero,meio + 1,fim)
        mesclar(numero, ini, meio, fim)    

#inicialização do vetor
numero = [1,7,10,9,2,3,20,18,33,90,44,34,30,21,27,5,8,99,54,68]

#exibir o vetor original
print("Vetor Original: ")
print(numero)

sair = False

while not sair:

    print("\n==================MENU============")
    print("1 - Bubble Sort")
    print("2 - Merge Sort")
    print("3 - Sair")

    try:
        op = int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção inválida, tente novamente.")
        continue

    if op == 1:
        print("\n1 - Bubble Sort")
        bubbleSort(numero, len(numero))
        print("Vetor Ordenado (Bubble Sort): ")
        print(numero)
    elif op == 2:
        print("\n2 - Merge Sort")
        merge_sort(numero, 0, len(numero) - 1)
        print("\nVetor Ordenado (Merge Sort): ")
        print(numero)
    elif op == 3:
        print("Saindo...")
        sair = True
    else:
        print("Opção inválida, tente novamente.")
