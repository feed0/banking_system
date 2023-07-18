# num de testes
T = int(input())

for i in range(T):
    # N = número de refrigerantes comprados 
    # K = número de garrafas vazias para ganhar uma cheia
    N, K = map(int, input().split())

    # se nao tem troca fica com o que ja tinha
    if N < K:
        print(N)

    # se tem troca: entrega vazia e recebe cheia
    else:
        novas = 0
        while N >= K:
            N -= K
            novas += 1
        
        # as novas mais as que nao trocou
        print(N + novas) 

''' 
TODO Ler as variáveis de entrada N e K. Talvez seja necessário fazer um "split" na linha 
        para obtenção dos valores.
TODO Calcular e imprimir o número de garrafas que o cliente terá no segundo dia, se 
        aproveitar ao máximo a oferta.
'''