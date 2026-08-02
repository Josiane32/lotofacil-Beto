import streamlit as st

st.title("Análise da Lotofácil")

st.write("Digite os 10 últimos jogos da Lotofácil.")

jogos = []

# Cria 10 caixas de texto
for i in range(10):

    jogo = st.text_input(
        f"Jogo {i+1}",
        placeholder="Ex: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15"
    )

    jogos.append(jogo)

# Botão
if st.button("Analisar Jogos"):

    frequencia = {}

    # Conta as frequências
    for jogo in jogos:

        if jogo.strip() == "":
            continue

        numeros = list(map(int, jogo.split()))

        for numero in numeros:

            if numero in frequencia:
                frequencia[numero] += 1
            else:
                frequencia[numero] = 1

    # ===========================
    # Frequência
    # ===========================

    st.header("📊 Frequência dos números")

    for numero in range(1, 26):

        quantidade = frequencia.get(numero, 0)

        st.write(f"Número {numero:2d} → {quantidade} vezes")

    # ===========================
    # Ranking
    # ===========================

    ordenados = sorted(
        frequencia.items(),
        key=lambda item: item[1],
        reverse=True
    )

    st.header("🏆 Ranking")

    for posicao, (numero, quantidade) in enumerate(ordenados, start=1):

        st.write(f"{posicao}º - Número {numero} → {quantidade} vezes")

    # ===========================
    # 14 mais frequentes
    # ===========================

    fixos = []

    for numero, quantidade in ordenados[:14]:
        fixos.append(numero)

    fixos.sort()

    st.header("⭐ 14 números fixos")

    st.write(fixos)

    # ===========================
    # Restantes
    # ===========================

    restantes = []

    for numero in range(1, 26):

        if numero not in fixos:
            restantes.append(numero)

    st.header("🎯 11 números restantes")

    st.write(restantes)

    # ===========================
    # Gera os 11 jogos
    # ===========================

    st.header("🎲 Jogos Gerados")

    texto_download = ""

    resultado = []

    for i, numero_extra in enumerate(restantes, start=1):
        # Faz uma cópia dos 14 números fixos
        novo_jogo = fixos.copy()

        # Acrescenta um número restante
        novo_jogo.append(numero_extra)

        # Coloca em ordem crescente
        novo_jogo.sort()

        # Soma dos números
        soma = sum(novo_jogo)

        st.write(f"### Jogo {i}")

        linha = " ".join(map(str, novo_jogo))
        texto_download += f"{linha}  | Soma: {soma}\n"

        st.code(" ".join(map(str, novo_jogo)))

        st.write(f"**Soma:** {soma}")

        st.divider()

texto_download = ""

for i, numero_extra in enumerate(restantes, start=1):

    novo_jogo = fixos.copy()

    novo_jogo.append(numero_extra)

    novo_jogo.sort()

    soma = sum(novo_jogo)

    linha = " ".join(map(str, novo_jogo))
    texto_download += f"{linha} | Soma: {soma}\n"

    resultado.append({
        "Jogo": i,
        "Números": linha,
        "Soma": soma
    })

# ← O for termina aqui

import pandas as pd

df = pd.DataFrame(resultado)

st.header("🎲 Jogos Gerados")

st.dataframe(df, use_container_width=True)

st.download_button(
    label="📥 Baixar Jogos",
    data=texto_download,
    file_name="jogos_lotofacil.txt",
    mime="text/plain"
)