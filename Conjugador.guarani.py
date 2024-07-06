import streamlit as st

def conjugate_guarani(morfema):
    pronouns = ["che", "nde", "ha'e", "ñande", "ore", "peẽ", "ha'ekuéra"]
    suffixes = ["a", "re", "i", "ro", "ro", "pe", "hikuái"]
    
    conjugated_forms = [f"{pronoun} {morfema}{suffix}" for pronoun, suffix in zip(pronouns, suffixes)]
    return conjugated_forms

# Estilos personalizados
st.markdown(
    """
    <style>
    .main {
        background-color: #77E843; /* Color de fondo */
    }
    .title-container {
        background-color: #f0f8ff; /* Color del recuadro del título */
        border: 2px solid #000000; /* Borde del recuadro del título */
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .title {
        font-family: 'Arial Black', Gadget, sans-serif;
        color: #000000; /* Color del título */
        text-align: center;
    }
    .input-area {
        font-family: 'Verdana', Geneva, sans-serif;
        color: #000000; /* Color del texto */
        padding: 10px;
        margin-bottom: 10px;
        border: 2px solid #000000; /* Borde de cuadro */
        border-radius: 10px;
    }
    .conjugation {
        font-family: 'Courier New', Courier, monospace;
        color: #000000; /* Color del texto */
        padding: 10px;
        margin: 5px;
        border: 2px solid #000000; /* Borde de cuadro */
        border-radius: 10px;
        background-color: #e6f2ff; /* Color de fondo del cuadro */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title-container"><h1 class="title">Conjugador de Verbos en Guaraní</h1></div>', unsafe_allow_html=True)

morfema = st.text_input("Introduce el morfema del verbo", key="morfema_input")

if st.button("Conjugar"):
    if morfema:
        conjugated_forms = conjugate_guarani(morfema)
        st.markdown(f'<div class="input-area">Conjugación de <strong>{morfema}</strong> en presente indicativo:</div>', unsafe_allow_html=True)
        for form in conjugated_forms:
            st.markdown(f'<div class="conjugation">{form}</div>', unsafe_allow_html=True)
    else:
        st.error("Por favor, introduce un morfema válido.")



#streamlit run /Users/jamesmedinavanini/Downloads/Conju.py
