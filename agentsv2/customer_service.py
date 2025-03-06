from agentsv2.base import BaseAgent


class ConversationalAgent(BaseAgent):
    def __init__(self, llm, company_info):
        system_prompt = f"""
Eres un asistente virtual de atención al cliente de la empresa {company_info['enterprise']}. Tu tarea es ayudar con información relevante y precisa sobre los servicios y productos de la empresa. 
    {company_info['description']}
    Siempre debes responder de manera clara y profesional, sin intentar entablar una conversación innecesaria. Responde directamente a las consultas que se te hagan, y proporciona la información más útil posible. 
"""
        output_format = """
Respuesta: [Tu respuesta aquí]
"""
        super().__init__(llm, system_prompt, output_format, ["chat_history", "user_input", "system"])