from typing import Final
from bs4 import BeautifulSoup as bs
import requests
import re

# TODO: Hacer manejar I/O

SITE_URL: Final[str] = "https://mover.uz/channel/UFCMan"

def getRequest(url: str) -> requests.Response:
    return requests.get(url)

def parseHtml(page_text: str) -> bs:
    return bs(page_text, "html.parser")

def playVideoMpv(video_url: str) -> None:
    eval(f"mpv {video_url}")

def searchVideoList(html: bs):
    return html.find("div",class_="video-list")


html = parseHtml(getRequest(SITE_URL).text )
#print(html)
result = searchVideoList(html)
#print(result)

# TODO: Hacer una funcion para cambiar un numero de pagina 
# TODO: Hacer el regex una funcion para que me sirva al momento de cambiar de nro de pag
video_links = re.findall(r'https://mover\.uz/watch/\w+',str(result))
print(video_links)
# playVideoMpv(video_links[0]) No sirve porque el link va a una pagina no a un archivo de video
# TODO: obtener el link del video de la pagina del video
