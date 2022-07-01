from datetime import date, timedelta, datetime
import pandas as pd
import sys
import requests


def descargar_data_sen(str_date):
    # fechas
    fecha_actual = datetime.strptime(str(str_date), '%Y-%m-%d %H:%M:%S').date() + timedelta(1)
    fecha_actual = fecha_actual.strftime('%Y%m%d')
    fecha_ayer = datetime.strptime(str(str_date), '%Y-%m-%d %H:%M:%S').date()
    fecha_ayer = fecha_ayer.strftime('%Y%m%d')
    fecha_ayer2 = datetime.strptime(str(str_date), '%Y-%m-%d %H:%M:%S').date()
    fecha_ayer2 = fecha_ayer2.strftime('%y%m%d')

    url = 'https://opreal.coordinador.cl/uploads/cdecsic_mvp/cdecsic/' + fecha_actual + '/' + fecha_ayer \
          + '.consolidado-global.estado-actual.' + fecha_actual + '1030.prn'


    #ruta = r'//10.20.3.251/negocios/BBDD/RO/comun/' + 'RO' + str(fecha_ayer2) + '.prn'
    ruta ='C:/Users/crist/OneDrive - Hidromaule S.A/data_sen/' + 'RO' + str(fecha_ayer2) + '.prn'

    r = requests.get(url, allow_redirects=True, verify=False)
    open(ruta, 'wb').write(r.content)

def in_fechas():
    # input de fechas para carga manual de datos
    input_fecha_inicio = input('fecha inicio en formato yyyy-mm-dd: ')
    input_fecha_final = input('fecha final en formato yyyy-mm-dd: ')
    year1, month1, day1 = map(int, input_fecha_inicio.split('-'))
    year2, month2, day2 = map(int, input_fecha_final.split('-'))
    fecha_inicio = date(year1, month1, day1)
    fecha_final =  date(year2, month2, day2)

    print(fecha_inicio)
    # print(fecha_inicio, fecha_final)
    return fecha_inicio, fecha_final

def run_range():
    fecha_ini, fecha_fin = in_fechas()
    lista_fechas = pd.date_range(fecha_ini, fecha_fin, freq='d')

    for i in range(len(lista_fechas)):
        descargar_data_sen(lista_fechas[i])
        print('datos del: ' + str(lista_fechas[i]) + ' fueron cargados')

def run():
    str_date = date.today() - timedelta(days=1)
    print(str_date)
    descargar_data_sen(str_date)
    print('datos del: ' + str(str_date) + ' fueron cargados')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    globals()[sys.argv[1]]()

