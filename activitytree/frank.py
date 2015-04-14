__author__ = 'frank'
from activitytree.contextactivities import contextactivities
import redis
import json
####################### hecho para cambiar strings a diccionarios del antihuo contextactivities##############
dic={'url': 'http://127.0.0.1:5984/objetos/objetos/Jaime_Nuno2.png', 'estado': 'play', 'dispositivo': '1', 'tipo': 'imagen'}
serv=redis.Redis("localhost")
serv.set(1,dic)#a=contextactivities.keys()[2]
a=serv.lpush(1)
a=contextactivities['/activity/Historia'][0]
    #b=a.split(",")
    #c=({"url":b[0],"reproduce":b[1],"tipo":b[2],"dispositivo":b[3]})
b=json.dumps(a)
o=json.loads(b)
print o["url"]

#{'url': 'http://127.0.0.1:5984/objetos/objetos/Jaime_Nuno2.png', 'estado': 'play', 'dispositivo': '1', 'tipo': 'imagen'}