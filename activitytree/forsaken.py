__author__ = 'frank'
import time
import redis
w=redis.Redis("11.0.0.19")
a=w.get("1")
b=a.split("\n")
print a
d=[]
b.remove("")
print b
print len(b)
engage=0
for x in range(len(b)):
        c=b[x]
        d.append(c.split(":"))

print len(d)
if d[0][1]==" Yes":
    print "conte"
    happy=+1
if d[1][1]==" Yes":
    print "conte"
    engage=+1
if d[2][1]==" Yes":
    print "conte"
    away=+1

print "entre", engage
print d[1][1]






while actividad==q.get("ana"):

        time.sleep(2) # delays for 1 seconds
        a=w.get("1")

        b=a.split("\n")
        print a
        print b
        b.remove("")

        for x in range(len(b)):
            c=b[x]
            d.append(c.split(":"))
        if d[0][1]==" Yes":
            print "conte"
            happy=+1
        if d[1][1]==" Yes":
            print "conte"
            engage=+1
        if d[2][1]==" Yes":
            print "conte"
            away=+1

        actividad=q.get("ana")

        print "entre", actividad, engage
