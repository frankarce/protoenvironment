# -*- coding: utf-8 -*-

##
##
##  Example of a Learning Activity Tree
##
##



if __name__ == "__main__":
    import os
    print "####### DJANGO SETTINGS"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "protoboard.settings")






from activitytree.models import LearningStyleInventory, LearningActivity, Course, UserLearningActivity
from django.contrib.auth.models import User
from activitytree.interaction_handler import SimpleSequencing



LearningActivity.objects.all().delete()
##############################          1
POO = LearningActivity( name = 'El Himno Nacional', slug = 'POO',
    uri = "/activity/POO",
    parent = None,
    root   = None,

    flow = True,
    forward_only = False,
    choice = True,
    choice_exit = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,

    is_container = True,
    is_visible = True,
    order_in_container = 0
    )

POO.save()
description= u"""
        <p> En este curso aprenderemos sobre el himno nacional mexicano, su historia, la letra que lo compone y a sus autores.</p>"""


cursoPOO = Course(short_description=description, root=POO)
cursoPOO.save()

#pretest = LearningActivity( name = 'pretest', slug = 'pretest',
#    uri = "/test/pretest",
#   lom = ,
#    parent = POO, root  = POO,

#    pre_condition_rule = "",
#    post_condition_rule = "" ,

#    rollup_rule  = "",
#    rollup_objective = True,
#    rollup_progress = True,
#    choice_exit = False,


#    is_container = False,
#    is_visible = False,
#    order_in_container = 0
#    )
#pretest.save()


##############################          2
historia = LearningActivity( name = 'Historia', slug = 'Historia',
    uri = "/activity/Historia",
#   lom =
    parent = POO, root  = POO,
    post_condition_rule = "",

    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = True,
    is_visible = False,
    order_in_container = 1
    )
historia.save()

historia1 = LearningActivity( name = 'Historia1', slug = 'Historia1',
    uri = "/activity/Historia1",
#   lom =
    parent = historia, root  = POO,
    post_condition_rule = "",
    pre_condition_rule = """if fisuserambiente.fisuser(self.user.learningstyleinventory.age,self.user.learningstyleinventory.aca_lvl) > 3:
	                  self.pre_condition = 'skip' """,
    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = False,
    order_in_container = 0
    )
historia1.save()

historia2 = LearningActivity( name = 'Historia2', slug = 'Historia2',
    uri = "/activity/Historia2",
#   lom =
    parent = historia, root  = POO,
    post_condition_rule = "",
    pre_condition_rule = """if fisuserambiente.fisuser(self.user.learningstyleinventory.age,self.user.learningstyleinventory.aca_lvl)  < 4 or fisuserambiente.fisuser(self.user.learningstyleinventory.age,self.user.learningstyleinventory.aca_lvl)  > 6:
	                  self.pre_condition = 'skip' """,
    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = False,
    order_in_container = 1
    )
historia2.save()

historia3 = LearningActivity( name = 'Historia3', slug = 'Historia3',
    uri = "/activity/Historia3",
#   lom =
    parent = historia, root  = POO,
    post_condition_rule = "",
    pre_condition_rule = """if fisuserambiente.fisuser(self.user.learningstyleinventory.age,self.user.learningstyleinventory.aca_lvl) < 6 or fisuserambiente.fisuser(self.user.learningstyleinventory.age,self.user.learningstyleinventory.aca_lvl)  > 9:
	                  self.pre_condition = 'skip' """,
    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = False,
    order_in_container = 2
    )
historia3.save()

Autores1 = LearningActivity( name = 'Autores1', slug = 'Autores1',
    uri = "/activity/Autores1",
#   lom =
    parent = POO, root  = POO,

    post_condition_rule = "",

    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = True,
    is_visible = False,
    order_in_container = 2
    )
Autores1.save()

Autores11 = LearningActivity(name = 'Autores11', slug = 'Autores11',
    uri = "/activity/Autores11",
#   lom =
    parent = Autores1, root  = POO,

    post_condition_rule = "",
    pre_condition_rule = """if fisuserambiente.fisuser(self.user.learningstyleinventory.age,self.user.learningstyleinventory.aca_lvl) > 3:
	                  self.pre_condition = 'skip' """,
    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = False,
    order_in_container = 0
    )
Autores11.save()

