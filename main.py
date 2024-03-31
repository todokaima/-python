class Point:
    pass

blank = Point()

print(blank)

blank.x = 3.0
blank.y = 4.0

print(blank.x)

f = blank.x

print(f)

print(type((blank.x)))

print('(' + str(blank.x) + " " + str(blank.y) + ')')
Distance_Squared = blank.x**2 + blank.y**2
print(Distance_Squared)

def Print_Point(p):
    print([p.x,p.y])


Print_Point(blank)

class Rectangle:
    pass

box = Rectangle()
box.width = 100.0
box.heigth = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def Find_Center(box):
    p = Point()
    p.x = box.corner.x + box.width/2.0
    p.y = box.corner.y - box.heigth/2.0
    return p

center = Find_Center(box)
Print_Point(center)

box.width = box.width + 50.0
box.heigth = box.heigth + 100.0

def Grow_Rectangle(box, dwidth, dheigth):
    box.width = box.width + dwidth
    box.heigth = box.heigth + dheigth

bob = Rectangle()
bob.width = 100.0
bob.heigth = 200.0
bob.corner = Point()
bob.corner.x = 0.0
bob.corner.y = 0.0
Grow_Rectangle(bob,50, 100)

import copy

p1 = Point()
p1.x = 3
p1.y = 4

p2 = copy.copy(p1)

b1 = Rectangle()
b1.width = 100
b1.heigth = 200
b1.corner = Point()
b1.corner.x = 0
b1.corner.x = 0

b2 = copy.deepcopy(b1)
print(b1.corner == b2.corner)

class Time:
    pass

time = Time
time.hours = 11
time.minute = 59
time.seconds = 30

def Add_Time(t1,t2):
    sumt = Time()
    sumt.hours = t1.hours + t2.hours
    sumt.minutes = t1.minutes + t2.minutes
    sumt.seconds = t1.seconds + t2.minutes

    if sumt.seconds >= 60:
        sumt.seconds = sumt.seconds - 60
        sumt.minutes = sumt.minutes + 1

    if sumt.minutes >= 60:
        sumt.minutes = sumt.minutes - 60
        sumt.hours = sumt.hour + 1

    return sumt

start = Time()
start.hours = 9
start.minutes = 10
start.seconds = 5
duration = Time()
duration.hours = 1
duration.minutes = 9
duration.seconds = 4
done = Add_Time(start, duration)

def Print_Time(time):
    print(time.hours, ':', time.minutes, ":", time.seconds)

Print_Time(done)

def increment(time, seconds):
    time.seconds = time.seconds + seconds
    if time.seconds >= 60:
        time.seconds = time.seconds - 60
        time.minutes = time.minutes + 1
    if time.minutes >= 60:
        time.minutes = time.minutes -60
        time.hours = time.hours = 1



def Converter_Seconds(t):
    minutes = t.hours*60 + t.minutes
    seconds = minutes*60 + t.minutes
    return seconds

def Make_Time(seconds):
    time = Time()
    time.hours = seconds //3600
    time.minutes = (seconds&3600) // 60
    time.seconds = seconds&60
    return time

def Add_Time_proper(t1,t2):
    seconds = Converter_Seconds(t1)+Converter_Seconds(t2)
    return Make_Time(seconds)

class Time():
    def printTime(self):
        print(str(self.hours) + ':' + str(self.minutes) + ':'+str(self.seconds))

    def Increment(self, seconds):
        self.seconds = self.seconds + seconds
        while self.seconds >= 60:
            self.seconds = self.seconds - 60
            self.minutes = self.minutes + 1

        while self.minutes >= 60:
            self.minutes = self.minutes - 60
            self.hours = self.hours + 1

t=Time()
t.minutes = 5
t.hours =10
t.seconds=39
t.printTime()
t.Increment(6)
t.printTime()

import os
def print_cube(num):
    print(os.getpid())
    print("Cube: {}".format(num*num*num))

def print_square(num):
    print(os.getpid())
    print("Square: {}".format(num*num))

print_cube(3)
print_square(8)


import multiprocessing

print(multiprocessing.cpu_count())
p1 = multiprocessing.Process(target = print_cube, args=(3,))
p2 = multiprocessing.Process(target = print_square, args=(4,))

p1.start()
p2.start()

p1.join()
p2.join()

print("done")

print(p1.is_alive())