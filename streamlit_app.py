import streamlit as st
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="EL TALLER DE DECIMAS DE CUECANTO", page_icon="📝", layout="centered")

# ==========================================
# MAESTRÍA EN CSS: Barniz de Madera Rústica
# ==========================================
st.markdown(
    """
    <style>
    /* Fondo principal: Textura de Madera de Nogal Rústica */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1533038590840-1cde6e668a91?q=80&w=2070&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    
    /* Contenedor central integrado, translúcido sobre la madera */
    .block-container {
        background-color: rgba(253, 246, 227, 0.6); /* Tono crema muy suave y transparente */
        padding: 2.5rem 2rem;
        border-radius: 20px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
    }

    /* Títulos y Subtítulos con color madera oscura */
    h1, h2, h3, h4, h5, h6 {
        color: #4a2c16 !important;
    }

    /* Fusión de botones: Efecto de tallado o pirograbado */
    div.stButton > button {
        background-color: rgba(101, 67, 33, 0.2) !important;
        color: #4a2c16 !important;
        border: 2px solid #5c3a21 !important;
        border-radius: 10px !important;
        padding: 10px 20px !important;
        font-weight: bold !important;
        transition: all 0.3s ease;
    }
    
    div.stButton > button:hover {
        background-color: rgba(92, 58, 33, 0.9) !important;
        color: #ffffff !important;
        transform: scale(1.02);
    }

    /* Integración de las pestañas de la biblioteca con tonos madera */
    .stTabs [data-baseweb="tab-list"] {
        background-color: rgba(101, 67, 33, 0.15) !important;
        border-radius: 10px;
        padding: 5px;
    }

    .stTabs [data-baseweb="tab"] {
        color: #5c3a21 !important;
        font-weight: bold;
    }

    .stTabs [aria-selected="true"] {
        background-color: rgba(101, 67, 33, 0.3) !important;
        border-radius: 8px;
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
# EL BOTÓN DEL GUITARRÓN CHILENO INTEGRADO CON AUDIO
# ==========================================
st.write("---")
st.subheader("🎸 El Guitarrón del Taller")
st.write("Pinche la imagen del Guitarrón Chileno para afinar las 25 cuerdas de la tradición:")

url_imagen_guitarron = "https://images.unsplash.com/photo-1510915361894-db8b60106cb1?q=80&w=600&auto=format&fit=crop"

# Enlace a un audio limpio de un rasgueo/acorde tradicional de cuerdas
url_audio_guitarron = "https://assets.mixkit.co/active_storage/sfx/123/123-84.wav"

if st.button("🎵 CLAVIJERO DEL POETA: Pinche aquí para afinar el verso"):
    # Mensaje en pantalla
    st.markdown("""
    <div style='background-color: rgba(255, 255, 255, 0.85); padding: 15px; border-radius: 10px; border-left: 5px solid #5c3a21; color: #2b1d0c;'>
        <h4>✨ ¡Guitarrón Afinado en la Variable! ✨</h4>
        <p><i>"Suenen las veinticinco cuerdas con fuerza, de norte a sur, 
        iluminando el libreto con la divina luz del Salvador."</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Inyección de HTML invisible para forzar la reproducción automática del audio al hacer click
    html_audio = f"""
        <iframe src="{url_audio_guitarron}" allow="autoplay" style="display:none" id="iframeAudio"></iframe>
        <audio autoplay><source src="{url_audio_guitarron}" type="audio/wav"></audio>
    """
    st.markdown(html_audio, unsafe_allow_html=True)

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

ststyle_css = f"font-size: {tamano_letra}px; color: #1a1a1a; "
if estilo_letra == "Elegante (Serif)":
    ststyle_css += "font-family: serif; "
elif estilo_letra == "Moderna (Sans)":
    ststyle_css += "font-family: sans-serif; "

if formato_negrita:
    ststyle_css += "font-weight: bold; "

st.markdown("### 👁️ Vista Previa de su Verso:")
st.markdown(f'<p style="{ststyle_css}">{texto_usuario.replace("\n", "<br>")}</p>', unsafe_allow_html=True)

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
            st.markdown(f"✅ **Línea {i+1}:** `{linea}` — **{cant_silabas} sílabas**")
        else:
            st.markdown(f"<span style='color: #654321;'>⚠️ **Línea {i+1}:** `{linea}` — **{cant_silabas} sílabas**</span>", unsafe_allow_html=True)

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

estilo_texto_biblioteca = "color: #2b1d0c; font-style: italic;"

with pestana1:
    st.subheader("Décimas de la Creación")
    st.markdown(f"""
    <p style="{estilo_texto_biblioteca}">
    Al principio todo era oscuridad, (A)<br>
    sin forma, vacío y desierto, (B)<br>
    pero el espíritu despierto (B)<br>
    de Dios, con su gran majestad, (A)<br>
    trajo la luz de la verdad. (A)<br>
    Separó las aguas del cielo, (C)<br>
    puso la semilla en el suelo, (C)<br>
    creó las estrellas y el sol, (D)<br>
    con su divino crisol (D)<br>
    le dio la vida a este suelo. (C)
    </p>
    """, unsafe_allow_html=True)
    st.caption("— Compuesto por Juanito")

with pestana2:
    st.subheader("Décimas de la Ley Antigua")
    st.markdown(f"""
    <p style="{estilo_texto_biblioteca}">
    En el monte Sinaí temblando, (A)<br>
    Moisés la piedra recibió, (B)<br>
    la ley que el Padre nos dio (B)<br>
    para seguir caminando. (A)<br>
    Su santa voz escuchando (A)<br>
    el pueblo su rumbo fijó, (C)<br>
    la alianza eterna selló (C)<br>
    con un mensaje de amor, (D)<br>
    siguiendo al buen Salvador (D)<br>
    que por la senda mandó. (C)
    </p>
    """, unsafe_allow_html=True)
    st.caption("— Compuesto por Juanito")

with pestana3:
    st.subheader("Décimas de Pentecostés")
    st.markdown(f"""
    <p style="{estilo_texto_biblioteca}">
    Como un viento huracanado (A)<br>
    el don divino descendió, (B)<br>
    el taller se iluminó (B)<br>
    con el fuego consagrado. (A)<br>
    El temor ha terminado, (A)<br>
    hablan lenguas sin cesar, (C)<br>
    la palabra hay que llevar (C)<br>
    con valentía y con fe, (D)<br>
    alza tu voz, ponte en pie, (D)<br>
    vamos todos a cantar. (C)
    </p>
    """, unsafe_allow_html=True)
    st.caption("— Compuesto por Juanito")

st.write("---")

# ==========================================
# PARTE 6: CALENDARIO Y VISITAS
# ==========================================
col_izq, col_der = st.columns(2)

with col_izq:
    st.subheader("📅 Fecha de Hoy")
    meses_es = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    ahora = datetime.now()
    dia = ahora.day
    mes = meses_es[ahora.month - 1]
    anio = ahora.year
    st.markdown(f"<p style='color: #4a2c16; font-weight: bold;'>Hoy es: {dia} de {mes} del {anio}</p>", unsafe_allow_html=True)

with col_der:
    st.subheader("👁️ Contador de Visitas")
    if 'visitas' not in st.session_state:
        st.session_state['visitas'] = 121
    else:
        st.session_state['visitas'] += 1
    st.metric(label="Visitantes en el taller", value=f"{st.session_state['visitas']} personas")
