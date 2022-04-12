vetor = []
#def preencherVetor():
#    vetor = ['1', '5', '7']
#    for i in range(len(vetor)):
#        print(vetor[i])

#Segunda forma de fazer
def preencherVetor2():
    for i in range(101):
        vetor.append(i+1)#Append(adicionar elementos dentro do vetor)

def mostrarVetor():
    preencherVetor2()
    for i in range(101):
        print(vetor[i])