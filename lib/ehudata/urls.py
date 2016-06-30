from bs4 import BeautifulSoup
import requests
import json
import re

def __getUrlByHrefRegEx(url, regex):
    """
        Devuelve una url que tenga en el href lo que hay en el parametro regex
    """
    req = requests.get(url)
    statusCode = req.status_code
    if statusCode == 200:
        html = BeautifulSoup(req.text, "html.parser")
        aTag = html.find('a', href = re.compile(regex))
        return "http://www.ehu.eus" + aTag['href']
    else:
        print("Status Code %d" %statusCode)

def __getGradoUrl(campus, plan):
    """
    Devuelve la url principal del grado
    """
    ehuUrl = "http://www.ehu.eus/es/web/vicer.grado-innovacion/aurtengo-graduak-campus-ikastegia?p_p_id=upvehuapp_WAR_upvehuappportlet&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=0&p_p_col_count=1&p_p_lifecycle=1&_upvehuapp_WAR_upvehuappportlet_action=redirectAction&reu=/pls/entrada/plew0040.htm?p_sesion=&p_cod_idioma=CAS&p_en_portal=N&p_titu_nuevas=S&p_opcion=2&p_anyoAcad=act&p_campus=1&p_rama=&p_ciclo="

    if campus == 'BI':
        campusVal = 3
    elif campus == "AR":
        campusVal = 1
    else:
        campusVal = 2 #Por defecto, el gipuzkoano
    nuevoTab = "p_campus=" + str(campusVal)
    ehuUrl = ehuUrl.replace("p_campus=1", nuevoTab)
    plan = "p_cod_plan=" + plan

    return __getUrlByHrefRegEx(ehuUrl, plan)


def __getUrlAsig(campus, codGrado, codAsig, idioma):
    ehuUrl = __getGradoUrl(campus, codGrado)
    ehuUrl = ehuUrl.replace("p_menu=intro", "p_menu=asig_cursos")
    ehuUrl = ehuUrl + "&p_pestanya=3"
    req = requests.get(ehuUrl)
    statusCode = req.status_code
    return __getUrlByHrefRegEx(ehuUrl, codAsig)
