from django.shortcuts import render
from django.db.models import Q
from . models import table
from django.db import connection
# https://docs.djangoproject.com/en/5.0/ref/models/querysets/

def index(request):
    db=table.objects.all()
    context={
        'db':db
    }
    
    return render (request,'home.html',context)

def create(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        subj=request.POST['subj']
        qualification=request.POST['qual']
        location=request.POST['location']
        new=table(name=name,age=age,subj=subj,qualification=qualification,location=location)
        new.save()

    return render (request,'create.html')

def filter(request):
    # pass
    # Get object is used for single values
    #filter is for the whole table
    #.union() removes duplicate values

    # a=table.objects.filter(age__lte=15)
    # a=table.objects.filter(name__startswith='S')
    # a=table.objects.filter(name__icontains='a')
    # a=table.objects.exclude(age=14)
    # a=table.objects.filter(name__icontains='Saanu')
    # a=table.objects.filter(Q(name__icontains='Saanu')| Q (name__icontains='Nomi'))
    # a=table.objects.filter(Q(name__icontains='S') & Q (age__gte=20))
    # a=table.objects.exclude(age=21)
    # a=table.objects.filter(age=14)
    # a=table.objects.filter(~Q(age=14))
    a=table.objects.filter(location="Mumbai").only ('name')
    # a=table.objects.raw("SELECT * FROM core_table") #appname_model
    # a=table.objects.raw("SELECT * FROM core_table Where age=14") #appname_model
    # a=table.objects.raw("SELECT * FROM core_table")[:2]
    
    
    context={
        'a':a
    }
    # print(a)
    print(a.query)
    # print(connection.queries)

    return render(request,'filter.html',context)


# def filter(request):
    # pass
    # cursor=connection.cursor()
    # cursor.execute(" SELECT count(*) FROM core_table")
    # r=cursor.fetchone() #one only
    # cursor.execute(" SELECT * FROM core_table")
    # cursor.execute(" SELECT * FROM core_table WHERE age<21")
    # r=cursor.fetchall() #all
    # r=dictfetchall(cursor) #dict function
    # print(r)
    # print(connection.queries)
    # return render(request,'filter.html',{'a':r})
