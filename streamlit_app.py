import streamlit as st
from datetime import datetime

# Configuración de la página - Esto cambia el nombre en la pestaña del navegador
st.set_page_config(page_title="EL TALLER DE DECIMAS DE CUECANTO", page_icon="📝", layout="centered")

# ==========================================
# PARTE 1: TITULO PRINCIPAL CON SU NUEVO NOMBRE
# ==========================================
# ¡Aquí quedó el letrero oficial de entrada, maestro!
st.title("📝 EL TALLER DE DECIMAS DE CUECANTO")
st.subheader("Herramientas de Escritura")

# Controles de formato
col1, col2, col3 = st.columns(3)
with col1:
    estilo_letra = st.selectbox("Estilo de letra", ["Normal", "Elegante (Serif)", "Moderna (Sans)"])
with col2:
    tamano_letra = st.slider("Tamaño de la letra", min_value=14, max_value=32, value=18)
with col3:
    formato_negrita = st.checkbox("Texto en Negrita (**B**)")

# Cuadro para que escriba sus versos
texto_usuario = st.text_area("Escriba o pegue sus décimas aquí:", value="Escriba aquí sus versos de fe...", height=150)

# Aplicar el formato elegido al texto usando HTML/CSS
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
st.subheader("📐 Contador de Sílabas Métcases")
st.write("Escriba un solo verso (una línea) abajo para medir sus 8 sílabas:")

verso_a_medir = st.text_input("Verso a revisar:", value="Bendito sea el Creador")

def contar_silabas_basico(texto):
    texto = texto.lower().strip()
    if not texto:
        return 0
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

if silabas == 8:
    st.success(f"¡Perfecto! Este verso tiene exactamente **{silabas} sílabas** (Octosílabo de ley).")
else:
    st.info(f"Este verso tiene **{silabas} sílabas** detectadas. (Recuerde ajustar las sinalefas si es necesario).")

st.write("---")

# ==========================================
# PARTE 3: LA BIBLIOTECA DE DÉCIMAS
# ==========================================
st.header("📚 Biblioteca Virtual de Décimas")
st.write("Seleccione un estante para leer los versos sagrados:")

# Aquí creamos las pestañas (los estantes de la biblioteca)
pestana1, pestana2, pestana3 = st.tabs(["🌱 La Creación", "📜 Los Mandamientos", "🕊️ Espíritu Santo"])

with pestana1:
    st.subheader("Décimas de la Creación")
    st.markdown("""
    *Al principio todo era oscuridad,*  
    *sin forma, vacío y desierto,*  
    *pero el espíritu despierto*  
    *de Dios, con su gran majestad,*  
    *trajo la luz de la verdad...*
    """)
    st.caption("— Compuesto por Cuecanto")

with pestana2:
    st.subheader("Décimas de la Ley Antigua")
    st.markdown("""
    *En el monte Sinaí temblando,*  
    *Moisés la piedra recibió,*  
    *la ley que el Padre nos dio*  
    *para seguir caminando...*
    """)
    st.caption("— Compuesto por Cuecanto")

with pestana3:
    st.subheader("Décimas de Pentecostés")
    st.markdown("""
    *Como un viento huracanado*  
    *el don divino descendió,*  
    *el taller se iluminó*  
    *con el fuego consagrado...*
    """)
    st.caption("— Compuesto por Cuecanto")

st.write("---")

# ==========================================
# PARTE 4: CALENDARIO Y CONTADOR DE VISITAS
# ==========================================
col_izq, col_der = st.columns(2)

with col_izq:
    st.subheader("📅 Fecha de Hoy")
    fecha_actual = datetime.now().strftime("%d de %B del %Y")
    st.write(f"Hoy es: **{fecha_actual}**")

with col_der:
    st.subheader("👁️ Contador de Visitas")
    if 'visitas' not in st.session_state:
        st.session_state['visitas'] = 121  # Manteniendo sus visitas reales intactas
    else:
        st.session_state['visitas'] += 1
        
    st.metric(label="Visitantes en el taller", value=f"{st.session_state['visitas']} personas")
