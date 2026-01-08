import os 
import shutil
from datetime import datetime
caminho_de_origem = "C:/Users/Valley/Pictures/pin work"
arquivos = os.listdir(caminho_de_origem)
print(f'iniciando a organização de {len(arquivos)} arquivos...')
for arquivo in arquivos:
    caminho_completo = os.path.join(caminho_de_origem, arquivo)
    if os.path.isdir(caminho_completo):
        continue
    try:
        tempo = os.path.getmtime(caminho_completo)
        datetime_obj = datetime.fromtimestamp(tempo)
        ano = datetime_obj.strftime("%Y")
        mes = datetime_obj.strftime("%m - %B")
        pasta_destino = os.path.join(caminho_de_origem, ano, mes)
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)
        shutil.move(caminho_completo, os.path.join(pasta_destino, arquivo))
        print(f"sucesso: {arquivo} movido para {mes}!")
    except Exception as e:
        print(f"Erro ao processar {arquivo}: {e}")
