import csv

def primeruso():
    data=[[a,b]]
    with open('users.csv','w') as csvfile:
        writer=csv.writer(csvfile,delimiter=",")
        writer.writerow(["usuario","contraseña"])
        writer.writerows(data)

def agregar():
    data=[[a,b]]
    with open("users.csv","a") as csvfile:
        writer=csv.writer(csvfile,delimiter=",")
        writer.writerows(data)


def len():
    with open("C:/Users/RAMSES/Desktop/hello_world_app/app/templates/users.csv","r") as a:
        zz=csv.reader(a)
        for row in zz:
            print(row,end='')

a="pelodelano"
b="pelodelescroto"

len()