def fmedia():   #define a função principal
    total = 0 # variável para soma das notas inseridas
    contador = 0 #variável contadora para o while loop
    try: #failcheck se o usuário colocar algo que não um número
        while contador < 10: #loop para perguntar as 10 notas ao usuário
            contador += 1 #adiciona 1 ao contador a cada loop
            nota = int(input("Digite sua nota:")) #pergunta a nota ao usuário com controle de entrada int
            total = total + nota # soma a nota inserida à variável de soma das notas
        media = total/10 # calcula a média baseado nas 10 notas
        print("Sua média é:", media) #imprime a média das notas
    except: #caso o usuário não tenha colocado um número
        print("Não digitou um número, tente de novo:") #avisa o usuário que não foi digitado um número
        fmedia() #retorna o script ao começo da função principal para que o usuário possa tentar novamente sem ter que reiniciar o programa manualmente
fmedia() #roda a função principal