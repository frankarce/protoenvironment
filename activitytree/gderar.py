__author__ = 'framk'
import time
import datetime
import random
from random import choice
from operator import itemgetter
#import redis
from FIS import *
#server=redis.Redis("127.0.0.1")
actores= ["User","Device"]
users="Sharita Chamberlin,Ewa Nault,Josh Balzer,Kristian Bonenfant,Tasha Marchand,America Peloquin,Azalee Callaway,Angele Mcnab,Celsa Gullette,Soraya Glorioso,Edison Rocamora,Leena Rolando,Temeka Armand,Belkis Rubottom,Julieann Taketa,Enola Wakeland,Reanna Fausnaught,Yahaira Brissette,Kristi Sabala,Georgene Petillo,Lashay Struck,Ja Lasky,Zachary Elliff,Alona Forshee,Jane Cobian,Mittie Cantwell,Jeremy Rarick,Barbar Plate,Brandie Coursey,Kizzy Gourley".split(',')
user_verbs= ["Login","Logout","Answered","Approached"]
device_names=["Monitor","Monitor","Tablet","SmartPhone","Projector","Speakers"]
device_verbs=["Start","Shutdown","Playing","Asking","Showing","Waiting"]
#index=[i for i in range(30)]
#name=dict(zip(index,names))
print len(users)
def evento(OT,DN,VB,D,T):
    ress={"actor": {"objectType":OT,"displayName":DN},"verb":VB,"Date":D,"Time":T}
    return(ress)
g=0
logins={}
loginsd={}
eventos=[]
timex=int(round(time.time()))
logouts=range(10,1000,20)
for x in range(1000):
    actor_temp = random.choice(actores)
    if actor_temp == "User":
        date=str(datetime.date.today())
        timex=timex+random.randint(1,60)
        #nametemp=users[int(random.gauss(15,5))]
        nametemp=users[int(random.triangular(0,29,14))]
        random_for_weighted=random.random()
        #if x==500:
        #    random.shuffle(users)
        if random_for_weighted < 0.1:
            verbtemp=user_verbs[0]
        else:
            verbtemp=user_verbs[random.randint(2,3)]
        if x in logouts and len(logins) > 1:
            to_Del=choice(logins.keys())
            eventos.append(evento(actor_temp,to_Del,"Logout",date,timex))
            del logins[to_Del]
        elif  nametemp  not in logins:
            logins[nametemp]=1
            eventos.append(evento(actor_temp,nametemp,"Login",date,timex))
        elif nametemp in logins and verbtemp not in  ["Logout","Login"]:
            eventos.append(evento(actor_temp,nametemp,verbtemp,date,timex))
        else:
            eventos.append(evento(actor_temp,nametemp,verbtemp,date,timex))
    else:
        date=str(datetime.date.today())
        timex=timex+random.randint(1,60)
        device_temp=device_names[random.randint(1,5)]
        random_for_weighted=random.random()
        if random_for_weighted < 0.2:
            device_verbtemp=device_verbs[random.randint(0,1)]
        else:
            device_verbtemp=device_verbs[random.randint(2,5)]
        if  device_temp  not in loginsd:
            loginsd[device_temp]=1
            eventos.append(evento(actor_temp,device_temp,"Start",date,timex))
        elif device_temp in loginsd and device_temp=="Shutdown":
            del loginsd[device_temp]
            eventos.append(evento(actor_temp,device_temp,device_verbtemp,date,timex))
        else:
        #elif device_temp in logins and device_temp not in  ["Start","Shutdown"]:
            eventos.append(evento(actor_temp,device_temp,device_verbtemp,date,timex))

#Conteo de los eventos
countLI={}
countLO={}
countAn={}
countAp={}
for i in range(len(eventos)):
    user_temp=eventos[i]["actor"]["displayName"]
    if eventos[i]["verb"]=="Login":
        countLI[user_temp]=countLI.get(user_temp, 1)+1
    if eventos[i]["verb"]=="Logout":
        countLO[user_temp]=countLO.get(user_temp, 1)+1
    if eventos[i]["verb"]=="Answered":
        countAn[user_temp]=countAn.get(user_temp, 1)+1
    if eventos[i]["verb"]=="Approached":
        countAp[user_temp]=countAp.get(user_temp, 1)+1

