import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Portfólio de Ciência de Dados", layout="wide")

# Estilos personalizados
st.markdown("""
    <style>
        .botao-nav {
            display: inline-block;
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            margin: 5px;
            text-decoration: none;
            border-radius: 5px;
            font-size: 16px;
        }
        .centered-title {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Criando botões de navegação no topo
st.markdown("""
<a class="botao-nav" href="#inicio">Início</a>
<a class="botao-nav" href="#sobre">Sobre Mim</a>
<a class="botao-nav" href="#projetos">Projetos</a>
<a class="botao-nav" href="#contato">Contato</a>
""", unsafe_allow_html=True)

# Barra lateral para navegação
st.sidebar.title("Navegação")
st.sidebar.markdown("[Início](#inicio)")
st.sidebar.markdown("[Sobre Mim](#sobre)")
st.sidebar.markdown("[Projetos](#projetos)")
st.sidebar.markdown("[Contato](#contato)")
st.sidebar.image("perfil.jpg", use_column_width=True)

# Seção: Início
st.markdown('<h1 id="inicio" class="centered-title">Bem-vindo ao meu Portfólio!</h1>', unsafe_allow_html=True)
st.write("Aqui você encontra meus projetos e análises de dados.")

# Seção: Sobre Mim
st.markdown('<h1 id="sobre">Sobre Mim</h1>', unsafe_allow_html=True)
st.write("Sou um cientista de dados apaixonado por transformar dados em insights valiosos. Tenho experiência com Python, Pandas, Machine Learning e Visualização de Dados.")

# Seção: Projetos
st.markdown('<h1 id="projetos">Meus Projetos</h1>', unsafe_allow_html=True)
st.write("Aqui estão alguns dos meus projetos de Ciência de Dados:")

# Seção: Contato
st.markdown('<h1 id="contato">Contato</h1>', unsafe_allow_html=True)
st.write("📧 Email: seuemail@email.com")
st.write("🔗 [LinkedIn](https://linkedin.com/in/seu-perfil)")
st.write("📂 [GitHub](https://github.com/seuusuario)")
