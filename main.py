from datetime import date, timedelta, datetime
import pandas as pd
import sys
import requests

def descargar_data_sen(str_date):
    # fechas
    fecha_actual = datetime.strptime(str(str_date), '%Y-%m-%d').date() + timedelta(1)
    fecha_actual = fecha_actual.strftime('%Y%m%d')
    fecha_ayer = datetime.strptime(str(str_date), '%Y-%m-%d').date()
    fecha_ayer = fecha_ayer.strftime('%Y%m%d')
    fecha_ayer2 = datetime.strptime(str(str_date), '%Y-%m-%d').date()
    fecha_ayer2 = fecha_ayer2.strftime('%y%m%d')

    url = 'https://opreal.coordinador.cl/uploads/cdecsic_mvp/cdecsic/' + fecha_actual + '/' + fecha_ayer \
          + '.consolidado-global.estado-actual.' + fecha_actual + '1030.prn'


    ruta = 'C:/Users/Cristobal Cruz/OneDrive - Hidromaule S.A/data_sen/' + 'RO' + str(fecha_ayer2) + '.prn'


    r = requests.get(url, allow_redirects=True, verify=False)
    open(ruta, 'wb').write(r.content)


def run():
    str_date = date.today() - timedelta(days=1)
    print(str_date)
    descargar_data_sen(str_date)
    print('datos del: ' + str(str_date) + ' fueron cargados')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

