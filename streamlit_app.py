import streamlit as st
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Décimas de Dios", page_icon="🎈", layout="centered")

# ==========================================
# PARTE 1: BARRA DE FORMATO DE TEXTO
# ==========================================
st.title("📝 El Taller de las Décimas de Dios")
st.subheader("Herramientas de Escritura")

# Controles de formato
col1, col2, col3 = st.columns(3)
with col1:
    estilo_letra = st.selectbox("Estilo de letra", ["Normal", "Elegante (Serif)", "Moderna (Sans)"])
with col2:
    tamano_letra = st.slider("Tamaño de la letra", min_value=14, max_value=32, value=18)
with col3:
    formato_negrita = st.checkbox("Texto en Negrita (**B**)")

# Cuadro para que Juanito escriba sus versos
texto_usuario = st.text_area("Escriba o pegue sus décimas aquí:", value="Escriba aquí sus versos de fe...", height=200)

# Aplicar el formato elegido al texto usando HTML/CSS simples
estilo_css = f"font-size: {tamano_letra}px; "
if estilo_letra == "Elegante (Serif)":
    estilo_css += "font-family: serif; "
elif estilo_letra == "Moderna (Sans)":
    estilo_css += "font-family: sans-serif; "

if formato_negrita:
    estilo_css += "font-weight: bold; "

st.markdown("### 👁️ Vista Previa de su Verso:")
st.markdown(f'<p style="{estilo_css}">{texto_usuario.replace("\n", "<br>")}</p>', unsafe_allow_html=True)

st.write("---")

# ==========================================
# PARTE 2: CONTADOR DE SÍLABAS Y RIMAS
# ==========================================
st.subheader("📐 Contador de Sílabas Métricas")
st.write("Escriba un solo verso (una línea) abajo para medir sus 8 sílabas:")

verso_a_medir = st.text_input("Verso a revisar:", value="Bendito sea el Creador")

# Función básica para contar sílabas (aproximación para el taller)
def contar_silabas_basico(texto):
    texto = texto.lower().strip()
    if not texto:
        return 0
    # Contador simple basado en grupos de vocales
    vocales = "aeiouáéíóúü"
    conteo = 0
    en_vocal = False
    for char in texto:
        if char in vocales:
            if not en_vocal:
                conteo += 1
                en_vocal = True
        else:
            en_vocal = False
    return conteo

silabas = contar_silabas_basico(verso_a_medir)

# Mostrar el resultado con color según la ley de la octosílaba
if silabas == 8:
    st.success(f"¡Perfecto! Este verso tiene exactamente **{silabas} sílabas** (Octosílabo de ley).")
else:
    st.info(f"Este verso tiene **{silabas} sílabas** detectadas. (Recuerde ajustar las sinalefas si es necesario).")

st.write("---")

# ==========================================
# PARTE 3: CALENDARIO Y CONTADOR DE VISITAS
# ==========================================
# Usamos columnas abajo para el rincón de datos
col_izq, col_der = st.columns(2)

with col_izq:
    st.subheader("📅 Fecha de Hoy")
    fecha_actual = datetime.now().strftime("%d de %B del %Y")
    st.write(f"Hoy es: **{fecha_actual}**")

with col_der:
    st.subheader("👁️ Contador de Visitas")
    # Inicializamos un contador simulado en la memoria de la página
    if 'visitas' not in st.session_state:
        st.session_state['visitas'] = 104  # Empezamos con un número bonito de muestra
    else:
        st.session_state['visitas'] += 1
        
    st.metric(label="Visitantes en el taller", value=f"{st.session_state['visitas']} personas")
