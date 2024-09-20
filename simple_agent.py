from langchain_ollama import ChatOllama
from langchain_community.tools import YouTubeSearchTool, DuckDuckGoSearchResults

from langchain_core.messages import SystemMessage

from langgraph.prebuilt import create_react_agent

question_user = input("Dime sobre que lenguaje o tecnologia te gustaria aprender \n")

system_prompt = SystemMessage('''
Eres un asistente llamado Pedro que sirve para que los desarrollladores puedan crear rutas de aprendizaje sobre el lenguaje o técnologia de su preferencia. 

Siempre debes iniciar presentandote al usuario.

Tu tarea es explicar los temas que el usuario solicita complementando con links relacioados con cursos(gratuitos) o ejercicios que puendan servir a través de dos medios: texto y links a videos de youtube.

Complementa el tema solicitado con articulos que encuentres en la web. No inventes nada y trae contenido en español.

Se detallado con la distribución de los temas que se debe seguir en la ruta, siguiendo la estructura:

1. Titulo de la ruta de aprendizaje
2. Descripción de la ruta de aprendizaje
3. Explicación de los temas de la ruta los cuales deben estar detallando los temas y distribuyendolos en semanas o meses.
4. Links de los cursos o articulos(Deben ser links reales sino no los pongas)
5. Proporciona ejercicios que puedan poner en práctica
6. Siempre finaliza sugiriendo que proyectos se pueden realizar para poner en práctica los conocimientos adquiridos.

Usa las herramientas disponibles para hacer la busqueda. No inventes nada.
                              
Debes despedirte del usuario.

''')


#Herramientas
youtube = YouTubeSearchTool(
   description="Una herramienta de busqueda videos de youtube. Entrega links de videos en Español sobre el tema solicitado por el usuario y actualizados. Ten en cuenta traer cursos, rutas de aprendizaje relacionadas y proyectos"
)

duck_search = DuckDuckGoSearchResults(description="Una herramienta para busqueda de información de apyo usando el buscador duckduckgo, agrega siempre 5 cursos, proyectos o ejercicios relacionados con la solicitud de la ruta de aprendizaje que desea el usuario Para complementar el resultado. Entrega busquedas en Español. No olvides buscar siempre la información más actualizada. Valida que los links esten funcionando.")

tools = [youtube, duck_search]

#modelo
llm = ChatOllama(model="llama3.1").bind_tools(tools)

#Agente
agent = create_react_agent(llm, tools, state_modifier=system_prompt, debug=True)


#Invocamos el agente
result = agent.invoke({"messages": question_user})

print(result["messages"][-1].content)