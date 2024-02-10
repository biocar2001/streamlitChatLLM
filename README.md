# Chat SWO con Streamlit

Este proyecto implementa una aplicación de chat simple pero interactiva utilizando Streamlit, permitiendo a los usuarios hacer preguntas y recibir respuestas simuladas. La aplicación mantiene un historial de la interacción que se puede revisar y gestionar. Fue diseñado siguiendo principios de código limpio y está estructurado para facilitar su expansión o integración con sistemas de respuestas más complejos.

## Características

- **Interfaz de Usuario Simple:** Utiliza Streamlit para una UI clara y amigable.
- **Historial de Chat:** Mantiene un registro de preguntas y respuestas que se pueden revisar.
- **Interacción Dinámica:** Permite a los usuarios seleccionar preguntas previas del historial para ver sus respuestas en el área principal.
- **Personalización y Mejora Facilitada:** Código estructurado pensando en la expansión y la integración con APIs de inteligencia artificial o bases de datos.

## Requisitos Previos

Para ejecutar esta aplicación, necesitarás:

- Python 3.6 o superior
- [Streamlit](https://streamlit.io) - Streamlit convierte los scripts de Python en aplicaciones web compartibles.

## Instalación y Ejecución

1. **Clona el repositorio:**
```bash
git clone https://github.com/biocar2001/streamlitChatLLM.git
cd streamlitChatLLM
```

2. **Instala las dependencias:**
```bash
pip install streamlit
```

3. **Ejecuta la aplicación:**
```bash
streamlit run app.py
```

Esto abrirá automáticamente la aplicación en tu navegador por defecto.

## Posibles Mejoras

- **Desarrollo de Test Unitarios:** Para garantizar la estabilidad y fiabilidad del código, se pueden desarrollar tests unitarios utilizando frameworks como unittest o pytest.

- **Contenerización con Docker:** Para facilitar el despliegue y garantizar la consistencia del entorno de ejecución, se puede contenerizar la aplicación utilizando Docker.

- **Despliegue en la Nube:** Para hacer la aplicación accesible globalmente, se puede desplegar en plataformas como AWS, GCP, o Heroku. Esto podría incluir la configuración de un CI/CD para automatizar el despliegue.

- **Integración con APIs de IA:** Para mejorar las respuestas del chat, se puede integrar con APIs de inteligencia artificial como OpenAI GPT o similares, permitiendo respuestas más ricas y contextuales.

- **Mejoras en la UI:** Aunque Streamlit ofrece una manera rápida de crear interfaces, se podrían explorar mejoras específicas en la UI para mejorar la experiencia del usuario, como temas personalizados o interacciones más ricas.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas para mejorar la aplicación o quieres reportar bugs, por favor, abre un issue o envía un pull request.

## Licencia

Este proyecto  no esta licenciado y es para uso libre por quien lo considere interesante.