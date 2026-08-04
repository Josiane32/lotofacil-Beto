# ============================================================
# PROJETO: Gerador Inteligente da Lotofácil
#
# Autor: Josiane (adaptado para estudos)
#
# Objetivo:
# Ler os 10 últimos concursos da Lotofácil,
# calcular a frequência dos números e gerar
# 11 novos jogos utilizando os 14 números
# mais frequentes.
# ============================================================

# ---------
# Bibliotecas
# ---------

import streamlit as st
import pandas as pd

# -------------------------------------------------------
# Configuração da página
# -------------------------------------------------------

st.set_page_config(
    page_title="Gerador Inteligente da Lotofácil",
    page_icon="🍀",
    layout="wide"
)

# -------------------------------------------------------
# CSS
# Esta parte muda totalmente o visual do Streamlit.
# -------------------------------------------------------

st.markdown("""
<style>

/* Fundo */

.stApp{
    background:linear-gradient(
        135deg,
        #0b6623,
        #17853d,
        #26a65b
    );
}

/* Título principal */

h1{
    color:white;
    text-align:center;
}

/* Subtítulos */

h2,h3{
    color:#FFD54F;
}

/* Caixa branca */

.card{

    background:white;

    padding:20px;

    border-radius:15px;

    margin-bottom:20px;

    box-shadow:0px 4px 12px rgba(0,0,0,0.25);

}

/* Bolinhas dos números */

.numero{

    display:inline-block;

    width:42px;

    height:42px;

    line-height:42px;

    text-align:center;

    border-radius:50%;

    background:#2E7D32;

    color:white;

    font-weight:bold;

    margin:4px;

    font-size:18px;

}

/* Botão */

.stButton>button{

    background:#FFD54F;

    color:black;

    width:100%;

    border:none;

    border-radius:10px;

    font-size:18px;

    font-weight:bold;

}

/* Download */

.stDownloadButton>button{

    background:#0B6623;

    color:white;

    width:100%;

    border:none;

    border-radius:10px;

    font-size:18px;

}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# Título
# -------------------------------------------------------

st.title("🍀 Gerador Inteligente da Lotofácil")

st.write(
"""
Digite abaixo os **10 últimos resultados**
da Lotofácil.

Cada linha deve possuir exatamente **15 números**
separados por espaço.
"""
)

# -------------------------------------------------------
# Função que desenha os números em bolinhas verdes
# -------------------------------------------------------

def mostrar_bolinhas(lista_numeros):

    html = ""

    for numero in lista_numeros:

        html += f"<span class='numero'>{numero:02d}</span>"

    st.markdown(html, unsafe_allow_html=True)

# -------------------------------------------------------
# Função para contar a frequência
# -------------------------------------------------------

def contar_frequencia(lista_jogos):

    frequencia = {}

    for jogo in lista_jogos:

        # Ignora linhas vazias
        if jogo.strip() == "":
            continue

        try:

            numeros = list(map(int, jogo.split()))

        except ValueError:

            st.error("Digite somente números separados por espaço.")

            st.stop()

        # Verifica se possui 15 números

        if len(numeros) != 15:

            st.error("Cada jogo deve possuir exatamente 15 números.")

            st.stop()

        # Soma as aparições

        for numero in numeros:

            frequencia[numero] = frequencia.get(numero, 0) + 1

    return frequencia

# ============================================================
# PARTE 2
# Entrada dos 10 concursos e análise das frequências
# ============================================================

# Lista onde serão armazenados os jogos digitados
jogos = []

st.divider()

st.subheader("📝 Digite os 10 últimos concursos")

# Cria as 10 caixas de texto
for i in range(10):

    jogo = st.text_input(
        label=f"Concurso {i + 1}",
        placeholder="Ex: 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15",
        key=f"jogo_{i}"
    )

    jogos.append(jogo)

st.divider()

# Botão principal
analisar = st.button("🍀 Analisar Jogos")

# Todo o restante será executado somente
# quando o botão for clicado.

if analisar:

    # Conta quantas vezes cada número apareceu
    frequencia = contar_frequencia(jogos)

    # Se nenhum jogo foi digitado
    if len(frequencia) == 0:

        st.warning("Digite pelo menos um concurso.")

        st.stop()

    # ========================================================
    # Frequência
    # ========================================================

    st.header("📊 Frequência dos números")

    dados = pd.DataFrame({

        "Número": list(range(1,26)),

        "Frequência":[
            frequencia.get(i,0)
            for i in range(1,26)
        ]

    })

    # Gráfico
    st.bar_chart(
        dados.set_index("Número")
    )

    # Mostra a tabela

    st.dataframe(
        dados,
        use_container_width=True,
        hide_index=True
    )

    # ========================================================
    # Ranking
    # ========================================================

    ordenados = sorted(

        frequencia.items(),

        key=lambda item:item[1],

        reverse=True

    )

    ranking = []

    for posicao,(numero,quantidade) in enumerate(
        ordenados,
        start=1
    ):

        ranking.append({

            "Posição":posicao,

            "Número":numero,

            "Apareceu":quantidade

        })

    st.header("🏆 Ranking dos números")

    st.dataframe(

        pd.DataFrame(ranking),

        use_container_width=True,

        hide_index=True

    )

    # ========================================================
    # Seleciona os 14 números mais frequentes
    # ========================================================

    fixos = sorted(

        numero

        for numero,_ in ordenados[:14]

    )

    st.header("⭐ 14 números fixos")

    mostrar_bolinhas(fixos)

    # ========================================================
    # Descobre quais sobraram
    # ========================================================

    restantes = [

        numero

        for numero in range(1,26)

        if numero not in fixos

    ]

    st.header("🎯 Números restantes")

    mostrar_bolinhas(restantes)

    # ========================================================
    # Geração dos 11 jogos
    # ========================================================

    st.header("🎲 Jogos Gerados")

    resultado = []

    texto_download = ""

    # Cada número restante será combinado
    # com os 14 números fixos.

    for indice, numero_extra in enumerate(restantes, start=1):

        novo_jogo = fixos.copy()

        novo_jogo.append(numero_extra)

        novo_jogo.sort()

        soma = sum(novo_jogo)

        resultado.append({

            "Jogo": indice,

            "Numeros": novo_jogo,

            "Soma": soma

        })

        texto_download += (
            f"Jogo {indice}: "
            + " ".join(f"{n:02d}" for n in novo_jogo)
            + f" | Soma: {soma}\n"
        )

    # ========================================================
    # Mostra cada jogo em um cartão
    # ========================================================

    for jogo in resultado:

        st.markdown(
            """
            <div class='card'>
            """,
            unsafe_allow_html=True
        )

        st.subheader(f"🎯 Jogo {jogo['Jogo']}")

        mostrar_bolinhas(jogo["Numeros"])

        st.markdown(
            f"""
            <div style="
                background: linear-gradient(90deg, #FFD54F, #FFC107);
                color: #1B1B1B;
                padding: 12px;
                border-radius: 10px;
                text-align: center;
                font-size: 20px;
                font-weight: bold;
                margin-top: 15px;
                box-shadow: 0px 2px 8px rgba(0,0,0,0.2);
            ">
                💰 Soma dos números: {jogo['Soma']}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

    # ========================================================
    # Download
    # ========================================================

    st.download_button(

        label="📥 Baixar Jogos em TXT",

        data=texto_download,

        file_name="Jogos_Lotofacil.txt",

        mime="text/plain"

    )

    # ========================================================
    # Estatísticas finais
    # ========================================================

    st.divider()

    st.subheader("📈 Resumo da análise")

    numero_mais = ordenados[0][0]
    vezes_mais = ordenados[0][1]

    numero_menos = ordenados[-1][0]
    vezes_menos = ordenados[-1][1]

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Número mais frequente",
            f"{numero_mais:02d}",
            f"{vezes_mais} aparições"
        )

    with col2:
        st.metric(
            "Número menos frequente",
            f"{numero_menos:02d}",
            f"{vezes_menos} aparições"
        )

    st.success("Análise concluída com sucesso! 🍀")