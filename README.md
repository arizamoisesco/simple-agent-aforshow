# Asistente de Rutas de Aprendizaje para Desarrolladores

Este repositorio contiene un asistente llamado **Pedro** que permite a los desarrolladores generar rutas de aprendizaje sobre lenguajes de programación o tecnologías. Utiliza un modelo de lenguaje y herramientas de búsqueda para ofrecer contenido relevante como videos de YouTube y artículos en la web. El asistente está diseñado para proporcionar una experiencia interactiva y útil en la creación de rutas de estudio personalizadas.

## Características

- **Búsqueda de contenido**: Utiliza herramientas de búsqueda para obtener videos de YouTube, artículos y ejercicios prácticos relacionados con el tema solicitado.
- **Organización de rutas de aprendizaje**: Proporciona una ruta estructurada en semanas o meses con enlaces a recursos y ejercicios.
- **Contenido en español**: Todos los recursos y contenido que proporciona el asistente están en español.

## Herramientas utilizadas

Este asistente hace uso de las siguientes herramientas de búsqueda:
- **YouTubeSearchTool**: Busca videos de YouTube actualizados en español sobre el tema solicitado.
- **DuckDuckGoSearchResults**: Realiza búsquedas en DuckDuckGo para obtener artículos, cursos, proyectos y ejercicios relacionados.

## Requisitos

Para ejecutar este proyecto, asegúrate de tener lo siguiente:
- Python 3.8 o superior
- Las siguientes dependencias de Python:
  - `langchain_ollama`
  - `langchain_community`
  - `langchain_core`
  - `langgraph`

Puedes instalar las dependencias utilizando `pip`:

```bash
pip install langchain langchain_community langgraph duckduckgo-search langchain_ollama youtube_search
