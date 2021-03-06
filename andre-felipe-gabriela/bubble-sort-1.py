import matplotlib.pyplot as plt

#designacao da lista a qual vamos executar os comandos desse progrma
cartas = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]

#representa o numero de elementos dentro da lista 

N = 20
plt.figure()

plt.plot(range(N), cartas, 'ok')

plt.title("grafico da lista original")

plt.xlabel("posicao na lista")

plt.ylabel("valores da lista")

plt.savefig("bubble-inicio.png")

print ("Lista original: ", cartas)

#i representa a posicao do primeiro elemento da lista e j o segundo. O for degigna juntamente com range o intervalo de atuacao do comando. 
#0 representa a primeira posicao da lista, N-1 a ultima possivel para i, e 1 o intervalo de plotagem
#foi realizada tambem a identacao das linhas, para que os comandos fossem rodados simultaneamente, acelerando o processo.
#if indica condicao de posicionamento dos elementos, indicando uma acao a ser efetuada, com determinada condicao. 
#No caso desse programa, a troca da posicao do elemento de acordo com seu valor.
#temp significa uma posicao temporaria do elemento, para que a troca ocorra de forma continua.


a = 0
for i in range(0, N - 1, 1):
    for j in range (i + 1, N, 1):
         
        plt.figure()
        plt.plot(range(N), cartas, 'ok')
        plt.plot(i, cartas [i], "ob")
        plt.plot(j, cartas [j], "or")
        plt.title("grafico da lista ordenada")
        plt.xlabel("posicao na lista")
        plt.ylabel("valores da lista")
        a = a + 1
        plt.savefig("bubble-troca {}.png" .format(a))
        plt.close()
                        
        if cartas[i] > cartas[j]:
            temp = cartas[i]
            cartas[i] = cartas[j]
            cartas[j] = temp
            plt.figure()
            plt.plot(range(N), cartas, 'ok')
            plt.title("grafico da lista ordenada")
            plt.xlabel("posicao na lista")
            plt.ylabel("valores da lista")
            a = a + 1
            plt.savefig("bubble-troca {}.png" .format(a))
            plt.close()
#print plota o resultado do logica de programacao, e colocada fora da identacao para que seja rodada apenas uma vez, no final da operacao.
print("Lista em Ordem Crescente: ", cartas)
#
print("cinco maiores: ", cartas[20:14:-1])

print("cinco menores: ", cartas[0:5:1])

plt.figure()

plt.plot(range(N), cartas, 'ok')

plt.title("grafico da lista ordenada")

plt.xlabel("posicao na lista")

plt.ylabel("valores da lista")

plt.savefig("bubble-fim.png")
