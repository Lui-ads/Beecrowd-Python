# The Race of Slugs
while True:
    try:
        qnt = int(input())
        velocidades = list(map(int, input().split()))
        maior = max(velocidades)
        if maior < 10:
            resposta = 1
        elif maior < 20:
            resposta = 2
        else:
            resposta = 3
        print(resposta)
    except EOFError:
        break