import streamlit as st
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="EL TALLER DE DECIMAS DE CUECANTO", page_icon="📝", layout="centered")

# =========================================================================
# MAESTRÍA EN CSS: Barniz de Madera Rústica e Importación de Fuentes a Mano
# =========================================================================
st.markdown(
    """
    <style>
    /* Importamos las tipografías estilo manuscrito, incluyendo Tangerine */
    @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Permanent+Marker&family=Sacramento&family=Tangerine:wght@700&display=swap');

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
        background-color: rgba(253, 246, 227, 0.6); 
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
        width: 100%; 
    }
    
    div.stButton > button:hover {
        background-color: rgba(92, 58, 33, 0.9) !important;
        color: #ffffff !important;
        transform: scale(1.02);
    }

    /* Integración de las pestañas principales de la página */
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
# MECANISMO INTERRUPTOR (ENCENDIDO / APAGADO)
# ==========================================
if 'estado_guitarron' not in st.session_state:
    st.session_state['estado_guitarron'] = False  

# TITULO PRINCIPAL DE LA APLICACIÓN
st.title("📝 EL TALLER DE DECIMAS DE CUECANTO")
st.write("---")

# =========================================================================
# CREACIÓN DE LAS PESTAÑAS PRINCIPALES DEL TALLER (Aquí unificamos todo)
# =========================================================================
pestana_taller, pestana_biblioteca, pestana_cronicas = st.tabs([
    "🎸 El Taller de Escritura", 
    "📚 Biblioteca de Décimas", 
    "📜 Crónicas y Geografía de la Décima"
])

# =========================================================================
# PESTAÑA 1: EL TALLER DE ESCRITURA (Guitarrón, Letras y Revisor)
# =========================================================================
with pestana_taller:
    st.subheader("El Guitarrón del Taller")
    st.write("Pinche directamente el interruptor musical de abajo para controlar la entonación:")

    url_imagen_guitarron = "https://images.unsplash.com/photo-1510915361894-db8b60106cb1?q=80&w=600&auto=format&fit=crop"
    st.image(url_imagen_guitarron, caption="Guitarrón de ley - 25 cuerdas para el Canto a lo Divino", width=350)

    texto_boton = "🛑 APAGAR MÚSICA DEL GUITARRÓN" if st.session_state['estado_guitarron'] else "🎵 AFINAR Y ENCENDER ESTE GUITARRÓN"

    if st.button(texto_boton, key="boton_guitarron"):
        st.session_state['estado_guitarron'] = not st.session_state['estado_guitarron']
        st.rerun()

    if st.session_state['estado_guitarron']:
        st.markdown("""
        <div style='background-color: rgba(230, 245, 230, 0.9); padding: 15px; border-radius: 10px; border-left: 5px solid #2e7d32; color: #1b5e20;'>
            <h4>✨ ¡Guitarrón Sonando en la Variable! ✨</h4>
            <p><i>"Suenen las veinticinco cuerdas con fuerza, de norte a sur, 
            iluminando el libreto con la divina luz del Salvador."</i></p>
            <p style='font-size: 13px; color: #2e7d32; margin-top: 5px;'>🎶 Escuchando de fondo: Entonación del Zurdo Ortega (Anticueca Banda)</p>
        </div>
        """, unsafe_allow_html=True)
        
        html_audio_invisible = """
        <iframe width="0" height="0" src="https://www.youtube.com/embed/9xr1KDOpReA?autoplay=1&start=20" 
        frameborder="0" allow="autoplay; encrypted-media" style="display:none;"></iframe>
        """
        st.markdown(html_audio_invisible, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.7); padding: 15px; border-radius: 10px; border-left: 5px solid #5c3a21; color: #4a2c16;'>
            <p style='margin: 0; font-style: italic;'>El guitarrón descansa colgado en la viga. Presione el botón de arriba para templar el verso.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")
    st.subheader("Herramientas de Escritura")

    col1, col2, col3 = st.columns(3)
    with col1:
        estilo_letra = st.selectbox(
            "Estilo de letra", 
            ["Normal", "Elegante (Serif)", "Moderna (Sans)", "Cancillería Italiana (Tangerine)", "Manuscrito Natural (Caveat)", "Pluma Elegante (Sacramento)", "Marcador Rústico"]
        )
    with col2:
        tamano_letra = st.slider("Tamaño de la letra", min_value=14, max_value=50, value=24) 
    with col3:
        formato_negrita = st.checkbox("Texto en Negrita (**B**)")

    texto_usuario = st.text_area("Escriba o pegue sus décimas aquí:", value="Escriba aquí sus versos de fe...", height=150)

    estilo_css = f"font-size: {tamano_letra}px; color: #1a1a1a; "
    if estilo_letra == "Elegante (Serif)":
        estilo_css += "font-family: serif; "
    elif estilo_letra == "Moderna (Sans)":
        estilo_css += "font-family: sans-serif; "
    elif estilo_letra == "Cancillería Italiana (Tangerine)":
        estilo_css += "font-family: 'Tangerine', cursive; font-size: {0}px; line-height: 1.1; ".format(tamano_letra + 12)
    elif estilo_letra == "Manuscrito Natural (Caveat)":
        estilo_css += "font-family: 'Caveat', cursive; "
    elif estilo_letra == "Pluma Elegante (Sacramento)":
        estilo_css += "font-family: 'Sacramento', cursive; font-size: {0}px; ".format(tamano_letra + 6)
    elif estilo_letra == "Marcador Rústico":
        estilo_css += "font-family: 'Permanent Marker', cursive; "

    if formato_negrita:
        estilo_css += "font-weight: bold; "

    st.markdown("### 👁️ Vista Previa de su Verso:")
    st.markdown(f'<p style="{estilo_css}">{texto_usuario.replace("\n", "<br>")}</p>', unsafe_allow_html=True)

    st.write("---")
    st.subheader("📐 Revisor Métrico de la Décima Completa")
    st.write("Pegue o escriba su décima de 10 líneas abajo. El sistema medirá cada renglón por separado:")

    decima_a_medir = st.text_area(
        "Escriba aquí sus 10 versos para medir:", 
        value="Al principio todo era oscuridad,\nsin forma, vacío y desierto,\npero el espíritu despierto\nde Dios, con su gran majestad,\ntrajo la luz de la verdad.",
        height=220,
        key="revisor_textarea"
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


# =========================================================================
# PESTAÑA 2: LA BIBLIOTECA DE DÉCIMAS (Tus estantes de versos)
# =========================================================================
with pestana_biblioteca:
    st.header("📚 Biblioteca Virtual de Décimas")
    st.write("Seleccione un estante para leer los versos sagrados:")

    sub_pestana1, sub_pestana2, sub_pestana3 = st.tabs(["🌱 La Creación", "📜 Los Mandamientos", "🕊️ Espíritu Santo"])
    estilo_texto_biblioteca = "color: #2b1d0c; font-style: italic; font-size: 20px;"

    with sub_pestana1:
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

    with sub_pestana2:
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

    with sub_pestana3:
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


# =========================================================================
# PESTAÑA 3: CRÓNICAS Y GEOGRAFÍA DE LA DÉCIMA (El nuevo contenido histórico)
# =========================================================================
with pestana_cronicas:
    st.header("📜 Crónicas y Geografía de la Décima")
    st.markdown(
        "Bienvenido a la sección histórica del taller. Aquí revisamos las raíces, "
        "el mapa de nuestra América Morena y los nombres de quienes han tallado la identidad de nuestro verso."
    )
    st.write("---")

    # SECCIÓN 1: El Altar Mayor de la Paya Chilena
    st.subheader("⚔️ El Altar Mayor de la Paya Chilena (1830)")
    st.markdown(
        "En el año 1830, en San Vicente de Tagua Tagua, se llevó a cabo el duelo poético más grande "
        "de la historia de Chile. Durante **80 horas seguidas** (tres días y tres noches), se enfrentaron "
        "dos mundos a través de la décima ruda y perfecta:"
    )
    
    col_taguada, col_rosa = st.columns(2)
    with col_taguada:
        st.markdown(
            "**🤠 El Mulato Taguada (El ingenio de la tierra):** Peón de campo, mestizo y analfabeto, pero tocado por la gracia "
            "divina de una rapidez mental y agudeza poética sobrehumana. Representaba la sabiduría del suelo."
        )
    with col_rosa:
        st.markdown(
            "**🎩 Don Javier de la Rosa (El caballero de alcurnia):** Terrateniente ilustrado, de familia acaudalada de la zona central, "
            "educado y de mente matemática. Representaba la décima culta y el saber de los libros."
        )

    st.markdown("\n**El Intercambio Legendario:**")
    st.info(
        "**Don Javier de la Rosa intentó arrinconarlo cantando:**\n\n"
        "*“Dime, mulato insolente,*\n"
        "*¿quién te ha dado la osadía*\n"
        "*de venir a esta hidalguía*\n"
        "*a cantar tan torpemente?...”*\n\n"
        "**A lo que el Mulato Taguada, firme en el mesón, respondió:**\n\n"
        "*“No me asusta su hidalguía,*\n"
        "*don Javier, con tanto brillo,*\n"
        "*que el oro ante el baratillo*\n"
        "*pierde toda su valía.*\n"
        "*Dios le dio la ciencia a usté*\n"
        "*en los libros que ha leío,*\n"
        "*pero a mí, que soy nacío*\n"
        "*bajo el cielo y en la fe,*\n"
        "*me dio el canto que ve usté*\n"
        "*pa' ganarle al más instruío.”*"
    )
    
    st.write("---")

    # SECCIÓN 2: Raíces Mundiales
    st.subheader("🌱 Raíces Mundiales y el Refugio Americano")
    st.markdown(
        "* **El Nacimiento (1591):** La estructura perfecta ($abbaaccddc$) fue fijada "
        "en España por el poeta, músico y sacerdote **Vicente Espinel**. El éxito fue tal que el mismísimo Lope de Vega bendijo su uso.\n"
        "* **El Refugio Americano:** Traída para la evangelización, la décima fue adoptada "
        "por el pueblo mestizo y campesino. Mientras en España perdió terreno, en América se transformó en la memoria "
        "oral de los pueblos, sobreviviendo por más de 400 años en la mente de poetas populares."
    )
    
    st.write("---")

    # SECCIÓN 3: El Mapa Continental
    st.subheader("🌎 El Mapa Continental de la Décima Viva")
    st.markdown("Así late la tradición viva y fuerte a lo largo de nuestra América Morena:")

    datos_mapa = [
        {"Región / País": "Chile", "Cultivo / Nombre": "El Canto a lo Poeta (Divino y Humano)", "Instrumento Rey": "Guitarrón Chileno (25 cuerdas) y Rabel", "Sello del Estilo": "Vigilias completas de respeto y fundamentos sagrados frente al altar."},
        {"Región / País": "Uruguay", "Cultivo / Nombre": "La Payada y Milonga Campera", "Instrumento Rey": "Guitarra Criolla (6 cuerdas)", "Sello del Estilo": "Canto pausado, reflexivo y filosófico de la pampa. Impulsado por Bartolomé Hidalgo."},
        {"Región / País": "Venezuela y Colombia", "Cultivo / Nombre": "El Galerón y cantos del llano", "Instrumento Rey": "Cuatro, Arpa y Maracas", "Sello del Estilo": "Canto recio del trópico para narrar faenas de a caballo y leyendas de la sabana."},
        {"Región / País": "Cuba", "Cultivo / Nombre": "El Punto Cubano (Patrimonio Mundial)", "Instrumento Rey": "Laúd Cubano y Tres", "Sello del Estilo": "Controversias guajiras, rápidas y de un virtuosismo métrico impresionante."},
        {"Región / País": "México", "Cultivo / Nombre": "Son Jarocho y Huasteca", "Instrumento Rey": "Jarana y Quinta Huapinguera", "Sello del Estilo": "Versos improvisados con alegría sobre la tarima de madera zapateada."},
        {"Región / País": "Puerto Rico", "Cultivo / Nombre": "Aguinaldo y los Seis", "Instrumento Rey": "Cuatro Puertorriqueño", "Sello del Estilo": "Muy ligado a las promesas cantadas a los Santos Reyes y navidades."},
        {"Región / País": "Panamá", "Cultivo / Nombre": "La Mejorana", "Instrumento Rey": "Guitarra Mejoranera", "Sello del Estilo": "El canto nacional que se bate con orgullo en los famosos 'galares' poéticos."}
    ]
    st.table(datos_mapa)
    
    st.write("---")

    # SECCIÓN 4: Cuadro de Honor Chileno
    st.subheader("🏛️ Cuadro de Honor del Verso Chileno")
    
    col_hist, col_vig = st.columns(2)
    with col_hist:
        st.markdown("**📜 Pilares Históricos**")
        st.markdown(
            "* **Rosa Araneda (1850–1894):** La gran reina de la Lira Popular decimonónica en Santiago.\n"
            "* **Bernardino Guajardo (1812–1886):** El poeta popular más masivo y célebre del siglo XIX.\n"
            "* **Roberto Parra (1921–1995):** El creador de las inmortales *Décimas de la Negra Ester*.\n"
            "* **Nicanor Parra (1914–2018):** El antipoeta que revolucionó todo basándose en la métrica campesina.\n"
            "* **Santos Rubio (1938–2011):** El maestro ciego de Pirque que rescató el guitarrón chileno."
        )
    with col_vig:
        st.markdown("**🔥 Guardianes Vigentes**")
        st.markdown(
            "* **Francisco 'Pancho' Astorga:** Gran maestro de Codegua y pilar de la enseñanza del verso.\n"
            "* **Familia Madariaga:** Tesoros Humanos Vivos que mantienen la tradición familiar pura en Casablanca.\n"
            "* **Manuel Sánchez:** Payador virtuoso que ha llevado el guitarrón a encontrarse con músicas del mundo.\n"
            "* **Myriam Arancibia:** Respetada cantora de Pirque, guardiana de las vigilias sagradas.\n"
            "* **La Nueva Hornada:** Jóvenes como Carola López, Rodrigo Núñez y Hugo Macaya que defienden la herencia."
        )

    st.write("---")

    # SECCIÓN 5: GRAN HOMENAJE FINAL
    st.subheader("🕯️ Homenaje a los Guardianes de la Tradición Campesina")
    st.success(
        "Este taller digital levanta su sombrero y rinde un profundo homenaje a todos los hombres y mujeres "
        "de Chile que hoy, en este mismo instante, defienden y cultivan la décima, el **Canto a lo Humano**, "
        "el **Canto a lo Divino** y cada expresión de la cultura campesina.\n\n"
        "A quienes viajan kilómetros por caminos de tierra para llegar a una vigilia; a los que templan las veinticinco "
        "cuerdas de un guitarrón en la penumbra de un altar; a los que siembran el octosílabo en las escuelas rurales y "
        "a los que improvisan con el ingenio despierto sobre el mesón de una cantina.\n\n"
        "Vaya este reconocimiento a los cultores anónimos, a las familias campesinas que guardan los cuadernos de versos "
        "como el tesoro más grande de su herencia, y a cada alma que se niega a dejar morir el canto con fundamento. "
        "Mientras un chileno siembre una décima en el viento, la raíz de nuestra patria seguirá viva y profunda. "
        "¡Salud por los poetas de la tierra!"
    )


# ==========================================
# PIE DE PÁGINA: CALENDARIO Y VISITAS
# ==========================================
st.write("---")
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
