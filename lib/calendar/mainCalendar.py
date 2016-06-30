import datetime
from icalendar import Calendar, Event, vCalAddress, vText, vFrequency, vRecur
import json
def switch_dias(dia):
    """
    Funcion que hace de swicth porque no se les ocurrio hacerlo a los que crearon el lenguaje
     y tengo que estar haciendolo yo aunque ahora no la uso
    """
    switcher = {
        1: "lunes",
        2: "martes",
        3: "miercoles",
        4: "jueves",
        5: "viernes"
    }
    return switcher.get(dia, "lunes", titulo)

def __eventsByType(data, cal, titulo, calendarioSemanal):
    """
    Funcion para aniadir clases al calendario
    """
    for clases in data:
        for dias in clases["dias_semanas"]:
            event = Event()
            horas = dias["horas"].split("-")
            hInicial = horas[0].split(":")
            hFinal = horas[1].split(":")
            rangosemanas = clases["rango_semanas"].split("-") #Numero de semanas que se va a repetir

            inicioSemana = calendarioSemanal[int(rangosemanas[0])-1]

            horainicio = datetime.datetime(int(inicioSemana["anio"]), int(inicioSemana["mes"]), int(inicioSemana["dia"]), int(hInicial[0]), int(hInicial[1]), 0) #Hora a la que empieza
            horaFin = datetime.datetime(int(inicioSemana["anio"]), int(inicioSemana["mes"]), int(inicioSemana["dia"]), int(hFinal[0]), int(hFinal[1]), 0) #Hora a la que termina
            event.add('dtstart', horainicio + datetime.timedelta(days=int(dias["dia"]) - 1))
            event.add('dtend', horainicio + datetime.timedelta(days=int(dias["dia"]) - 1))
            event.add('summary', titulo)

            event.add('rrule', {'freq': 'weekly', 'count': int(rangosemanas[1]) - int(rangosemanas[0])})
            event['uid'] = str(horainicio) + '@magnasis.com'

            cal.add_component(event) #Aniado el evento al calendario
    return cal

def createCalendar(data, calendarioSemanal):
    """
    Aqui es donde la magia pasa
    """
    try:
        cal = Calendar()

        for item in data["asignaturas"]:
            cal = __eventsByType(item["teorico"], cal, item["nombre"], calendarioSemanal)
            cal = __eventsByType(item["practico"], cal, item["nombre"], calendarioSemanal)

        cal_content = cal.to_ical()
        #with open("meeting.ics", 'wb') as f:
        #    f.write(cal_content)
        return cal_content
    except Exception as e:
        """
         Que lo gestionen los de magnasis
         """
        print("Si te sale este mensaje es porque algo has hecho mal, tu culpa tio")
        print (str(e))