#Convierto el diccionario en lista y la divido para usarlos en el Fis
Login=dict.items(countLI)
Logout=dict.items(countLO)
Answ=dict.items(countAn)
Appro=dict.items(countAp)
name_Logi1,num_logi1=zip(*Login)
name_Logo1,num_logo1=zip(*Logout)
name_asn1,num_ans1=zip(*Answ)
name_app1,num_app1=zip(*Appro)

#Lleno de 0 los que no aparecieron en los eventos
for i in range(30):
    if users[i] not in name_Logi1:
        Login.append([users[i],0])
    if users[i] not in name_Logi1:
        Logout.append([users[i],0])
    if users[i] not in name_asn1:
        Answ.append([users[i],0])
    if users[i] not in name_app1:
        Appro.append([users[i],0])
#Ordeno por nombre
Login=sorted(Login, key=itemgetter(0))
Answ=sorted(Answ, key=itemgetter(0))
Appro=sorted(Appro, key=itemgetter(0))
name_Logi,num_logi=zip(*Login)
name_Logo,num_logo=zip(*Logout)
name_asn,num_ans=zip(*Answ)
name_app,num_app=zip(*Appro)
##################imprimia la lista para ver numeros########################
#
#for u in range(30):
#    print Login[u][0],Login[u][1]
##for u in range(len(Logout)):
#print " "
#for u in range(30):
#    print u,Answ[u][0], Answ[u][1]
#print " "
#for u in range(30):
#    print u,Appro[u][0], Appro[u][1]
##for w in range(len(eventos)):
##    print eventos[w]

##############################FIS##############################################

Logs = LinguisticVariable('Logins')
Logs.addMF('Low',MF.Triangular(-4, 0, 4))
Logs.addMF('Mid',MF.Triangular(1, 5, 9))
Logs.addMF('High',MF.Triangular(6, 10, 14))
Answers = LinguisticVariable('Answer')
Answers.addMF('Low',MF.Triangular(-4, 0, 8))
Answers.addMF('High',MF.Triangular(2, 10, 14))
Approached = LinguisticVariable('Approached')
Approached.addMF('Low',MF.Triangular(-4, 0, 8))
Approached.addMF('High',MF.Triangular(2, 10, 14))
#OUT
Out = LinguisticVariable('topN', type='out', range=(0, 1))
Out.addMF('Low',MF.Triangular(-0.4, 0, 0.4,))
Out.addMF('Mid',MF.Triangular(0.1, 0.5, 0.9))
Out.addMF('High',MF.Triangular(0.6, 1, 1.4))
# Rules
#if Logs == Low and Answer == low and Approached == Low then Out == Low
r1 = FuzzyRule()
r1.antecedent.append(FuzzyOperator('and',FuzzyProposition(Logs,Logs.mfs['Low'])
                                        ,FuzzyOperator('and',FuzzyProposition(Answers,Answers.mfs['Low'])
                                        ,FuzzyProposition(Approached,Approached.mfs['Low']))))
r1.consequent.append(FuzzyProposition(Out,Out.mfs['Low']))
#if Logs == Low and Answer == High and Approached == Low then Out == Low
r2 = FuzzyRule()
r2.antecedent.append(FuzzyOperator('and',FuzzyProposition(Logs,Logs.mfs['Low'])
                                        ,FuzzyOperator('and',FuzzyProposition(Answers,Answers.mfs['Low'])
                                        ,FuzzyProposition(Approached,Approached.mfs['High']))))
r2.consequent.append(FuzzyProposition(Out,Out.mfs['Low']))
#if Logs == Low and Answer == High and Approached == Low then Out == Low
r3 = FuzzyRule()
r3.antecedent.append(FuzzyOperator('and',FuzzyProposition(Logs,Logs.mfs['Low'])
                                        ,FuzzyOperator('and',FuzzyProposition(Answers,Answers.mfs['High'])
                                        ,FuzzyProposition(Approached,Approached.mfs['Low']))))
r3.consequent.append(FuzzyProposition(Out,Out.mfs['Low']))
#if Logs == Low and Answer == High and Approached == Low then Out == Low
r4 = FuzzyRule()
r4.antecedent.append(FuzzyOperator('and',FuzzyProposition(Logs,Logs.mfs['Low'])
                                        ,FuzzyOperator('and',FuzzyProposition(Answers,Answers.mfs['High'])
                                        ,FuzzyProposition(Approached,Approached.mfs['High']))))
