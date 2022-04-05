# menu driven program on binary file to perform basic operations such as
# inserting, reading, updating, seraching and deleteing.

import os
import pickle

# Accepting data
def insertRec():
    rollno=int(input("Enter roll number: ",))
    name=input("Enter Name: ",)
    marks=int(input("Enter Marks: ",))
    # creating the Dictionary
    rec={"Rollno":rollno,"Name":name,"Marks":marks}
    #writing the Dictionary
    f=open("student.dat","ab")
    pickle.dump(rec,f)
    print("Data Successfully dump")
    f.close()

# Reading the records
def readRec():
    f=open("student.dat","rb")
    while True:
        try:
            rec=pickle.load(f)
            print("Roll Num:",rec['Rollno'])
            print("Name:",rec['Name'])
            print("Marks:",rec['Marks'])
        except EOFError:
            break
    f.close()


#Seraching a record based on Rollno
def searchRoll(r):
    f=open("student.dat","rb")
    flag=False
    while True:
        try:
            rec=pickle.load(f)
            if rec['Rollno']==r:
                print("Roll Num:",rec['Rollno'])
                print("Name:",rec['Name'])
                print("Marks:",rec['Marks'])
                flag=True
        except EOFError:
            break
    if flag==False:
        print("No record Found")
    f.close()


# Marks Modification for Rollno
def updateMarks(r,m):
    f=open("student.dat","rb")
    reclst=[]
    while True:
        try:
            rec=pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()
    for i in range(len(reclst)):
        if reclst[i]['Rollno']==r:
            reclst[i]['Marks']=m
        f=open("student.dat","wb")
        for x in reclst:
            pickle.dump(x,f)
        f.close()


#Deleting a Record based on Roll no
def DeleteRec(r):
    f=open("student.dat","rb")
    reclst=[]
    while True:
        try:
            rec=pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()
    f=open("student.dat","wb")
    for x in reclst:
        if x['Rollno']==r:
            continue
        pickle.dump(x,f)
    f.close()

while True:
    print("MENU DRIVEN PROGRAM FOR STUDENT RECORD")
    print("1.Add Record")
    print("2.Display Records")
    print("3.Search Record")
    print("4.Update Record")
    print("5.Delete Record")
    print("6.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        insertRec()
    elif ch==2:
        readRec()
    elif ch==3:
        rollno=int(input("Enter rollno to search: "))
        searchRoll(rollno)
    elif ch==4:
        r=int(input("Enter a rollno:"))
        m=int(input("Enter new marks:"))
        updateMarks(r,m)
    elif ch==5:
        r=int(input("Enter a rollno to delete:"))
        DeleteRec(r)
    elif ch==6:
        break

    
    
    

