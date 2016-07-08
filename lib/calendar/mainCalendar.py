import datetime
from icalendar import Calendar, Event, vCalAddress, vText, vFrequency, vRecur
import json



# Input: diccionario con la informacion basica del calendario recibida del formulario
# Output: calendario en formato JSON
def createCalendarJson(dataDict):

    Ic1 = dateFormat(dataDict['inicioPrimerCuatrimestre'])
    Fc1 = dateFormat(dataDict['finPrimerCuatrimestre'])
    Ic2 = dateFormat(dataDict['inicioSegundoCuatrimestre'])
    Fc2 = dateFormat(dataDict['finSegundoCuatrimestre'])

    #Propositos de testing
    '''
    Ic1 = '2000/10/01 MON'
    Fc1 = '2000/10/01 MON'
    Ic2 = '2000/10/01 MON'
    Fc2 = '2000/10/01 MON'
    '''


    data = {"calendario":{
        'cursoAcademico' : dataDict['cursoAcademico'],
        'inicioCuatrimestreUno' : Ic1,
        'finCuatrimestreUno' : Fc1,
        'inicioCuatrimestreDos' : Ic2,
        'finCuatrimestreDos' : Fc2,
        'diasSemanalesNoLectivos':[],
        'diasSinClase':[],
        'periodosHorarioEspecial':[],
        'semanasExcluidas':[],
        'intercambioDias':[]
    }}
    return json.dumps(data)

def transformarJSON(datos):
    return json.dumps(datos)

# Input: JSON estandar de calendario
# Output: Contenido en formato iCal
#   Anade el curso academico al calendario y la fecha de creacion
#   Anade un evento por cada fecha de inicio y fin de cuatrimestre
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
def icalDate(date):
    d = datetime.datetime.strptime(date,'%Y/%m/%d %H:%M:%S')
    return d.strftime('%Y%m%dT%H%M%S')

# Input: Fecha en formato YYYY/MM/DD
# Output: Fecha en formato YYYY/MM/DD WED
def dateFormat(date):
    d = datetime.datetime.strptime(date, '%d %B, %Y')
    wd_list = [" MON"," TUE"," WED"," THU"," FRI"," SAT", " SUN"];
    weekday = wd_list[d.weekday()]
    return d.strftime('%Y/%m/%d') + weekday



# Anadir eventos al calendario progresivamente
def editarInicioFinal(dataDict, data):
    if data == None:
        Ic1 = dateFormat(dataDict['inicioPrimerCuatrimestre'])
        Fc1 = dateFormat(dataDict['finPrimerCuatrimestre'])
        Ic2 = dateFormat(dataDict['inicioSegundoCuatrimestre'])
        Fc2 = dateFormat(dataDict['finSegundoCuatrimestre'])
        data = {"calendario":{
            'cursoAcademico' : dataDict['cursoAcademico'],
            'inicioCuatrimestreUno' : Ic1,
            'finCuatrimestreUno' : Fc1,
            'inicioCuatrimestreDos' : Ic2,
            'finCuatrimestreDos' : Fc2,
            'diasSemanalesNoLectivos':[],
            'diasSinClase':[],
            'periodosHorarioEspecial':[],
            'semanasExcluidas':[],
            'intercambioDias':[]
        }}
        return json.dumps(data)
    else:
        data['calendario']['cursoAcademico'] = dataDict['cursoAcademico']
        data['calendario']['inicioCuatrimestreUno'] = dateFormat(dataDict['inicioPrimerCuatrimestre'])
        data['calendario']['finCuatrimestreUno'] = dateFormat(dataDict['finPrimerCuatrimestre'])
        data['calendario']['inicioCuatrimestreDos'] = dateFormat(dataDict['inicioSegundoCuatrimestre'])
        data['calendario']['finCuatrimestreDos'] = dateFormat(dataDict['finSegundoCuatrimestre'])
    return data

#Anadir dias semanales no lectivos (MO, TU, WE, TH...)
def anadirDiasNoLectivos(dataDict, data):
    data['calendario']['diasSemanalesNoLectivos'].append(dataDict['diasSemanalesNoLectivos'])
    return data

def quitarDiasNoLectivos(dia, data):
    data['calendario']['diasSemanalesNoLectivos'].remove(dia)
    return data

def anadirDiasSinClase(dataDict, data):
    fecha = dateFormat(dataDict['fechaDiaSinClase'])
    dia={
        'motivo': dataDict['motivoDiasSinClase'],
        'fecha': fecha
    }
    data['calendario']['diasSinClase'].append(dia)
    return data

def quitarDiasSinClase(dia, data):
    return data['calendario']['diasSinClase'].remove(dia)


def anadirPeriodosHorarioEspecial(dataDict,data):
    fechaI = dateFormat(dataDict['fechaISemanasHorarioEspecial'])
    fechaF = dateFormat(dataDict['fechaFSemanasHorarioEspecial'])
    periodo={
        'fechaInicio':fechaI,
        'fechaFin':fechaF,
        'motivo': dataDict['motivoSemanasHorarioEspecial']
    }
    data['calendario']['periodosHorarioEspecial'].append(periodo)
    return data


def anadirSemanasExcluidas(dataDict, data):
    fechaI = dateFormat(dataDict['fechaISemanasExcluidas'])
    semana={
        'primerDiaSemana': fechaI,
        'motivo': dataDict['motivoSemanasExcluidas']
    }
    data['calendario']['semanasExcluidas'].append(semana)
    return data



def anadirDiasIntercambio(dataDict, data):
    fecha = dateFormat(dataDict['diaOriginal'])
    dia={
        'diaOriginal':fecha,
        'diaPorQueSeCambia':dataDict['diaporQueSeCambia']
    }
    data['calendario']['intercambioDias'].append(dia)
    return data