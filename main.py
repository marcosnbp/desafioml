import requests
import json
import boto3

def buscar_dados(event, context):
    
    api_request = requests.get("https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios/")
    cliente = json.loads(api_request.content)
    nome_s3 = "desafio-ml-bucket"
    contador: int
    contador = 0
    while contador <= int(cliente[contador]['id']):
        caminho_arq_local = "/tmp/Cliente"+str(cliente[contador]['id'])+".txt"
        arq_s3= "Dados_cliente/Cliente"+str(cliente[contador]['id'])+".txt"
        with open(caminho_arq_local, 'w') as arquivo:
            print("id: "+cliente[contador]['id'], file=arquivo)
            print("fec_alta: "+cliente[contador]['fec_alta'], file=arquivo)
            print("user_name: "+cliente[contador]['user_name'], file=arquivo)
            print("codigo_zip: "+cliente[contador]['codigo_zip'], file=arquivo)
            print("credit_card_num: "+cliente[contador]['credit_card_num'], file=arquivo)
            print("credit_card_ccv: "+cliente[contador]['credit_card_ccv'], file=arquivo)
            print("cuenta_numero: "+cliente[contador]['cuenta_numero'], file=arquivo)
            print("direccion: "+cliente[contador]['direccion'], file=arquivo)
            print("geo_latitud: "+cliente[contador]['geo_latitud'], file=arquivo)
            print("geo_longitud: "+cliente[contador]['geo_longitud'], file=arquivo)
            print("color_favorito: "+cliente[contador]['color_favorito'], file=arquivo)
            print("foto_dni: "+cliente[contador]['foto_dni'], file=arquivo)
            print("ip: "+cliente[contador]['ip'], file=arquivo)
            print("auto: "+cliente[contador]['auto'], file=arquivo)
            print("auto_modelo: "+cliente[contador]['auto_modelo'], file=arquivo)
            print("auto_tipo: "+cliente[contador]['auto_tipo'], file=arquivo)
            print("auto_color: "+cliente[contador]['auto_color'], file=arquivo)
            print("cantidad_compras_realizadas: "+str(cliente[contador]['cantidad_compras_realizadas']), file=arquivo)
            print("avatar: "+cliente[contador]['avatar'], file=arquivo)
            print("fec_birthday: "+cliente[contador]['fec_birthday'], file=arquivo)
            arquivo.close()
        s3 = boto3.client('s3')
        with open(caminho_arq_local, "rb") as f:
            s3.upload_fileobj(f, nome_s3, arq_s3)
        contador += 1
    else:
        print("fim")