r4.consequent.append(FuzzyProposition(Out,Out.mfs['Low']))
#if Logs == Low and Answer == High and Approached == Low then Out == Low
r5 = FuzzyRule()
r5.antecedent.append(FuzzyOperator('and',FuzzyProposition(Logs,Logs.mfs['Mid'])
                                        ,FuzzyOperator('and',FuzzyProposition(Answers,Answers.mfs['Low'])
                                        ,FuzzyProposition(Approached,Approached.mfs['Low']))))
r5.consequent.append(FuzzyProposition(Out,Out.mfs['Mid']))
#if Logs == Low and Answer == High and Approached == Low then Out == Low
r6 = FuzzyRule()
r6.antecedent.append(FuzzyOperator('and',FuzzyProposition(Logs,Logs.mfs['Mid'])
                                        ,FuzzyOperator('and',FuzzyProposition(Answers,Answers.mfs['Low'])
                                        ,FuzzyProposition(Approached,Approached.mfs['High']))))
r6.consequent.append(FuzzyProposition(Out,Out.mfs['Mid']))
#if Logs == Low and Answer == High and Approached == Low then Out == Low
r7 = FuzzyRule()
r7.antecedent.append(FuzzyOperator('and',FuzzyProposition(Logs,Logs.mfs['Mid'])
                                        ,FuzzyOperator('and',FuzzyProposition(Answers,Answers.mfs['High'])
                                        ,FuzzyProposition(Approached,Approached.mfs['Low']))))
r7.consequent.append(FuzzyProposition(Out,Out.mfs['Mid']))
#if Logs == Low and Answer == High and Approached == Low then Out == Low
r8 = FuzzyRule()
r8.antecedent.append(FuzzyOperator('and',FuzzyProposition(Logs,Logs.mfs['Mid'])
                                        ,FuzzyOperator('and',FuzzyProposition(Answers,Answers.mfs['High'])
                                        ,FuzzyProposition(Approached,Approached.mfs['High']))))
r8.consequent.append(FuzzyProposition(Out,Out.mfs['Mid']))
#if Logs == Low and Answer == High and Approached == Low then Out == Low
r9 = FuzzyRule()
r9.antecedent.append(FuzzyOperator('and',FuzzyProposition(Logs,Logs.mfs['High'])
                                        ,FuzzyOperator('and',FuzzyProposition(Answers,Answers.mfs['Low'])
                                        ,FuzzyProposition(Approached,Approached.mfs['Low']))))
r9.consequent.append(FuzzyProposition(Out,Out.mfs['High']))
#if Logs == Low and Answer == High and Approached == Low then Out == Low
r10 = FuzzyRule()
r10.antecedent.append(FuzzyOperator('and',FuzzyProposition(Logs,Logs.mfs['High'])
                                        ,FuzzyOperator('and',FuzzyProposition(Answers,Answers.mfs['Low'])
                                        ,FuzzyProposition(Approached,Approached.mfs['High']))))
r10.consequent.append(FuzzyProposition(Out,Out.mfs['High']))
#if Logs == Low and Answer == High and Approached == Low then Out == Low
r11 = FuzzyRule()
r11.antecedent.append(FuzzyOperator('and',FuzzyProposition(Logs,Logs.mfs['High'])
                                        ,FuzzyOperator('and',FuzzyProposition(Answers,Answers.mfs['High'])
                                        ,FuzzyProposition(Approached,Approached.mfs['Low']))))
r11.consequent.append(FuzzyProposition(Out,Out.mfs['High']))
#if Logs == Low and Answer == High and Approached == Low then Out == Low
r12 = FuzzyRule()
r12.antecedent.append(FuzzyOperator('and',FuzzyProposition(Logs,Logs.mfs['High'])
                                        ,FuzzyOperator('and',FuzzyProposition(Answers,Answers.mfs['High'])
                                        ,FuzzyProposition(Approached,Approached.mfs['High']))))
r12.consequent.append(FuzzyProposition(Out,Out.mfs['High']))
Reglas=[r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12]
fis = FIS(Reglas)
def evaluate(logs,Ans,App):
    Logs.current_value = logs
    Answers.current_value = Ans
    Approached.current_value = App
    return fis.eval( out_var = 0)
if __name__ == '__main__':
    for g in range(29):
        print num_logi[g],num_ans[g],num_app[g]
        print evaluate(num_logi[g],num_ans[g],num_app[g])