Autores12 = LearningActivity( name = 'Autores12', slug = 'Autores12',
    uri = "/activity/Autores12",
#   lom =
    parent = Autores1, root  = POO,

    post_condition_rule = "",
    pre_condition_rule = """if fisuserambiente.fisuser(self.user.learningstyleinventory.age,self.user.learningstyleinventory.aca_lvl)  < 4 or fisuserambiente.fisuser(self.user.learningstyleinventory.age,self.user.learningstyleinventory.aca_lvl)  > 6:
	                  self.pre_condition = 'skip' """,
    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = False,
    order_in_container = 1
    )
Autores12.save()

Autores13 = LearningActivity( name = 'Autores13', slug = 'Autores13',
    uri = "/activity/Autores13",
#   lom =
    parent = Autores1, root  = POO,

    post_condition_rule = "",
    pre_condition_rule = """if fisuserambiente.fisuser(self.user.learningstyleinventory.age,self.user.learningstyleinventory.aca_lvl) < 6 or fisuserambiente.fisuser(self.user.learningstyleinventory.age,self.user.learningstyleinventory.aca_lvl)  > 9:
	                  self.pre_condition = 'skip' """,
    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = False,
    order_in_container = 2
    )
Autores13.save()

Autores2 = LearningActivity( name = 'Autores2', slug = 'Autores2',
    uri = "/activity/Autores2",
#   lom =
    parent = POO, root  = POO,

    post_condition_rule = "",

    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = True,
    is_visible = False,
    order_in_container = 3
    )
Autores2.save()

Autores21 = LearningActivity( name = 'Autores21', slug = 'Autores21',
    uri = "/activity/Autores21",
#   lom =
    parent = Autores2, root  = POO,

    post_condition_rule = "",
    pre_condition_rule = """if fisuserambiente.fisuser(self.user.learningstyleinventory.age,self.user.learningstyleinventory.aca_lvl) > 3:
	                  self.pre_condition = 'skip' """,
    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = False,
    order_in_container = 0
    )
Autores21.save()

Autores22 = LearningActivity( name = 'Autores22', slug = 'Autores22',
    uri = "/activity/Autores22",
#   lom =
    parent = Autores2, root  = POO,

    post_condition_rule = "",
    pre_condition_rule = """if fisuserambiente.fisuser(self.user.learningstyleinventory.age,self.user.learningstyleinventory.aca_lvl)  < 4 or fisuserambiente.fisuser(self.user.learningstyleinventory.age,self.user.learningstyleinventory.aca_lvl)  > 6:
	                  self.pre_condition = 'skip' """,
    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = False,
    order_in_container = 1
    )
Autores22.save()

Autores23 = LearningActivity( name = 'Autores23', slug = 'Autores23',
    uri = "/activity/Autores23",
#   lom =
    parent = Autores2, root  = POO,

    post_condition_rule = "",
    pre_condition_rule = """if fisuserambiente.fisuser(self.user.learningstyleinventory.age,self.user.learningstyleinventory.aca_lvl) < 6 or fisuserambiente.fisuser(self.user.learningstyleinventory.age,self.user.learningstyleinventory.aca_lvl)  > 9:
	                  self.pre_condition = 'skip' """,
    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = False,
    order_in_container = 2
    )
Autores23.save()

Letra = LearningActivity( name = 'Letra', slug = 'Letra',
    uri = "/activity/Letra",
#   lom =
    parent = POO, root  = POO,

    post_condition_rule = "",

    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = True,
    is_visible = False,
    order_in_container = 4
    )
Letra.save()

Letra1 = LearningActivity( name = 'Letra1', slug = 'Letra1',
    uri = "/activity/Letra1",
#   lom =
    parent = Letra, root  = POO,

    post_condition_rule = "",
    pre_condition_rule = """if fisuserambiente.fisuser(self.user.learningstyleinventory.age,self.user.learningstyleinventory.aca_lvl) > 3:
	                  self.pre_condition = 'skip' """,
    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = False,
    order_in_container = 0
    )
Letra1.save()

Letra2 = LearningActivity( name = 'Letra2', slug = 'Letra2',
    uri = "/activity/Letra2",
#   lom =
    parent = Letra, root  = POO,

    post_condition_rule = "",
    pre_condition_rule = """if fisuserambiente.fisuser(self.user.learningstyleinventory.age,self.user.learningstyleinventory.aca_lvl)  < 4 or fisuserambiente.fisuser(self.user.learningstyleinventory.age,self.user.learningstyleinventory.aca_lvl)  > 6:
	                  self.pre_condition = 'skip' """,
    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = False,
    order_in_container = 1
    )
