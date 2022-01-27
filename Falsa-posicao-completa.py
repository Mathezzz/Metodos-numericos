#/////////////Método da falsa posição///////////////
#/Para utilizar esse código, substitua a função/////
#/'#Função testada' para a função que deseja calcular
#/Depois defina o valor inferior e superior do /////
#/intervalo que deseja analisar.////////////////////

#/Acredito que esse método encontrará problemas/////
#/com funções que possuam duas raízes dentro de/////
#/um intervalo de valor 1, ex: função com duas /////
#/raizes entre 1 e 2, se o intervalo pular de 1 em 1
from sys import stdin
import numpy as np
#/Use as funções do numpy para criar as funções problemas/
#/Utilize np.sqrt(termo) para a raiz quadrada do termo////

#Definindo a função matemática que será analisada
#Função testada:
def f(x): return x**2-4
#Definindo os valores do intervalo
intervalo_inferior = -4
intervalo_superior = 2
step=0.5
#O termo e se refere à precisão que deseja
e=0.0002
limite=10 #limite de iterações
#
#Passar o valor do intervalo para ser trabalhado por duas outras variáveis
a= intervalo_inferior
b= intervalo_superior
c=step
#limite de interações
limite=50
#
#Definindo a função que irá achar o valor da raiz após isolar pelo teorema de bolzano
def aproximador(valor1, valor2):
    iteracao=0
    while True:
        xi=(valor1*f(valor2)-valor2*f(valor1))/(f(valor2)-f(valor1)) #método da falsa posição
        print("iteração:", iteracao)
        print("valor encontrado de xi:", xi)
        iteracao=iteracao+1
        if (iteracao==limite):
            return xi
            break
        if (f(xi)==0):
            #este print abaixo é só para me orientar modificando o código
            #print("Achou a raiz, retornando xi", xi)
            return xi
            break
        else:
            if (f(valor1)*f(xi)<0):
                valor2=xi
            else:
                valor1=xi
        if (abs(f(xi))<e):    
            return xi
            break
#/////////////////////////////////////////////////
#/Separação de intervalos de bolzano//////////////
#/O loop a seguir irá percorrer todo o intervalo//
#/procurando valores que o teorema de bolzano seja
#/verdadeiro. Ao encontrar o intervalo, ele chama/
#/a função, passando o intervalo como parâmetro///
#
for ponto in np.arange(a, b, c):     #É necessário somar o stop com o step pois a função é aberta para o valor de stop do intervalo
    
    #Testando o valor inicial de cada intervalo
    if f(a)==0:
        print("intervalo:", a, ponto)
        print("a raiz e", a)

    if f(a)*f(ponto)<0:                 #Se o teorema verdadeiro
        raiz=aproximador(a,ponto)       #A raiz é o valor retornado da função aproximação com o intervalo como parâmetro
        print("intervalo:", a, ponto)
        print("a raiz e", raiz)
    a=ponto
    
#Testando apenas o valor final do último intervalo
if f(b)==0:
    print("intervalo:", a, b)
    print("a raiz e", b)
print("Finalizado")