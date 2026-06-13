import streamlit as st
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="EL TALLER DE DECIMAS DE CUECANTO", page_icon="📝", layout="centered")

# ==========================================
# BARNIZ DE FONDO: PAPEL ANTIGUO / PERGAMINO
# ==========================================
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1585314062340-f1a5a7c9328d?q=80&w=2070&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    /* Cuadro sutil blanco translúcido de fondo para que las letras resalten impecable */
    .block-container {
        background-color: rgba(255, 255, 255, 0.65);
        padding: 3rem 2rem;
        border-radius: 15px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================
# PARTE 1: TITULO PRINCIPAL
# ==========================================
st.title("📝 EL TALLER DE DECIMAS DE CUECANTO")

# ==========================================
# EL BOTÓN DEL GUITARRÓN CHILENO
# ==========================================
st.write("---")
st.subheader("🎸 El Guitarrón del Taller")
st.write("Pinche la imagen del Guitarrón Chileno para afinar las 25 cuerdas de la tradición:")

url_imagen_guitarron = "https://images.unsplash.com/photo-1510915361894-db8b60106cb1?q=80&w=600&auto=format&fit=crop"

if st.button("🎵 CLAVIJERO DEL POETA: Pinche aquí para afinar el verso"):
    st.markdown("""
    <div style='background-color: rgba(255,255,255,0.9); padding: 15px; border-radius: 10px; border-left: 5px solid #8B4513;'>
        <h4>✨ ¡Guitarrón Afinado en la Variable! ✨</h4>
        <p><i>"Suenen las veinticinco cuerdas con fuerza, de norte a sur, 
        iluminando el libreto con la divina luz del Salvador."</i></p>
    </div>
    """, unsafe_allow_html=True)

st.image(url_imagen_guitarron, caption="Guitarrón de ley - 25 cuerdas para el Canto a lo Divino", width=350)
st.write("---")

# ==========================================
# PARTE 2: HERRAMIENTAS DE ESCRITURA Y FORMATO
# ==========================================
st.subheader("Herramientas de Escritura")

col1, col2, col3 = st.columns(3)
with col1:
    estilo_letra = st.selectbox("Estilo de letra", ["Normal", "Elegante (Serif)", "Moderna (Sans)"])
with col2:
    tamano_letra = st.slider("Tamaño de la letra", min_value=14, max_value=32, value=18)
with col3:
    formato_negrita = st.checkbox("Texto en Negrita (**B**)")

texto_usuario = st.text_area("Escriba o pegue sus décimas aquí:", value="Escriba aquí sus versos de fe...", height=150)

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
# PARTE 3: REVISOR DE 10 LÍNEAS
# ==========================================
st.subheader("📐 Revisor Métrico de la Décima Completa")
st.write("Pegue o escriba su décima de 10 líneas abajo. El sistema medirá cada renglón por separado:")

decima_a_medir = st.text_area(
    "Escriba aquí sus 10 versos para medir:", 
    value="Al principio todo era oscuridad,\nsin forma, vacío y desierto,\npero el espíritu despierto\nde Dios, con su gran majestad,\ntrajo la luz de la verdad.",
    height=220
)

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

lineas = decima_a_medir.split('\n')

st.markdown("### 📊 Reporte del Calce (Línea por Línea):")

for i, linea in enumerate(lineas[:10]):
    if linea.strip():
        cant_silabas = contar_silabas_basico(linea)
        if cant_silabas == 8:
            st.markdown(f"✅ **Línea {i+1}:** `{linea}` — **{cant_silabas} sílabas** (¡De ley!)")
        else:
            st.markdown(f"⚠️ **Línea {i+1}:** `{linea}` — **{cant_silabas} sílabas** (Revisar calce)")

st.write("---")

# ==========================================
# PARTE 4: SECCIÓN DE ESTUDIO E HISTORIA
# ==========================================
st.header("🎓 Rincón del Estudio: El Origen de la Décima")

with st.expander("📖 Pinche aquí para leer la historia y estructura de la décima"):
    st.markdown("""
    ### El Nacimiento de la Espinela
    La décima que utilizamos hoy en día nació en **España en el año 1591**. Fue fijada por el poeta, músico y sacerdote **Vicente Espinel**. Por esta razón, a la décima de diez versos octosílabos se le conoce formalmente en todo el mundo hispanohablante como **Décima Espinela**.
    
    A través de los siglos, esta estructura viajó en los barcos y echó raíces profundas en el alma de América Latina, convirtiéndose en Chile en la llave maestra del **Canto a lo Poeta** (tanto a lo Divino como a lo Humano) y de nuestras queridas cuecas astutas.
    """)

st.write("---")

# ==========================================
# PARTE 5: LA BIBLIOTECA DE DÉCIMAS
# ==========================================
st.header("📚 Biblioteca Virtual de Décimas")
st.write("Seleccione un estante para leer los versos sagrados:")

pestana1, pestana2, pestana3 = st.tabs(["🌱 La Creación", "📜 Los Mandamientos", "🕊️ Espíritu Santo"])

with pestana1:
    st.subheader("Décimas de la Creación")
    st.markdown("""
    Al principio todo era oscuridad, (A)  
    sin forma, vacío y desierto, (B)  
    pero el espíritu despierto (B)  
    de Dios, con su gran majestad, (A)  
    trajo la luz de la verdad. (A)  
    Separó las aguas del cielo, (C)  
    puso la semilla en el suelo, (C)  
    creó las estrellas y el sol, (D)  
    con su divino crisol (D)  
    le dio la vida a este suelo. (C)
    """)
    st.caption("— Compuesto por Juanito")

with pestana2:
    st.subheader("Décimas de la Ley Antigua")
    st.markdown("""
    En el monte Sinaí temblando, (A)  
    Moisés la piedra recibió, (B)  
    la ley que el Padre nos dio (B)  
    para seguir caminando. (A)  
    Su santa voz escuchando (A)  
    el pueblo su rumbo fijó, (C)  
    la alianza eterna selló (C)  
    con un mensaje de amor, (D)  
    siguiendo al buen Salvador (D)  
    que por la senda mandó. (C)
    """)
    st.caption("— Compuesto por Juanito")

with pestana3:
    st.subheader("Décimas de Pentecostés")
    st.markdown("""
    Como un viento huracanado (A)  
    el don divino descendió, (B)  
    el taller se iluminó (B)  
    con el fuego consagrado. (A)  
    El temor ha terminado, (A)  
    hablan lenguas sin cesar, (C)  
    la palabra hay que llevar (C)  
    con valentía y con fe, (D)  
    alza tu voz, ponte en pie, (D)  
    vamos todos a cantar. (C)
    """)
    st.caption("— Compuesto por Juanito")

st.write("---")

# ==========================================
# PARTE 6: CALENDARIO Y VISITAS
# ==========================================
col_izq, col_der = st.columns(2)

with col_izq:
    st.subheader("📅 Fecha de Hoy")
    fecha_actual = datetime.now().strftime("%d de %B del %Y")
    st.write(f"Hoy es: **{fecha_actual}**")

with col_der:
    st.subheader("👁️ Contador de Visitas")
    if 'visitas' not in st.session_state:
        st.session_state['visitas'] = 121
    else:
        st.session_state['visitas'] += 1
    st.metric(label="Visitantes en el taller", value=f"{st.session_state['visitas']} personas")
