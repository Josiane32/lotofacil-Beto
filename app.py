import streamlit as st
import pandas as pd

st.set_page_config(page_title="Análise da Lotofácil", layout="wide")

st.title("🎯 Análise da Lotofácil")

st.write("Digite os 10 últimos resultados da Lotofácil.")

jogos = []

# Entradas
for i in range(10):
    jogo = st.text_input(
        f"Jogo {i+1}",
        placeholder="Ex: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15"
    )
    jogos.append(jogo)

# Botão
if st.button("Analisar Jogos"):

    frequencia = {}

    # Conta a frequência
    for jogo in jogos:

        if jogo.strip() == "":
            continue

        try:
            numeros = list(map(int, jogo.split()))
        except:
            st.error("Digite apenas números separados por espaço.")
            st.stop()

        if len(numeros) != 15:
            st.error("Cada jogo deve possuir exatamente 15 números.")
            st.stop()

        for numero in numeros:
            frequencia[numero] = frequencia.get(numero, 0) + 1

    # Frequência
    st.header("📊 Frequência")

    for numero in range(1, 26):
        st.write(f"Número {numero:2d} → {frequencia.get(numero,0)} vezes")

    # Ranking
    ordenados = sorted(
        frequencia.items(),
        key=lambda x: x[1],
        reverse=True
    )

    st.header("🏆 Ranking")

    for posicao, (numero, quantidade) in enumerate(ordenados, start=1):
        st.write(f"{posicao}º - Número {numero} → {quantidade} vezes")

    # 14 mais frequentes
    fixos = sorted([numero for numero, _ in ordenados[:14]])

    st.header("⭐ 14 números fixos")
    st.write(fixos)

    # Restantes
    restantes = [n for n in range(1, 26) if n not in fixos]

    st.header("🎯 11 números restantes")
    st.write(restantes)

    # Jogos gerados
    st.header("🎲 Jogos Gerados")

    resultado = []
    texto_download = ""

    for i, numero_extra in enumerate(restantes, start=1):

        novo_jogo = fixos.copy()
        novo_jogo.append(numero_extra)
        novo_jogo.sort()

        soma = sum(novo_jogo)

        linha = " ".join(map(str, novo_jogo))

        resultado.append({
            "Jogo": i,
            "Números": linha,
            "Soma": soma
        })

        texto_download += f"Jogo {i}: {linha} | Soma: {soma}\n"

    df = pd.DataFrame(resultado)

    st.dataframe(df, use_container_width=True)

    st.download_button(
        label="📥 Baixar Jogos",
        data=texto_download,
        file_name="jogos_lotofacil.txt",
        mime="text/plain"
    )