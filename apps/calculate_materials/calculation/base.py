import openai
import os
import json
import re
import environ
from .radier import calculation_radier
from .ceramic import ceramic_floor

env = environ.Env()
environ.Env.read_env()

ENVIROMENT = env

api_key = os.getenv('OPENAI_API_KEY')

openai.api_key = api_key
#:\n\n\"{text_user}\"
def date_extract(promp_main,text_user):
    prompt = promp_main
    
    try:
        response = openai.chat.completions.create(model="gpt-4o-mini",
                                                  temperature=0,
                                                  messages=[
                                                      {"role": "system", "content": prompt},
                                                      {
                                                          "role": "user",
                                                          "content": text_user
                                                      }
                                                  ])
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error al llamar a la API de OpenAI: {e}")
        return None


def extract_json(content):

    try:
        json_block = re.search(r"```json\s*(\{.*?\})\s*```", content, re.DOTALL)
        if json_block:
            json_str = json_block.group(1)
            return json.loads(json_str)
        else:
            print("Nose encontro un bloque JSON en la respuesta.")
            print("Contenido devuelto:", content) 
            return None
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")
        return None


def calculate_promp_input(promp_main,text_user_prompt,slug):
    #text_user_prompt = input('Ingrese prompt: ')
    promp_ai = promp_main

    date_proyect_content = date_extract(promp_ai,text_user_prompt )

    if not date_proyect_content:
        return {"error": "No se pudo obtener respuesta de la API"}

    print("Contenido de la respuesta de la API: ")
    print(date_proyect_content)

    dates_json = extract_json(date_proyect_content)
    if not dates_json:
        return {"error": "El JSON extraído no es válido."}

    print("\nJSON extraido: ")
    #print(json.dumps(dates_json, indent=2, ensure_ascii=False))
    print(type(dates_json))

    try:
        if slug == "radier":
            return_response = calculation_radier(dates_json)
            return return_response
        elif slug == "ceramica":
            return_response = ceramic_floor(dates_json)
            return return_response

    except KeyError as e:
        return f"Clave no encontrada en el JSON: {e}"