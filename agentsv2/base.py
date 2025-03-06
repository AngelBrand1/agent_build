from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class BaseAgent:
    def __init__(self, llm, system_prompt, output_format, input_vars):
        self.llm = llm
        self.system_prompt = system_prompt
        self.output_format = output_format
        self.chat_history = []
        
        self.prompt_template = PromptTemplate(
            input_variables=input_vars,
            partial_variables={"format_instructions": self.output_format},
            template="Eres: {system}\n\nHistorial de la conversación:\n{chat_history}\nEntrada: {input_text}\nInstrucciones de formato:{format_instructions}"
        )
        
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template, verbose=True)
    
    def interact(self, input_text):
        chat_history_str = "\n".join([f"\tUsuario: {entry['user']}\n\tAgente: {entry['agent']}" for entry in self.chat_history])
        
        response = self.chain.invoke({
            "chat_history": chat_history_str,
            "input_text": input_text,
            "system": self.system_prompt
        })
        agent_response = response.get("text", "").split("Respuesta: ")[-1]
        
        self.chat_history.append({"user": input_text, "agent": agent_response})
        return agent_response
    
    def iniciar_conversacion(self):
        print("Iniciando conversación. Escribe 'salir' para terminar.")
        while True:
            user_input = input("Tú: ")
            if user_input.lower() == "salir":
                print("Saliendo...")
                break
            response = self.interact(user_input)
            print(f"Agente: {response}")