from agentsv2.base import BaseAgent


class UserAgent(BaseAgent):
    def __init__(self, llm, user_profile):
        system_prompt = f"""
Eres un usuario de {user_profile['edad']} años, con ocupación de {user_profile['ocupacion']}, y estás en medio de una llamada con un asesor porque necesitas resolver el siguiente requerimiento: {user_profile['requerimiento']}.

Durante la conversación, responde siempre en función de lo que te diga el asesor, proporcionando solo la información necesaria para resolver tu requerimiento. Evita ofrecer detalles que no hayan sido solicitados. Cuando ya no necesites más ayuda, di explícitamente las palabras "terminar llamada" para finalizar la conversación.
"""
        output_format = """
Respuesta: [Tu respuesta aquí]
"""
        super().__init__(llm, system_prompt, output_format, ["chat_history", "agent_response", "system"])

    def interact(self, agent_response):
        return super().interact(agent_response)