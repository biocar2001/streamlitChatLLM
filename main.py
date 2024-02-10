import streamlit as st
import json
import os

# Configuración inicial de la página con Streamlit, estableciendo el título y el icono de la pestaña del navegador.
st.set_page_config(page_title="Chat SWO Data Labs - LLMs", page_icon="💬🦙")

class ChatHistorial:
    # Constructor de la clase, inicializa el archivo de historial y carga el historial existente.
    def __init__(self, archivo='historial_chat.json'):
        self.archivo = archivo
        self.historial = self.cargar_historial()

    # Carga el historial de chat desde un archivo JSON, si existe; de lo contrario, inicia una lista vacía.
    def cargar_historial(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as archivo:
                return json.load(archivo)
        return []

    # Guarda el historial de chat actual en el archivo JSON.
    def guardar_historial(self):
        with open(self.archivo, "w") as archivo:
            json.dump(self.historial, archivo)

    # Agrega un mensaje al historial y luego guarda el cambio.
    def agregar_mensaje(self, autor, mensaje):
        self.historial.append({"autor": autor, "mensaje": mensaje})
        self.guardar_historial()

    # Limpia el historial de chat completo y guarda el archivo JSON como una lista vacía.
    def limpiar_historial(self):
        self.historial = []
        self.guardar_historial()

def obtener_respuesta(pregunta):
    # Simulación de una función que obtiene respuestas, Aqui cada Equipo llamara a su LLM, el cual si ha sido desarrollado con patrones SOLID deberia ser muy facil ;-).
    return "Esto es una respuesta simulada. Integra aquí tu lógica."

def main():
    st.title('💬🦙 SWO Labs - Chat LLMS')

    chat_historial = ChatHistorial()

    # Generación de la lista de preguntas para el selectbox en el sidebar, filtrando solo las entradas de "Tú".
    preguntas = [item["mensaje"] for item in chat_historial.historial if item["autor"] == "Tú"]
    pregunta_seleccionada = st.sidebar.selectbox("Selecciona una pregunta para ver su respuesta:", preguntas, key="preguntas_select")

    # Mostrar la pregunta y respuesta seleccionada en el área principal.
    if pregunta_seleccionada:
        indice_pregunta = preguntas.index(pregunta_seleccionada) * 2
        pregunta = chat_historial.historial[indice_pregunta]["mensaje"]
        if indice_pregunta + 1 < len(chat_historial.historial):
            respuesta = chat_historial.historial[indice_pregunta + 1]["mensaje"]
            st.markdown(f"**Pregunta:** {pregunta}", unsafe_allow_html=True)
            st.markdown(f"**Respuesta:** {respuesta}", unsafe_allow_html=True)

    # Campo de entrada para nuevas preguntas.
    pregunta_usuario = st.text_input("Hazme una pregunta:", key="pregunta", value="")

    # Botón de enviar que procesa la nueva pregunta, obtiene una respuesta, y las muestra.
    if st.button('Enviar') and pregunta_usuario:
        chat_historial.agregar_mensaje("Tú", pregunta_usuario)
        respuesta = obtener_respuesta(pregunta_usuario)
        chat_historial.agregar_mensaje("ChatGPT", respuesta)
        st.markdown(f"**Respuesta:** {respuesta}", unsafe_allow_html=True)

    # Botón para limpiar el historial, que borra tanto el historial visual como el archivo.
    if st.sidebar.button('Limpiar Historial'):
        chat_historial.limpiar_historial()
        st.experimental_rerun()  # Refresca la aplicación para reflejar el historial limpio.

if __name__ == "__main__":
    main()
