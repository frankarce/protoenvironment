__author__ = 'franciscoarcecardenas'
import time
import datetime
import random
import redis
from FIS import *
server=redis.Redis("127.0.0.1")
names="Sharita Chamberlin,Ewa Nault,Josh Balzer,Kristian Bonenfant,Tasha Marchand,America Peloquin,Azalee Callaway,Angele Mcnab,Celsa Gullette,Soraya Glorioso,Edison Rocamora,Leena Rolando,Temeka Armand,Belkis Rubottom,Julieann Taketa,Enola Wakeland,Reanna Fausnaught,Yahaira Brissette,Kristi Sabala,Georgene Petillo,Lashay Struck,Ja Lasky,Zachary Elliff,Alona Forshee,Jane Cobian,Mittie Cantwell,Jeremy Rarick,Barbar Plate,Brandie Coursey,Kizzy Gourley"

user=["User","Device"]
names2="Monitor,Monitor,Tablet,SmartPhone,Projector,Speakers"
verbs="Login,Logout,Answered,Approached"
verbs2="Playing,Asking,Showing,Waiting"
verb=verbs.split(',')
verb2=verbs2.split(',')
name=names.split(',')

name2=names2.split(',')

logins=[0]*50
lista={}
timex=int(round(time.time()))
a=0
for x in range(1000):
    date=str(datetime.date.today())
    timex=timex+random.randint(1,60)
    nametemp=random.randint(0,29)
    verbtemp=random.randint(0,3)
    if random.randint(0,1) == 0:
        if verbtemp==0 and logins[nametemp]==1:
            actor=name[nametemp]
            verbo=verb[1]
            logins[nametemp]=0
            evento1={"actor": {"objectType":"User","displayName":actor},"verb":verbo,"Date":date,"Time":str(timex)}
            lista[x]=evento1

            #server.rpush("eventos",evento1)
        elif verbtemp==1 and logins[nametemp]==0:
            actor=name[nametemp]
            verbo=verb[1]
            logins[nametemp]=0
            evento1={"actor": {"objectType":"User","displayName":actor},"verb":verbo,"Date":date,"Time":str(timex)}
            lista[x]=evento1
            #server.rpush("eventos",evento1)

        elif verbtemp==0 and logins[nametemp]==0:
            actor=name[nametemp]
            verbo=verb[0]
            logins[nametemp]=1
            evento1={"actor": {"objectType":"User","displayName":actor},"verb":verbo,"Date":date,"Time":str(timex)}
            lista[x]=evento1
            #server.rpush("eventos",evento1)
        elif verbtemp==1 and logins[nametemp]==1:
            actor=name[nametemp]
            verbo=verb[1]
            logins[nametemp]=0
            evento1={"actor": {"objectType":"User","displayName":actor},"verb":verbo,"Date":date,"Time":str(timex)}
            lista[x]=evento1
            #server.rpush("eventos",evento1)

        elif verbtemp==2 and logins[nametemp]==1:
             actor=name[nametemp]
             verbo=verb[2]
             evento1={"actor": {"objectType":"User","displayName":actor},"verb":verbo,"Date":date,"Time":str(timex)}
             lista[x]=evento1
             #server.rpush("eventos",evento1)
        elif verbtemp==3 and logins[nametemp]==1:
             actor=name[nametemp]
             verbo=verb[3]
             evento1={"actor": {"objectType":"User","displayName":actor},"verb":verbo,"Date":date,"Time":str(timex)}
             lista[x]=evento1
             #server.rpush("eventos",evento1)
        else:
            evento2={"actor": {"objectType":"Device","displayName":name2[random.randint(0,3)]},"verb":verb2[random.randint(0,3)],"Date":date,"Time":str(timex)}
            #server.rpush("eventos",evento2)
            lista[x]=evento2
    else:

        evento2={"actor": {"objectType":"Device","displayName":name2[random.randint(0,3)]},"verb":verb2[random.randint(0,3)],"Date":date,"Time":str(timex)}
        lista[x]=evento2
        #server.rpush("eventos",evento2)


q=lista[0]
contadora=[0]*30
contadorb=[0]*30
contadorc=[0]*30
contadord=[0]*30

#print lista[0]["actor"]["objectType"]
for z in range(1000):
    for c in range(30):
        if lista[z]["actor"]["objectType"]=="User" and lista[z]["actor"]["displayName"]==name[c]and lista[z]["verb"]=="Login":
            contadora[c]=contadora[c]+1
        elif lista[z]["actor"]["objectType"]=="User" and lista[z]["actor"]["displayName"]==name[c]and lista[z]["verb"]=="Logout":
            contadorb[c]=contadorb[c]+1
        elif lista[z]["actor"]["objectType"]=="User" and lista[z]["actor"]["displayName"]==name[c]and lista[z]["verb"]=="Answer":
            contadorc[c]=contadorc[c]+1
        elif lista[z]["actor"]["objectType"]=="User" and lista[z]["actor"]["displayName"]==name[c]and lista[z]["verb"]=="Approached":
            contadord[c]=contadord[c]+1



##############################FIS########################################

# Variables
#IN's
Logs = LinguisticVariable('Logins')
Logs.addMF('Low',MF.Triangular(0, 0, 3))
Logs.addMF('Mid',MF.Triangular(3, 5, 8))
Logs.addMF('High',MF.Triangular(7, 10, 10))

Answers = LinguisticVariable('Answer')
Answers.addMF('Low',MF.Triangular(0, 0, 6))
Answers.addMF('High',MF.Triangular(4, 10, 10))

Approached = LinguisticVariable('Approached')
Approached.addMF('Low',MF.Triangular(0, 0, 6))
Approached.addMF('High',MF.Triangular(4, 10, 10))
#OUT
Out = LinguisticVariable('topN', type='out', range=(0, 1))
Out.addMF('Low',MF.Triangular(0, 0, 0.4))
Out.addMF('Mid',MF.Triangular(0.3, 0.5, 0.7))
Out.addMF('High',MF.Triangular(0.6, 1, 1))

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
r4.consequent.append(FuzzyProposition(Out,Out.mfs['Mid']))
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
r9.consequent.append(FuzzyProposition(Out,Out.mfs['Mid']))
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

def eval(logs,Ans,App):
    Logs.current_value = logs
    Answers.current_value = Ans
    Approached.current_value = App
    return fis.eval( out_var = 0)

if __name__ == '__main__':
    for g in range(30):
        print eval(contadora[g],contadorc[g],contadord[g])