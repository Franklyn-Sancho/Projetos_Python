import datetime
import time

def esta_na_hora(hora, minuto, hora_atual):
    if hora_atual.hour == hora and hora_atual.minute == minuto:
        return True
    return False

def processa_dias_da_semana(dias_da_semana):
    dias_da_semana_int = []

    for dia in dias_da_semana:
        if dia == "seg":
            dias_da_semana_int.append(0)
        if dia == "ter":
            dias_da_semana_int.append(1)
        if dia == "qua":
            dias_da_semana_int.append(2)
        if dia == "qui":
            dias_da_semana_int.append(3)
        if dia == "sex":
            dias_da_semana_int.append(4)
        if dia == "sab":
            dias_da_semana_int.append(5)
        if dia == "dom":
            dias_da_semana_int.append(6)

    return dias_da_semana_int

def esta_no_dia_semana(dias_desejados, data_atual):
    if data_atual.weekday() in dias_desejados:
        return True
    
    return False

print("++++++++++++++++++++++++++")
print("DESPERTADOR")
print("++++++++++++++++++++++++++")

hora_string = input("Que horas você quer acordar? (hh:mm): ")
dia_da_semana_string = input("quais dias da semana? (seg, ter, qua, qui, sex, sab, dom): ")

hora = int(hora_string.split(':')[0])
minuto = int(hora_string.split(':')[1])

dias_da_semana = dia_da_semana_string.split(' ')
dias_da_semana_int = processa_dias_da_semana(dias_da_semana)

agora = datetime.datetime.now()

while True:
    now = datetime.datetime.now()

    if esta_na_hora(hora, minuto, now) and esta_no_dia_semana(dias_da_semana_int, now):
        print("ACORDAR")

    time.sleep(60)




