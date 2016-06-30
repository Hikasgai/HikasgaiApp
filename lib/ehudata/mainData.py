import urls
from bs4 import BeautifulSoup
import requests
import json
import re

def __getNombreAsig(html):
    contenido = html.find("div", {"id": "contenido_"})
    titulo = contenido.find("h1").getText()
    return titulo.split("-")[1]

def __getHorariosTabla(regex, html):
    teorico = []
    tabla = html.find(text=re.compile(regex)).findNext('table')
    semanas = tabla.select("tbody tr")
    for rango_semanas in semanas:
        obj_teorico = {}
        dias = []
        columnas = rango_semanas.find_all('td')
        i = 0
        for columna in columnas:
            if i == 0:
                obj_teorico["rango_semanas"] = columna.getText()
            elif columna.getText() != "--":
                horas = {}
                horas["dia"] = str(i)
                horas["horas"] = columna.getText()
                dias.append(horas)
            i = i+1
        obj_teorico["dias_semanas"] = dias
        teorico.append(obj_teorico)
    return teorico

def __getHorarioTeorico(data, html):
    """
        Funcion para obtener el horario de las clases teoricas de una asignatura
    """
    regex = "Grupos:." + data["grupo"] + ".T"
    return __getHorariosTabla(regex, html)

def __getHorarioPractico(data, html):
    """
        Funcion para obtener el horario de las clases practicas de una asignatura
    """
    regex = "Grupos:." + data["grupo"] + ".P"
    return __getHorariosTabla(regex, html)


#campus, codigoGrado, codigoAsig, idioma, grupo
def getHorarioAsignatura(data):

    urlAsignatura = urls.__getUrlAsig(data["campus"], data["codigoGrado"], data["codigoAsig"], data["idioma"])

    horario = {}
    req = requests.get(urlAsignatura)
    statusCode = req.status_code
    if statusCode == 200:
        html = BeautifulSoup(req.text, "html.parser")
        horario["nombre"] = __getNombreAsig(html)
        horario["teorico"] = __getHorarioTeorico(data, html)
        horario["practico"] = __getHorarioPractico(data, html)

        return horario
        #print(json.dumps(horario, indent=4, sort_keys=True))
    else:
        print("Status Code %d" %statusCode)


def getInicioCuatrimestre():
    return None

def getDiasSemanas():
    """
        Esto deberia hacerse automatico pero no se de donde sacar los datos
        asi que hago la  trampa y los meto a mano.
        Creo que todas las facultades tienen las mismas semanas, al menos en la guia.
        Lo he sacado de aqui: http://www.ehu.eus/documents/1675541/1827566/Calendario+2016-2017.pdf
    """
    #Cada posicion del array corresponde a la semana i+1 y al dia de inicio de las clases
    data = [
        { "anio": "2016","mes": "09","dia": "05" },
        { "anio": "2016","mes": "09","dia": "12" },
        { "anio": "2016","mes": "09","dia": "19" },
        { "anio": "2016","mes": "09","dia": "26" },
        { "anio": "2016","mes": "10","dia": "03" },
        { "anio": "2016","mes": "10","dia": "10" },
        { "anio": "2016","mes": "10","dia": "17" },
        { "anio": "2016","mes": "10","dia": "24" },
        { "anio": "2016","mes": "10","dia": "31" },
        { "anio": "2016","mes": "11","dia": "07" },
        { "anio": "2016","mes": "11","dia": "14" },
        { "anio": "2016","mes": "11","dia": "21" },
        { "anio": "2016","mes": "11","dia": "28" },
        { "anio": "2016","mes": "12","dia": "12" },
        { "anio": "2016","mes": "12","dia": "19" },
        { "anio": "2017","mes": "01","dia": "30" },
        { "anio": "2017","mes": "02","dia": "06" },
        { "anio": "2017","mes": "02","dia": "13" },
        { "anio": "2017","mes": "02","dia": "20" },
        { "anio": "2017","mes": "02","dia": "27" },
        { "anio": "2017","mes": "03","dia": "06" },
        { "anio": "2017","mes": "03","dia": "13" },
        { "anio": "2017","mes": "03","dia": "20" },
        { "anio": "2017","mes": "03","dia": "27" },
        { "anio": "2017","mes": "04","dia": "03" },
        { "anio": "2017","mes": "04","dia": "10" },
        { "anio": "2017","mes": "04","dia": "24" },
        { "anio": "2017","mes": "05","dia": "01" },
        { "anio": "2017","mes": "05","dia": "08" },
        { "anio": "2017","mes": "05","dia": "15" }
    ]
    return data

def getInicioSemana(sem):
    """
        Devuelve el dia de inicio de una semana en concreto
    """
    return getDiasSemanas()[sem-1]
