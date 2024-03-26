print ("CRINGE, LOL, ROFL, SHEESH, CREEPY, AGGRO, OMG, ASAP, YOLO")
mun_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            "OMG": "Cuando te sorprende",
            "ASAP": "Cuando quieres algo ya",
            "YOLO": "Solo tienes una oportunidad",
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in mun_dict.keys():
    print (mun_dict[word])

else:
   print ("Lo siento esa palabra no se encuentra en este diccionario")