Letra2.save()

Letra3 = LearningActivity( name = 'Letra3', slug = 'Letra3',
    uri = "/activity/Letra3",
#   lom =
    parent = Letra, root  = POO,

    post_condition_rule = "",
    pre_condition_rule = """if fisuserambiente.fisuser(self.user.learningstyleinventory.age,self.user.learningstyleinventory.aca_lvl) < 6 or fisuserambiente.fisuser(self.user.learningstyleinventory.age,self.user.learningstyleinventory.aca_lvl)  > 9:
	                  self.pre_condition = 'skip' """,
    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = False,
    order_in_container = 2
    )
Letra3.save()

Uso = LearningActivity( name = 'Uso', slug = 'Uso',
    uri = "/activity/Uso",
#   lom =
    parent = POO, root  = POO,
    post_condition_rule = "",

    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = False,
    order_in_container = 5
    )
Uso.save()

Ensenanza = LearningActivity( name = 'Ensenanza', slug = 'Ensenanza',
    uri = "/activity/Ensenanza",
#   lom =
    parent = POO, root  = POO,
    post_condition_rule = "",

    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = False,
    order_in_container = 6
    )
Ensenanza.save()

Otrosidiomas = LearningActivity( name = 'Otrosidiomas', slug = 'Otrosidiomas',
    uri = "/activity/Otrosidiomas",
#   lom =
    parent = POO, root  = POO,
    post_condition_rule = "",

    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = False,
    order_in_container = 7
    )
Otrosidiomas.save()

Importancia = LearningActivity( name = 'Importancia', slug = 'Importancia',
    uri = "/activity/Importancia",
#   lom =
    parent = POO, root  = POO,
    post_condition_rule = "",

    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = False,
    order_in_container = 8
    )
Importancia.save()

Cine = LearningActivity( name = 'Cine', slug = 'Cine',
    uri = "/activity/Cine",
#   lom =
    parent = POO, root  = POO,
    post_condition_rule = "",

    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = False,
    order_in_container = 9
    )
Cine.save()

Curiosidades = LearningActivity( name = 'Curiosidades', slug = 'Curiosidades',
    uri = "/activity/Curiosidades",
#   lom =
    parent = POO, root  = POO,
    post_condition_rule = "",

    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = False,
    order_in_container = 10
    )
Curiosidades.save()

#Karaoke = LearningActivity( name = 'karaoke', slug = 'karaoke',
#    uri = "/activity/Karaoke",
#   lom =
#    parent = POO, root  = POO,
#    post_condition_rule = "",

#    flow = True,
#    forward_only = False,
#    choice = False,

#    rollup_rule  = "",
#    rollup_objective = True,
#    rollup_progress = True,
#    is_container = False,
#    is_visible = False,
#    order_in_container = 11
#    )
#Karaoke.save()
test = LearningActivity( name = 'test', slug = 'test',
    uri = "/test/test",
#   lom = ,
    parent = POO, root  = POO,

    pre_condition_rule = """if self.num_attempts == 0 :
 self.pre_condition = 'stopForwardTraversal'
else:
 self.pre_condition = 'hidden'""",
    post_condition_rule = "" ,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    choice_exit = False,


    is_container = False,
    is_visible = False,
    order_in_container = 11
    )
test.save()






##
##
##
## Example of two Users
##
##

User.objects.filter(username='ana').delete()
User.objects.filter(username='paul').delete()

j = User.objects.create_user('ana', 'lennon@thebeatles.com', '1234')
j.is_active = True
j.save()

p = User.objects.create_user('paul', 'paul@thebeatles.com', '1234')
p.is_active = True
p.save()

lsj=LearningStyleInventory(visual=12,verbal=11,aural=15,physical=9,logical=11,
                          social=9, solitary=10, age=5, aca_lvl=3, user = j)
lsj.save()

lsp=LearningStyleInventory(visual=12,verbal=11,aural=20,physical=9,logical=11,
                          social=9, solitary=7, age=15, aca_lvl=15, user = p)
lsp.save()

s = SimpleSequencing()

s = SimpleSequencing()
s.assignActivityTree(j,POO)
s.assignActivityTree(p,POO)


