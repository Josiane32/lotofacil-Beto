# ==========================================================
# PROGRAMA LOTOFÁCIL
# Conta os números dos 10 últimos jogos
# Mostra a frequência
# Escolhe os 14 números mais frequentes
# Gera 11 jogos acrescentando um número diferente
# ==========================================================

# Dicionário que irá guardar a frequência de cada número
frequencia = {}

# Lista que armazenará os 10 jogos
jogos = []

print("=" * 60)
print("ANÁLISE DOS 10 ÚLTIMOS JOGOS DA LOTOFÁCIL")
print("=" * 60)

# ----------------------------------------------------------
# LEITURA DOS 10 JOGOS
# ----------------------------------------------------------

for i in range(10):

    print(f"\nJogo {i + 1}")

    entrada = input("Digite os 15 números separados por espaço: ")

    # transforma o texto em lista de números inteiros
    numeros = list(map(int, entrada.split()))

    # verifica se foram digitados 15 números
    if len(numeros) != 15:
        print("Erro! Digite exatamente 15 números.")
        exit()

    # guarda o jogo
    jogos.append(numeros)

    # conta quantas vezes cada número apareceu
    for numero in numeros:

        if numero in frequencia:
            frequencia[numero] += 1
        else:
            frequencia[numero] = 1

# ----------------------------------------------------------
# MOSTRAR QUANTAS VEZES CADA NÚMERO APARECEU
# ----------------------------------------------------------

print("\n")
print("=" * 40)
print("QUANTIDADE DE VEZES QUE CADA NÚMERO SAIU")
print("=" * 40)

for numero in range(1, 26):

    quantidade = frequencia.get(numero, 0)

    print(f"Número {numero:2d} -> {quantidade} vezes")

# ----------------------------------------------------------
# ORDENA DO MAIOR PARA O MENOR
# ----------------------------------------------------------

ordenados = sorted(
    frequencia.items(),
    key=lambda item: item[1],
    reverse=True
)

# ----------------------------------------------------------
# MOSTRA O RANKING
# ----------------------------------------------------------

print("\n")
print("=" * 40)
print("RANKING DOS NÚMEROS")
print("=" * 40)

for posicao, (numero, quantidade) in enumerate(ordenados, start=1):

    print(f"{posicao:2d}º - Número {numero:2d} -> {quantidade} vezes")

# ----------------------------------------------------------
# PEGA OS 14 NÚMEROS MAIS FREQUENTES
# ----------------------------------------------------------

fixos = []

for numero, quantidade in ordenados[:14]:

    fixos.append(numero)

fixos.sort()

# ----------------------------------------------------------
# DESCOBRE OS 11 NÚMEROS RESTANTES
# ----------------------------------------------------------

restantes = []

for numero in range(1, 26):

    if numero not in fixos:
        restantes.append(numero)

# ----------------------------------------------------------
# MOSTRA OS 14 FIXOS
# ----------------------------------------------------------

print("\n")
print("=" * 40)
print("14 NÚMEROS MAIS FREQUENTES")
print("=" * 40)

print(fixos)

# ----------------------------------------------------------
# MOSTRA OS 11 RESTANTES
# ----------------------------------------------------------

print("\n")
print("=" * 40)
print("11 NÚMEROS RESTANTES")
print("=" * 40)

print(restantes)

# ----------------------------------------------------------
# GERA OS 11 NOVOS JOGOS
# ----------------------------------------------------------

print("\n")
print("=" * 60)
print("JOGOS GERADOS")
print("=" * 60)

for i, numero_extra in enumerate(restantes, start=1):

    novo_jogo = fixos.copy()

    novo_jogo.append(numero_extra)

    novo_jogo.sort()

    soma = sum(novo_jogo)

    print(f"\nJogo {i}")

    print(novo_jogo)

    print(f"Soma = {soma}")

print("\n")
print("=" * 60)
print("FIM DO PROGRAMA")
print("=" * 60)