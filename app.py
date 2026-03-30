import streamlit as st
import time

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Para o Meu Amor ❤️",
    page_icon="❤️",
    layout="centered"
)

# --- ESTILIZAÇÃO CSS (UI/UX) ---
st.markdown("""
    <style>
    /* Fundo e fontes */
    .main { background-color: #fff5f5; }
    
    /* Caixa de destaque principal */
    .hero-box {
        background: white;
        padding: 30px;
        border-radius: 25px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        text-align: center;
        border-bottom: 5px solid #e63946;
        margin-bottom: 25px;
        color: black;
    }
    
    /* Botão personalizado */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        background: linear-gradient(90deg, #e63946, #ff4d6d);
        color: white;
        height: 3.5em;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    
    /* Texto do Inter */
    .inter-box {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 15px;
        border-left: 5px solid #e63946;
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTEÚDO PRINCIPAL ---
st.markdown('<div class="hero-box"><h1>Oi, minha vida! ❤️</h1><p>Desenvolvi algo especial para você saber o quanto eu gosto de ti.</p></div>', unsafe_allow_html=True)

# Botão de ativação com feedback visual
if st.button("CLIQUE PARA LIBERAR O ACESSO"):
    st.balloons() # Balões para comemorar
    st.snow()     # Efeito de "neve" (que no Streamlit são flocos, mas dão um ar mágico)
    
    time.sleep(0.5)
    
    # Mensagem 1: O Sentimento
    st.markdown("### Primeiro de tudo...")
    st.info("Quero que você saiba que **eu quero muito você!**")
    
    # Mensagem 2: O Sorriso
    st.write("---")
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("## ✨")
    with col2:
        st.subheader("O seu sorriso é maravilhoso!")
        st.write("Ele muda o meu dia por completo.")

    # Mensagem 3: A Analogia do Inter (O toque especial)
    st.write("---")
    st.markdown(f"""
    <div class="inter-box">
        <strong>Fato Científico:</strong><br>
        O tanto que você ama o <b>Internacional</b>, multiplica por mil... 
        é exatamente o tanto que eu gosto de você! 🇦🇹❤️
    </div>
    """, unsafe_allow_html=True)

    # Mensagem 4: O Mistério de 11/04
    st.write("---")
    st.subheader("📌 Agendamento Importante")
    
    with st.container():
        st.warning("Data: **11/04**")
        st.write("Reserve esse dia. iremos fazer algo muito especial e vou deixar apenas um gostinho de **segredo** no ar... 🤫")
        
    # Finalização fofa
    st.markdown("---")
    st.caption("Feito com todo carinho pq sou apaixonado por você.")

