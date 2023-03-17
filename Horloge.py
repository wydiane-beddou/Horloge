import datetime
import time

def afficher_heure(Clock, alarm):
    heure = datetime.datetime.combine(datetime.date.today(), datetime.time(*Clock))
    while True:
        Heure = heure.strftime("%H:%M:%S")
        print(Heure)

        if heure.hour == alarm[0] and heure.minute == alarm[1] and heure.second == alarm[2]:
            print("ALARME !")
            break
    
        heure += datetime.timedelta(seconds=1)
        time.sleep(1)

Clock = tuple(map(int, input("Entrez l'heure actuelle (format 24 heures): ").split(":")))
alarm = tuple(map(int, input("Entrez l'heure d'alarme (format 24 heures): ").split(":")))

afficher_heure(Clock, alarm)