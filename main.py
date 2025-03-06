import random
import json
from langchain.chat_models import ChatOpenAI

from agentsv2.business_evaluator import BusinessEvaluator, ConversationalAgent
from agentsv2.usability_evaluator import UsabilityEvaluator
from agentsv2.user import UserAgent

def main():
    llm = ChatOpenAI(temperature=0.7, model="gpt-4o-mini")
    company_info = {
        'enterprise': 'TechWorld',
        'description': 'TechWorld es una tienda especializada en la venta de productos electrónicos y tecnología avanzada, incluyendo computadoras, teléfonos móviles, accesorios y gadgets innovadores.'
    }

    asistente = ConversationalAgent(llm, company_info)

    user_profile = {
        'edad': 34,
        'ocupacion': 'Gerente de TI',
        'requerimiento': 'Consulta sobre disponibilidad de laptops para empresas'
    }

    user_agent = UserAgent(llm, user_profile)

    message = "hola"
    max_interactions = random.randint(6, 9)
    while True:
        asistant_response = asistente.interact(message)
        print(asistant_response)
        user_response = user_agent.interact(asistant_response)
        print(user_response)
        message = user_response
        if 'terminar llamada' in message.lower():
            break

        if len(asistente.chat_history) >= max_interactions:
            break

    historial = asistente.chat_history
    print("historial", historial)
    transcript = "\n".join([f"Usuario: {entry['user']}\nAsistente: {entry['agent']}" for entry in historial])

    evaluador = UsabilityEvaluator(llm)
    resultado_usabilidad = evaluador.evaluar(transcript)
    print(resultado_usabilidad)
    busines_evaluator = BusinessEvaluator(llm)
    resultado_negocios = busines_evaluator.evaluar(transcript)
    print(resultado_negocios)

    try:
        resultado_usabilidad = json.loads(resultado_usabilidad)
        resultado_negocios = json.loads(resultado_negocios)
    except:
        resultado_usabilidad = resultado_usabilidad
        resultado_negocios = resultado_negocios
        print("Error al cargar los resultados de las métricas de usabilidad y negocios.")
    
    output_data = {
        "history": historial,
        "usability_metrics": resultado_usabilidad,
        "business_metrics": resultado_negocios
    }

    output_file = f"./runs/results_metrics{company_info['enterprise']}_{user_profile['requerimiento'].replace(' ','_')}.json"
    with open(output_file, "w") as json_file:
        json.dump(output_data, json_file, ensure_ascii=False, indent=4)

    print(f"Archivo JSON generado en: {output_file}")

if __name__ == "__main__":
    main()
