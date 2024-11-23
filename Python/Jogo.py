print("1-Programacao Estruturada")
print("2-Programacoo Orientada a Objetos")
print("3-Codigo Fonte")
print("4-Codigo Objeto")
print("5-Codigo Executavel")
print("6-Compilador")
print("7-Finalizar")

a=int(input("Escolha uma Opcao: "))

if a == 1:
    print("Programacao Estruturada e um paradigma de programacao que visa melhorar a qualidade, clareza e eficiência no desenvolvimento de programas de computador. Ela utiliza sub-rotinas e tres estruturas basicas: sequencia, selecao (if e switch) e iteracao (laços for e while).")

elif a == 2:
    print("Programacao orientada a objetos e um paradigma de programacao baseado no conceito de objetos, que podem conter dados na forma de campos, também conhecidos como atributos, e codigos, na forma de procedimentos, tambem conhecidos como metodos.")

elif a == 3:
    print("O codigo-fonte e a origem de um programa de computador. E constituido por declaracoes, instrucoes, funcoes, loops e outras definicoes, que atuam como guias para o software saber como operar.")

elif a == 4:
    print("Em computacao, codigo objeto ou modulo objeto e o produto de um compilador. Em um sentido geral código objeto é uma sequência de comandos ou instruções numa linguagem de computador, geralmente numa linguagem código de máquina ou uma linguagem intermediária, como register transfer language.")

elif a == 5: 
    print("codigo-executavel: quando os comandos poderão ser executados pelo sistema operacional, sendo esta a etapa final.")

elif a == 6:
    print("Um compilador é um programa de computador que, a partir de um código fonte escrito em uma linguagem compilada, cria um programa semanticamente equivalente, porém escrito em outra linguagem, código objeto. Classicamente, um compilador traduz um programa de uma linguagem textual.")

elif a == 7:
    print("Obrigado por Jogar")
    
elif a>=8:
    print("Opcao Invalida, escolha uma das 7 Opcoes")