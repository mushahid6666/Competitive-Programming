__author__ = 'mushahidalam'

q1 = list()
q2 = list()


def push(x):
    global q1
    global q2
    q1.append(x)


def pop():
    global q1
    global q2
    while len(q1) != 1:
        q2.append(q1.pop(0))
    last = q1.pop()
    q1, q2 = q2, q1
    return last


def getTop():
    global q1
    global q2
    while len(q1) != 1:
        q2.append(q1.pop(0))
    Top = q1.pop()
    q2.append(Top)
    q1, q2 = q2, q1
    return Top


push(2)
push(3)
push(4)
push(5)
push(6)
push(7)
push(8)
push(9)
push(10)
push(11)
print pop()
print(getTop())
