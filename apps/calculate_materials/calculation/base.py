import openai
import os
import json
import re
import environ

env = environ.Env()
environ.Env.read_env()

ENVIROMENT = env

api_key = os.getenv('OPENAI_API_KEY')

openai.api_key = api_key
#:\n\n\"{text_user}\"
def date_extract(text_user):
    prompt = f"""Extrae las dimensiones y detalles del siguiente proyecto de construcción y preséntalos en formato JSON:
    Instrucciones:
    -Identifica las medidas y transformalas siempre a metros.
    -Extrae los datos en largo, ancho, espesor.
    -Si el usuario espesifica como grueso o alto o algo similar a espesor, siempre dejarlo como espesor.
    -Identifica las distintas siglas de medidas que el usuario puede ingresar.
    """
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

    
def calculate_promp_input(text_user_prompt):
    #text_user_prompt = input('Ingrese prompt: ')

    date_proyect_content = date_extract(text_user_prompt)

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
        dimention = dates_json['dimensiones']
        large = dimention['largo']
        width = dimention['ancho']
        thickness = dimention['espesor']
        print()
        print()
        print(f"largo: {large}, ancho: {width}, espesor: {thickness}")
        print()
        #calculate
        volume = large * width * thickness
        bags_cement_m3 = 7
        m3_sand = 0.7
        m3_gravel = 0.7

        bag_cement = volume * bags_cement_m3
        cube_sand = volume * m3_sand
        cube_gravel = volume * m3_gravel

        return f"Necesitas aproximadamente {bag_cement:.2f} bolsas de cemento, {cube_sand:.2f} cubos de arena y {cube_gravel:.2f} cubos de grava"

    except KeyError as e:
        return f"Clave no encontrada en el JSON: {e}"