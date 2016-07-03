import datetime
from icalendar import Calendar, Event, vCalAddress, vText, vFrequency, vRecur
import json

# Input: JSON estandar de calendario
# Output: Contenido en formato iCal
#   Anade el curso academico al calendario y la fecha de creacion
#   Anade un evento por cada fecha de inicio y fin de cuatrimestre
def createCalendarJson(dataDict):
    Ic1 = dateFormat(dataDict['inicioPrimerCuatrimestre_year'],dataDict['inicioPrimerCuatrimestre_month'],dataDict['inicioPrimerCuatrimestre_day'])
    Fc1 = dateFormat(dataDict['finPrimerCuatrimestre_year'],dataDict['finPrimerCuatrimestre_month'],dataDict['finPrimerCuatrimestre_day'])
    Ic2 = dateFormat(dataDict['inicioSegundoCuatrimestre_year'],dataDict['inicioSegundoCuatrimestre_month'],dataDict['inicioSegundoCuatrimestre_day'])
    Fc2 = dateFormat(dataDict['finSegundoCuatrimestre_year'],dataDict['finSegundoCuatrimestre_month'],dataDict['finSegundoCuatrimestre_day'])
    str(Ic1)

    data={
        'cursoAcademico' : dataDict['cursoAcademico'],
        'inicioCuatrimestreUno' : Ic1,
        'finCuatrimestreUno' : Fc1,
        'inicioCuatrimestreDos' : Ic2,
        'finCuatrimestreDos' : Fc2
    }
    return json.dumps(data)

def transformarJSON(datos):
    return json.dumps(datos)

def createCalendar(data):
    try:
        cal = Calendar()
        # anade al calendario el curso academico
        data = createCalendarJson(data)
        print data['inicioCuatrimestreUno']
        print data['inicioCuatrimestreDos']
        cal.add('prodid', data['cursoAcademico'])
        # anade a calendario la fecha de creacion
        cal.add('dtstamp', datetime.datetime.today())
        # anade los eventos de inicio y fin de cuatrimestre
        cal.add_component(nuevo_evento(data['inicioCuatrimestreUno'],data['inicioCuatrimestreUno'],'Inicio Primer Cuatrimestre'))
        cal.add_component(nuevo_evento(data['finCuatrimestreUno'],data['finCuatrimestreUno'],'Fin Primer Cuatrimestre'))
        cal.add_component(nuevo_evento(data['inicioCuatrimestreDos'],data['inicioCuatrimestreDos'],'Inicio Segundo Cuatrimestre'))
        cal.add_component(nuevo_evento(data['finCuatrimestreDos'],data['finCuatrimestreDos'],'Fin Segundo Cuatrimestre'))
        #cal_content = cal.to_ical()
        return cal_content
    except Exception as e:
        print("Error al crear calendario")
        print (str(e))
# Input: Fechas inicio y fin en formato estandar de JSON calendario "YYYY/MM/DD WED"
#         Summary descripcion texto del evento
#         Extension : Lugar del evento
# Output: Evento de dia entero con parametros de entrada y UID = fecha inicio
def nuevo_evento(fechaInicio, fechaFin, Summary):
    try:
        event = Event()
        fechaI = fechaInicio.split(' ')[0] + " 00:00:00"
        fechaF = fechaFin.split(' ')[0] + " 23:59:59"
        event['dtstart']= formatodata(fechaI)
        event['dtend']= formatodata(fechaF)
        event['summary']= Summary
        event['uid'] = fechaI
        return event
    except Exception as e:
        print("Error al crear evento")
        print (str(e))

# Input: Fecha en formato YYYY/MM/DD HH:MM:SS
# Output: Fecha en formato YYYYMMDDTHHMMSS adecuado para icalendar
def formatodata(date):
    d = datetime.datetime.strptime(date,'%Y/%m/%d %H:%M:%S')
    return d.strftime('%Y%m%dT%H%M%S')

# Input: Fecha en formato YYYY/MM/DD
# Output: Fecha en formato YYYY/MM/DD WED
def dateFormat(year,month,day):
    d = datetime.datetime(int(year), int(month), int(day))
    value = d.strftime('%Y/%m/%d')
    wd_list = [" SUN"," MON"," TUE"," WED"," THU"," FRI"," SAT"];
    weekday = wd_list[d.weekday()]
    return d.strftime('%Y/%m/%d') + weekday
