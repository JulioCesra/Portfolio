import streamlit as st

st.set_page_config(page_title='Meu Portfólio', layout='wide')

class pagina_principal():

    def inicio():
        inicio_container = st.container()
        inicio_container.title(':blue[Início]')
        inicio_container.title('Olá! Sou Júlio César, entusiasta por ciência de dados e python')
        inicio_container.subheader('''Neste portfólio, compartilho projetos que refletem meu trabalho e aprendizado na área de :blue[ciência de dados, visualização gráfica, e desenvolvimento de soluções inteligentes]. Sempre busco aprender algo novo que me permita criar novas ferramentas afim de auxiliar na solução de problemas reais.
        ''')
        inicio_container.subheader('Aqui você encontrará projetos que demonstram minhas habilidades com :blue[Python, Pandas, Machine Learning e SQL], assim como a análise de dados, e outras tecnologias essenciais para transformar dados em :blue[informações valiosas].')
    
    def sobre_mim():
        sobre_mim_container = st.container()
        sobre_mim_container.title(':blue[Sobre Mim]')
        sobre_mim_container.subheader('Sou :blue[Júlio César], estudante de :blue[Engenharia de Computação na UEMA] e entusiasta da :blue[Ciência de Dados]. Minha curiosidade por tecnologia e dados me levou a explorar ferramentas como :blue[Python, Pandas, Matplotlib, Sklearn e Streamlit] para transformar informações em :blue[insights valiosos].')
        sobre_mim_container.subheader('Atualmente, desenvolvo projetos voltados para :blue[visualização de dados, machine learning, automoção e inteligência de negócios], sempre aplicando boas práticas e buscando soluções eficientes. Meu objetivo é :blue[me tornar um cientista de dados completo], capaz de resolver problemas complexos e gerar impacto real por meio da análise de dados.')
        sobre_mim_container.subheader('Acredito que a tecnologia tem o poder de transformar o mundo, e estou sempre disposto a aprender e encarar novos desafios.')
    
    def meus_projetos():
        meus_projetos_container = st.container()
        meus_projetos_container.title(':blue[Meus Projetos]')
        meus_projetos_container.subheader('Aqui estão alguns dos projetos que desenvolvi, aplicando técnicas de :blue[análise, tratamento, classificação, regressão de dados e desenvolvimento de aplicações interativas].')
        col1, col2, col3 = st.columns(3,border=True)
        
        with col1:
            st.title('Músicas Spotify: Análise Gráfica')
            st.image('grafico2.png')
            st.subheader(':blue[Descrição:] Visualização de gráficos, entender a tendência dos dados e como eles se relacionam')
            st.subheader(':blue[Tecnologias:] Python, Pandas, Matplotlib e Seaborn')
            st.subheader(':blue[Destaque:] Análise gráfica das visualizações, popularidade, artistas mais escutados, álbuns mais escutados, idioma mais visualizado, compositores e produtores mais populares')
            st.link_button(label='Visualizar projeto no Kaggle', url='https://www.kaggle.com/code/juliosilv/songs-deep-analysis')
        with col2:
            st.title('Doenças Pulmonares: Análise e Tratamento de Dados')
            st.image('grafico1.png')
            st.subheader(':blue[Descrição:] Visualização de agrupamentos atráves de gráficos de dados provenientes de informações sobre doenças pulmonares')
            st.subheader(':blue[Tecnologias:] Python, Pandas, Matplotlib e Seaborn')
            st.subheader(':blue[Destaque:] Identificação de valores nulos, percentual das doenças e tipos de tratamento')
            st.link_button(label='Visualizar projeto no Kaggle',url='https://www.kaggle.com/code/juliosilv/lungs-diseases-graphic-analysis-and-data-tratament')
        with col3:
            st.title('Insuficiência Cardiáca: Estudo e Implemtanção de Machine Learning')
            st.image('grafico3.png')
            st.subheader(':blue[Descrição:] Visualização de dados númericos, entender as causas da insuficiência cardiáca e prevenir')
            st.subheader(':blue[Tecnologias:] Python, Pandas, Sklearn, Matplotlib e Seaborn')
            st.subheader(':blue[Destaque:] Análisar a correlação dos colunas númericas, boxplots, divisão de treino e teste, comparação de métricas de erros e escolha do modelo de classificação ou regressão')
            st.link_button(label='Visualizar projeto no Kaggle',url='https://www.kaggle.com/code/juliosilv/heart-failure-ml-and-analysis-for-study')
        
        # Próximos Projetos
        #col4, col5, col6 = st.columns(3, border=True)
        #with col4:
        #    st.title('Gerenciador de Pacientes')
        #    st.subheader(':blue[Descrição:] Site hospedado online com implementação de banco de dados para adicionar, remover, alterar e excluir pacientes, assim como visualizar os dados em tempo real')
        #    st.subheader(':blue[Tecnologias:] Python, Pandas, Streamlit e SQLAlchemy')
        #    st.subheader(':blue[Destaque:] Site com registro único individual de usuário, com a possibilidade de visualizar online o dataset, fácil de utilizar e simples de entender')
    def meus_contatos():
        meus_contatos_container = st.container()
        meus_contatos_container.title(':blue[Meus Contatos]')
        meus_contatos_container.subheader('Estou sempre aberto a novas conexões, colaborações e oportunidades na área de :blue[Ciência de Dados e Engenharia de Computação]. Se quiser trocar ideias ou conhecer mais sobre meu trabalho, entre em contato por qualquer uma das plataformas abaixo:')
        meus_contatos_container.subheader(':blue[Linkedin] - Meu perfil profissional, onde compartilho insights, projetos e interações sobre tecnologia e ciência de dados. Vamos nos conectar!')
        meus_contatos_container.link_button(label='Linkedin',url='https://www.linkedin.com/in/jjuliocesar-silva/')
        meus_contatos_container.subheader(':blue[Kaggle] - Aqui você encontra minhas análises, notebooks e desafios que participei na comunidade de ciência de dados.')
        meus_contatos_container.link_button(label='Kaggle',url='https://www.kaggle.com/juliosilv')
        meus_contatos_container.subheader(':blue[GitHub] - Repositório dos meus projetos, onde compartilho códigos de ciência de dados e desenvolvimento.')
        meus_contatos_container.link_button(label='GitHub',url='https://github.com/JulioCesra')
        meus_contatos_container.subheader('Fique à vontade para me chamar em qualquer uma dessas plataformas!')

    def barra_lateral():
        st.sidebar.image('foto.png', use_container_width=True)
        st.sidebar.title('Júlio César')
        st.sidebar.subheader(':blue[Data Science | Python | Pandas | Streamlit | Machine Learning]')
        opcoes = st.sidebar.multiselect(label='Opções de Contato',options=['Linkedin','Kaggle','GitHub'])
        if opcoes == ['Linkedin']:
            st.sidebar.link_button('Linkedin',url='https://www.linkedin.com/in/jjuliocesar-silva/')
        elif opcoes == ['Kaggle']:
            st.sidebar.link_button('Kaggle',url='https://www.kaggle.com/juliosilv')
        elif opcoes == ['GitHub']:
            st.sidebar.link_button('GitHub',url='https://github.com/JulioCesra')
        menu = st.sidebar.radio('Seções do Portfólio', ['🏠 Início','👤 Sobre Mim','📊 Projetos','📞 Contatos'])
        if menu == '🏠 Início':
            pagina_principal.inicio()
        elif menu == '👤 Sobre Mim':
            pagina_principal.sobre_mim()
        elif menu == '📊 Projetos':
            pagina_principal.meus_projetos()
        elif menu == '📞 Contatos':
            pagina_principal.meus_contatos()
pagina_principal.barra_lateral()
