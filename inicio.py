import streamlit as st
import smtplib
from email.message import EmailMessage
from PIL import Image
image_logo = Image.open("jh.png")
def enviar_email(nome, remetente, mensagem):
    email = EmailMessage()
    email['Subject'] = f"📨 Mensagem de contato de {nome}"
    email['From'] = remetente
    email['To'] = "jh6823211@gmail.com"
    email.set_content(f"Nome: {nome}\nE-mail: {remetente}\n\nMensagem:\n{mensagem}")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("jh6823211@gmail.com", "hbey wlcp bunv skxt")
            smtp.send_message(email)
        return True
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        return False

st.set_page_config(page_title="Portifólio",page_icon="💻")
st.logo(image_logo)

text_sobre='''Meu nome é João e minha jornada no mundo da programação começou em 2022, quando me formei em Python e JavaScript. Desde então, a tecnologia deixou de ser só curiosidade e virou uma paixão que levo a sério — mas sem perder o senso de humor quando o código insiste em não colaborar (faz parte, né?).

Em 2023, mergulhei de cabeça no desenvolvimento web e, com o tempo, fui me apaixonando pelo universo completo da programação — do front-end ao back-end. Hoje, meu foco é em desenvolvimento full stack, criando soluções completas que unem boas interfaces com lógicas robustas por trás.

Gosto de construir aplicações que façam sentido, que resolvam problemas reais e que tenham um código limpo e funcional por trás. Levo a sério a ideia de que programar é mais do que escrever código: é pensar em experiências, em performance e em impacto.

Se quiser conhecer meus projetos ou trocar uma ideia, fique à vontade para explorar o portfólio. Quem sabe o próximo sistema incrível a ser criado não é o seu?'''

text_inicio = '''👋 Olá, seja bem-vindo(a)!
Sou João, desenvolvedor(a) focado(a) em transformar ideias em soluções funcionais, eficientes e com código limpo.

Aqui no meu portfólio, você vai encontrar os projetos que desenvolvi, as tecnologias com que trabalho e um pouco da minha trajetória na programação. Se você está procurando alguém que não só entende de código, mas que também se importa com a experiência do usuário, performance e boas práticas… você está no lugar certo.

Fique à vontade para explorar, conhecer meu trabalho e, se quiser trocar uma ideia ou começar um projeto, é só ir até a página de contato.

'''

text_projects=''' 
Ao longo da minha jornada como desenvolvedor full stack, venho criando soluções que misturam lógica, criatividade e muita vontade de resolver problemas reais. Abaixo, alguns dos meus projetos — alguns feitos por curiosidade, outros para facilitar a vida de pessoas e até automatizar processos.

🤖 Automação com API do ChatGPT
Criei um sistema que se conecta à API do ChatGPT para automatizar respostas inteligentes em diferentes contextos. A aplicação permite personalizar o comportamento da IA, armazenar conversas e integrar com outras ferramentas via webhooks. Tudo feito com Python no back-end e uma interface limpa com HTML, CSS e JavaScript puro.

📬 Bot de E-mail Automático
Um script em Python capaz de ler uma planilha de contatos e enviar e-mails personalizados automaticamente, ideal para envios em massa ou notificações periódicas. Inclui logs de envio, verificação de status e integração com SMTP de forma segura.

📊 Painel de Indicadores Simples
Desenvolvi um painel web utilizando apenas JavaScript, HTML e CSS, onde é possível visualizar dados carregados via arquivos CSV ou APIs simples. O sistema organiza, filtra e exibe os dados em tabelas e gráficos gerados dinamicamente com JS puro.

📁 Organizador de Arquivos com Python
Um utilitário local criado com Python que escaneia pastas e organiza arquivos por tipo, extensão ou data automaticamente. Um projeto pequeno, mas extremamente útil para quem vive com o desktop lotado.

🌐 Este Portfólio
Claro, este site também é um projeto meu! Desenvolvido com HTML, CSS e JavaScript, com foco em performance, design responsivo e uma estrutura leve. Afinal, se é pra mostrar trabalho, que seja com estilo e funcionalidade.'''

text_forms='''Minha base como desenvolvedor vem de muita prática, curiosidade e dedicação aos estudos. Aqui estão algumas das formações que contribuíram diretamente para meu desenvolvimento como programador full stack:

📌 Formação em Python – 2022
Curso completo com foco em lógica de programação, automações, manipulação de arquivos, requisições HTTP, tratamento de dados e criação de scripts robustos.
Principais aprendizados: Sintaxe Python, bibliotecas como requests, os, datetime, automações com arquivos e integração com APIs.

📌 Formação em JavaScript – 2022
Estudos voltados ao uso moderno do JavaScript puro, incluindo manipulação de DOM, eventos, lógica condicional, loops e criação de interações dinâmicas para páginas web.
Principais aprendizados: JS Vanilla, eventos, funções assíncronas (async/await), manipulação de elementos e estruturação de scripts organizados.

📌 Desenvolvimento Web – 2023
Curso focado em desenvolvimento de páginas e sistemas com HTML5, CSS3 e JavaScript, com aplicação prática em interfaces responsivas, formulários, boas práticas e semântica web.
Principais aprendizados:HTML/CSS moderno, design responsivo, formulários, layout com Flexbox/Grid e interatividade com JS.

Estou sempre buscando evoluir, testando coisas novas e estudando tecnologias que me ajudem a escrever um código cada vez mais eficiente — porque conhecimento nunca é demais.'''

text_contato='''Se você chegou até aqui, é porque algo chamou sua atenção — seja um projeto, uma ideia ou até a forma como escrevo código (ou textos 👀).

Se quiser conversar, tirar dúvidas, propor uma parceria ou pedir um orçamento, é só me mandar um e-mail. Gosto de ser direto, honesto e sempre busco entender a real necessidade antes de sugerir qualquer solução.

📧 E-mail para contato:
jh6823211@gmail.com

🚀 Bora criar algo juntos?
Se você tem uma ideia, eu tenho o código. Me manda uma mensagem e vamos transformar essa ideia em algo real.

'''
with st.sidebar:

    st.header("Navegar")
    page = st.radio("",["Início","Sobre Mim","Projetos","Formações","Contato"])
if page=="Início":

    st.title("Início")
    with st.container():
        st.write(text_inicio)
elif page=="Sobre Mim":

    st.title("🧠Sobre Mim")
    with st.container():
        st.write(text_sobre)
elif page=="Projetos":

    st.title("💻Projetos")
    with st.container():
        st.write(text_projects)
elif page=="Formações":
    st.title("🎓Formações")
    with st.container():
        st.write(text_forms)
elif page=="Contato":
    st.title("📬Contato")
    with st.container():
        st.write(text_contato)
    st.write("---")
    with st.form("form_contato"):
        nome = st.text_input("Seu nome")
        email = st.text_input("Seu e-mail")
        mensagem = st.text_area("Sua mensagem ou proposta")

        enviado = st.form_submit_button("Enviar Mensagem")

        if enviado:
            if nome and email and mensagem:
                st.success("✅ Mensagem enviada com sucesso! Responderei em breve.")
                enviar_email(nome,email,mensagem)
            else:
                st.error("Por favor, preencha todos os campos antes de enviar.")

    # Rodapé com call to action
    st.markdown("---")
    st.markdown("### 🚀 Bora criar algo juntos?")
    st.markdown("Se você tem uma ideia, eu tenho o código. Me chama! 😄")
