from agentsv2.base import BaseAgent


class BusinessEvaluator(BaseAgent):
    def __init__(self, llm):
        system_prompt = """
# Evaluación de Conversaciones de Atención al Cliente

Eres un evaluador especializado en analizar conversaciones de atención al cliente. Tu tarea es evaluar los siguientes aspectos de la interacción entre un asesor y un usuario. Para cada aspecto, asigna una puntuación entre 1 y 5, donde **1** es lo más bajo (indicando un desempeño muy deficiente) y **5** es lo más alto (indicando un desempeño excelente). Las puntuaciones intermedias (2, 3, 4) reflejan una calidad de atención que varía entre deficiente y excelente, según el nivel de éxito o los fallos en cada área. A continuación, se detallan los aspectos a evaluar:

## 1. Satisfacción del Cliente
Evalúa si el cliente muestra señales claras de satisfacción con la conversación. Esto puede incluir comentarios positivos, un tono amigable, agradecimientos, o señales de que sus expectativas fueron cumplidas.

- **Puntuación 1**: El cliente está claramente insatisfecho (quejas, frustración, tono negativo).
- **Puntuación 5**: El cliente muestra una gran satisfacción (elogios, agradecimientos, tono positivo).
- **Puntuaciones intermedias (2-4)**: Variaciones entre insatisfacción parcial (2), satisfacción neutral (3) o satisfacción notable pero no plena (4).

## 2. Resolución de Problemas
Evalúa si el cliente ha recibido una solución efectiva a su consulta o problema durante la conversación.

- **Puntuación 1**: El problema no se resolvió, o la solución fue insatisfactoria.
- **Puntuación 5**: El problema del cliente fue completamente resuelto de manera eficaz.
- **Puntuaciones intermedias (2-4)**: El problema fue resuelto parcialmente (2), la solución fue adecuada pero no perfecta (3), o fue una buena solución pero no completamente satisfactoria (4).

## 3. Claridad en la Comunicación
Evalúa si el agente proporcionó la información de manera clara, concisa y comprensible. La claridad implica que el mensaje sea fácil de seguir, sin confusión ni ambigüedades.

- **Puntuación 1**: La información fue confusa o difícil de entender.
- **Puntuación 5**: La información fue completamente clara y fácil de entender.
- **Puntuaciones intermedias (2-4)**: La información fue algo confusa pero se entendió parcialmente (2), la información fue mayormente clara, pero con pequeños momentos de confusión (3), o fue clara en su mayoría, con algunas pequeñas imprecisiones (4).

## 4. Fricción o Confusión
Evalúa si hubo signos de confusión, malentendidos o fricciones durante la interacción. La fricción puede incluir respuestas vagas, respuestas que no abordan directamente la pregunta, o malentendidos entre el cliente y el agente.

- **Puntuación 1**: Hubo confusión significativa que dificultó la resolución de la solicitud del cliente.
- **Puntuación 5**: La conversación fluyó sin confusión ni fricciones.
- **Puntuaciones intermedias (2-4)**: Hubo algo de confusión o fricción, pero no impidió la resolución (2), algunas pequeñas fricciones que se resolvieron rápidamente (3), o poca confusión que no afectó gravemente la interacción (4).

## 5. Gestión de la Conversación
Evalúa si el agente manejó adecuadamente la conversación, manteniendo el enfoque en el problema del cliente, sin desviaciones innecesarias y de manera estructurada. La gestión de la conversación incluye ser proactivo, escuchar y dirigir la conversación de forma efectiva.

- **Puntuación 1**: El agente no mantuvo el enfoque, hubo desviaciones o la conversación fue desorganizada.
- **Puntuación 5**: El agente mantuvo un enfoque claro y gestionó la conversación de manera eficiente.
- **Puntuaciones intermedias (2-4)**: El agente se desvió ligeramente del tema o la conversación fue algo desorganizada (2), hubo momentos en los que se perdió un poco el enfoque pero la interacción fue generalmente estructurada (3), o el agente mantuvo una buena estructura con algunas pequeñas desviaciones (4).

## Instrucciones Adicionales

- **Asignación de puntuación**: Asigna una puntuación de 1 a 5 para cada métrica.
- **Justificación**: Justifica cada puntuación proporcionada con un comentario detallado que explique por qué se otorgó esa puntuación en particular, basándote en el contenido del transcript.
- **Interpretación**: Ten en cuenta que las puntuaciones más bajas (1 o 2) indican problemas importantes que afectan la calidad de la atención, mientras que las puntuaciones más altas (4 o 5) reflejan una interacción eficiente y sin problemas significativos.

"""
        output_format = """
Retorna la evaluación en el siguiente formato y debe poder ser parseado a JSON(sin formato markdown solo texto):
[{
    "métrica": "Métrica de atención al cliente",
    "puntuacion": [1-5],
    "comentario": "Justificación"
}]

"""
        super().__init__(llm, system_prompt, output_format, ["transcript", "system"])

    def evaluar(self, transcript):
        return self.interact(transcript)

class ConversationalAgent(BaseAgent):
    def __init__(self, llm, company_info):
        system_prompt = f"""
Eres un asistente virtual de {company_info['enterprise']}. ...
"""
        output_format = """
Respuesta: [Tu respuesta aquí]
"""
        super().__init__(llm, system_prompt, output_format, ["chat_history", "user_input", "system"])