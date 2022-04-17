from django.shortcuts import render
import mysql.connector as sql
un=0
name=''
em=''
mno=0
city=''
street=''
pin=0
pwd=''
cpwd=''
age=0
exp=0
dep=''
sr=0
ld=''

# Create your views here.

def RegisterClientAction(request):

    global un,name,em,mno,city,street,pin,pwd,cpwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Project2OOPs!",database='courtroomdatabase')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Username":
               un=value
            if key=="Name":
                name=value
            if key=="Email":
                em=value
            if key=="ContactNo":   
                mno=value
            if key=="City":
                city=value
            if key=="Street":
                street=value
            if key=="Pincode":
                pin=value
            if key=="Password":
                pwd=value
            if key=="ConfPassword":
                cpwd=value
            if key=="DepName":
                dep=value

        if(pwd==cpwd):
            c="insert into clienttable values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(un,name,em,mno,city,street,pin,0,1,pwd)
            cursor.execute(c)
            c="insert into client_dependentstable values('{}','{}')".format(un,dep)
            cursor.execute(c)
            m.commit()
            return render(request,'TestDashboard.html')
        else :
            return render(request,'RegisterRetryClient.html')

    return render(request,'RegisterClient.html')

def RegisterJudgeAction(request):

    global un,name,age,em,mno,exp,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Project2OOPs!",database='courtroomdatabase')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Username":
               un=value
            if key=="Name":
                name=value
            if key=="Email":
                em=value
            if key=="ContactNo":   
                mno=value
            if key=="Password":
                pwd=value
            if key=="ConfPassword":
                cpwd=value
            if key=="Age":
                age=value
            if key=="YearsOfExp":
                exp=value

        if(pwd==cpwd):
            c="insert into judgetable values('{}','{}','{}','{}','{}','{}','{}')".format(un,name,age,em,mno,exp,pwd)
            cursor.execute(c)
            m.commit()
            return render(request,'TestDashboard.html')
        else :
            return render(request,'RegisterRetryJudge.html')          

    return render(request,'RegisterJudge.html')  

def RegisterLawyerAction(request):

    global un,name,age,em,mno,exp,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Project2OOPs!",database='courtroomdatabase')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Username":
               un=value
            if key=="Name":
                name=value
            if key=="Email":
                em=value
            if key=="ContactNo":   
                mno=value
            if key=="Password":
                pwd=value
            if key=="ConfPassword":
                cpwd=value
            if key=="Age":
                age=value
            if key=="WorkExperience":
                exp=value
            if key=="SuccessRate":
                sr=value
            if key=="LawDomain":
                ld=value

        if(pwd==cpwd):
            c="insert into lawyertable values('{}','{}','{}','{}','{}','{}','{}')".format(un,name,em,mno,exp,sr,pwd)
            cursor.execute(c)
            c="insert into lawyer_domain values('{}','{}')".format(un,ld)
            cursor.execute(c)
            m.commit()
            return render(request,'TestDashboard.html')
        else :
            return render(request,'RegisterRetryLawyer.html')

    return render(request,'RegisterLawyer.html')