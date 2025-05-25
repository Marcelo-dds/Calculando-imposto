from dic import dicionario_vimeo
import pprint
informacoes = dicionario_vimeo["data"]
#imprimi de forma identada e alfabetica
#pprint.pprint(dicionario_vimeo)
videos = []
for item in informacoes:
    video_uri = item["uri"]
    nome = item["name"]
    duracao = item ["duration"]
    

    link_540p = ""
    link_720p = ""
    link_1080p = ""


    lista_download = item["download"]
    for dicionario_download in lista_download:
        if dicionario_download["rendition"] == "540p":
            link_540p = dicionario_download["link"]
        if dicionario_download["rendition"] == "720p":
            link_720p = dicionario_download["link"]
        if dicionario_download["rendition"] == "1080p":
            link_1080p = dicionario_download["link"]
    
    dic_item = {'uri': video_uri, 'nome': nome, 'duracao': duracao, 'link540p': link_540p, 'link720p': link_720p, 'link1080p': link_720p}
    videos.append(dic_item)
pprint.pprint(videos)

