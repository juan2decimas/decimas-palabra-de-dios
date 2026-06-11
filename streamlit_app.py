import streamlit as st
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="EL TALLER DE DECIMAS DE CUECANTO", page_icon="📝", layout="centered")

# ==========================================
# PARTE 1: TITULO PRINCIPAL Y FORMATO
# ==========================================
st.title("📝 EL TALLER DE DECIMAS DE CUECANTO")
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
# REFORMADO - PARTE 2: EL REVISOR DE 10 LÍNEAS
# ==========================================
st.subheader("📐 Revisor Métrico de la Décima Completa")
st.write("Pegue o escriba su décima de 10 líneas abajo. El sistema medirá cada renglón por separado:")

# Cuadro grande para meter las 10 líneas juntas
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

# Separamos el texto por líneas para revisarlas una a una
lineas = decima_a_medir.split('\n')

st.markdown("### 📊 Reporte del Calce (Línea por Línea):")

# Revisamos un máximo de 10 líneas para mantener el orden de la décima
for i, linea in enumerate(lineas[:10]):
    if linea.strip(): # Si la línea no está vacía
        cant_silabas = contar_silabas_basico(linea)
        if cant_silabas == 8:
            st.markdown(f"✅ **Línea {i+1}:** `{linea}` — **{cant_silabas} sílabas** (¡De ley!)")
        else:
            st.markdown(f"⚠️ **Línea {i+1}:** `{linea}` — **{cant_silabas} sílabas** (Revisar calce)")

if len(lineas) > 10:
    st.caption("💡 *Nota: Una décima de ley tiene solo 10 líneas. Ha escrito más renglones de la cuenta.*")
else:
    st.caption("💡 *Recuerde: El contador hace una medición matemática básica. Al cantar, considere las sinalefas (unión de vocales) para el octosílabo definitivo.*")

st.write("---")

# ==========================================
# PARTE 3: SECCIÓN DE ESTUDIO E HISTORIA
# ==========================================
st.header("🎓 Rincón del Estudio: El Origen de la Décima")

with st.expander("📖 Pinche aquí para leer la historia y estructura de la décima"):
    st.markdown("""
    ### El Nacimiento de la Espinela
    La décima que utilizamos hoy en día nació en **España en el año 1591**. Fue fijada por el poeta, músico y sacerdote **Vicente Espinel**. Por esta razón, a la décima de diez versos octosílabos se le conoce formalmente en todo el mundo hispanohablante como **Décima Espinela**.
    
    A través de los siglos, esta estructura viajó en los barcos y echó raíces profundas en el alma de América Latina, convirtiéndose en Chile en la llave maestra del **Canto a lo Poeta** (tanto a lo Divino como a lo Humano) y de nuestras queridas cuecas astutas.
    
    ### La Regla de Oro: La Estructura ABBAACCDDC
    Para que una décima esté correctamente construida y tenga rima consonante perfecta, los 10 versos deben rimar siguiendo este plano exacto de carpintería:
    
    * **Verso 1 (A)** rima con el **Verso 4** y el **Verso 5**.
    * **Verso 2 (B)** rima únicamente con el **Verso 3**.
    * **Verso 6 (C)** rima con el **Verso 7** y el **Verso 10**.
    * **Verso 8 (D)** rima únicamente con el **Verso 9**.
    
    *¡Cada línea debe tener exactamente 8 sílabas métricas para mantener la música y el galope del verso chileno!*
    """)

st.write("---")

# ==========================================
# PARTE 4: LA BIBLIOTECA DE DÉCIMAS (REVISADAS)
# ==========================================
st.header("📚 Biblioteca Virtual de Décimas")
st.write("Seleccione un estante para leer los versos sagrados:")

pestana1, pestana2, pestana3 = st.tabs(["🌱 La Creación", "📜 Los Mandamientos", "🕊️ Espíritu Santo"])

with pestana1:
    st.subheader("Décimas de la Creación")
    st.markdown("""
    Al principio oscuridad, (A)  
    sin forma, y desierto, (B)  
    el espíritu despierto (B)  
    de Dios, y su gran majestad, (A)  
    trajo la luz de la verdad. (A)  
    Separó las aguas del cielo, (C)  
    las semillas en  suelo, (C)  
    creó estrellas y el sol, (D)  
    y con su divino crisol (D)  
    le dio vida a mi suelo. (C)
    """)
    st.caption("— Compuesto por Cuecanto")

with pestana2:
    st.subheader("Décimas de la Ley Antigua")
    st.markdown("""
    Y en el monte temblando, (A)  
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
    st.caption("— Compuesto por Cuecanto")

with pestana3:
    st.subheader("Décimas de Pentecostés")
    st.markdown("""
    Como viento huracanado (A)  
    el don divino descendió, (B)  
    el taller se iluminó (B)  
    con el fuego consagrado. (A)  
    El temor ha terminado, (A)  
    hablando lenguas sin cesar, (C)  
    la palabra hay que llevar (C)  
    con valentía y con fe, (D)  
    alza tu voz, ponte en pie, (D)  
    y vamos todos a cantar. (C)
    """)
    st.caption("— Compuesto por Cuecanto")

st.write("---")

# ==========================================
# PARTE 5: CALENDARIO Y CONTADOR DE VISITAS
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
