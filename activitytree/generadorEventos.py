import time
import datetime
import random
#import redis
from FIS import *
#server=redis.Redis("127.0.0.1")

actores= ["User","Device"]

users="Sharita Chamberlin,Ewa Nault,Josh Balzer,Kristian Bonenfant,Tasha Marchand,America Peloquin,Azalee Callaway,Angele Mcnab,Celsa Gullette,Soraya Glorioso,Edison Rocamora,Leena Rolando,Temeka Armand,Belkis Rubottom,Julieann Taketa,Enola Wakeland,Reanna Fausnaught,Yahaira Brissette,Kristi Sabala,Georgene Petillo,Lashay Struck,Ja Lasky,Zachary Elliff,Alona Forshee,Jane Cobian,Mittie Cantwell,Jeremy Rarick,Barbar Plate,Brandie Coursey,Kizzy Gourley".split(',')
user_verbs= ["Login","Logout","Answered","Approached"]

device_names={1:"Monitor",2:"Monitor",3:"Tablet",4:"SmartPhone",5:"Projector",6:"Speakers"}
device_verbs={1:"Playing",2:"Asking",3:"Showing",4:"Waiting"}

#index=[i for i in range(30)]
#name=dict(zip(index,names))

def evento(OT,DN,VB,D,T):
    ress={"actor": {"objectType":OT,"displayName":DN},"verb":VB,"Date":D,"Time":T}
    return(ress)

logins={}

eventos=[]

timex=int(round(time.time()))

for x in range(1000):
    actor_temp = random.choice(actores)

    if actor_temp == "User":
        date=str(datetime.date.today())
        timex=timex+random.randint(1,60)

        nametemp=users[int(random.gauss(15,5))]

        verbtemp=random.choice(user_verbs)

        if  nametemp  not in logins:
            logins[nametemp]=1
            eventos.append(evento("User",nametemp,"Login",date,timex))

        elif nametemp in logins and verbtemp=="Logout":
            del logins[nametemp]
            eventos.append(evento("User",nametemp,verbtemp,date,timex))

        elif nametemp in logins and verbtemp not in  ["Logout","Login"]:
            eventos.append(evento("User",nametemp,verbtemp,date,timex))
    else:
        pass

for evento in eventos:
    print evento