estudiantes = [
('edgar',          '1234',17,13,16,12,14,16,9, 25, 21),
('osuna',       '1234',15,12,14,18,14,19,8, 18, 4),
('malu',         '1234', 7,10, 4, 8,17,14,16, 18, 4),
('jose',        '1234',17, 6,16,13,14,11, 8, 18, 4),
('david',         '1234',15,10,13,14,17,15,11, 18, 4),
('juan',    '1234',11,13,11,10,13,18, 8, 18, 4),
('cota',              '1234',13, 7,18,14,12,10,13, 18, 4),
('omar',            '1234', 7, 3, 7,12,16,17, 6, 18, 4),
('santana',           '1234',10, 9,13,13,13,14,13, 18, 4),
('hector',  '1234', 1,11,11,11,18,13,13, 18, 4),
('edie',           '1234',14, 6,16,12,12,13,12, 18, 4),
('baby',      '1234',15,18,20,17,13,18,17, 18, 4),
('saul',            '1234',13,11,14,11,14,14,13, 18, 4),
('brenda',             '1234',17,13,20,12,14,11,16, 18, 4),
('samara',         '1234',14,15,13,12,15,16,12, 18, 4),
('daniel',      '1234', 9, 8,15,11,13,14,13, 18, 4),
('jorge',           '1234',17,12,14,17,19,18,14, 18, 4),
('mike',             '1234',15,16,17,18,18,13,11, 18, 4),
('luis',            '1234',11, 7,11,10,11,12, 6, 18, 4),
('anguiano.ae22@hotmail.com',       '1234',12,10,12,13,10,18,10, 18, 4),
('christian',       '1234',12,10,12,13,10,18,10, 18, 4),
('juancarlos',       '1234',12,10,12,13,10,18,10, 18, 4),
('diego',       '1234',12,10,12,13,10,18,10, 6, 2),
('xochilt',       '1234',12,10,12,13,10,18,10, 18, 4),
('cinthya',       '1234',12,10,12,13,10,18,10, 18, 4),
('claudia',       '1234',12,10,12,13,10,18,10, 25, 18),
('mario',       '1234',12,10,12,13,10,18,10, 25, 18),]

for e in estudiantes:
    User.objects.filter(username=e[0]).delete()
    u = User.objects.create_user(e[0],e[0], e[1])

    u.is_active = True
    u.save()
    lsu=LearningStyleInventory(visual=e[2],verbal=e[3],aural=e[4],physical=e[5],logical=e[6],
                          social=e[7], solitary=e[8], age=e[9], aca_lvl=e[10], user = u)

    lsu.save()
    ss = SimpleSequencing()
    ss.assignActivityTree(u,POO)


import os
#proot = UserLearningActivity.objects.filter(learning_activity = requested_activity.learning_activity.get_root() ,user = request.user )[0]
proot = LearningStyleInventory.objects.filter(user = User.objects.filter(username='edgar'))[0]
#.objects.filter(learning_activity = requested_activity.learning_activity.get_root() ,user = request.user )[0]


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "protoboard.settings")

##
##
## Assign Activity to both Users
##
##

#
# poo =UserLearningActivity.objects.filter(learning_activity__uri = "/activity/POO" ,user = User.objects.filter(username='paul')[0] )[0]
# ss = SimpleSequencing()


#
#
#a = ss.get_nav(poo)
#print ss.nav_to_xml(root=a)
#
#
#pre_j = UserLearningActivity.objects.filter(learning_activity__name = "Pretest" ,user = j )[0]
#s.set_current(pre_j)
#
#a = s.get_nav(root)
#print s.nav_to_xml(root=a)
#
#s.exit(pre_j, objective_measure = 0.20, objective_status = 'satisfied')
#
#a = s.get_nav(root)
#print s.nav_to_xml(root=a)

#
#s.set_current(j,remediation)
#s.exit(j,remediation, objective_measure = 0.80, objective_status = 'satisfied')
#a = s.get_nav(root)
#print s.nav_to_xml(root=a)
#
#
#s.set_current(j,general)
#s.exit(j,general, objective_measure = 0.80, objective_status = 'satisfied')
#a = s.get_nav(root)
#print s.nav_to_xml(root=a)


#root = UserLearningActivity.objects.filter(learning_activity__name = "Unit" ,user = j )[0]
#c = s.get_nav(root)
#print "-"*20
#print s.xml_children(root=c)
#
#s.set_current(j,general)
#s.exit(j, general, objective_measure = 0.80, objective_status = 'satisfied')
#root = UserLearningActivity.objects.filter(learning_activity__name = "Unit" ,user = j )[0]
#c = s.get_nav(root)
#print "-"*20
#print s.xml_children(root=c)


  