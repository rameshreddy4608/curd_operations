from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *


def insert_topic(request):
    tn=input('enter topic name: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('sucessfully inserted data into topic')

def insert_webpage(request):
    tn=input('enter a topicname: ')
    na=input('enter a name: ')
    ur=input('enter url: ')
    email=input('enter email: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=email)[0]
    WO.save()
    return HttpResponse('sucessfully inserted data into webpage')

def insert_accessrecords(request):
    tn=input('enter topic: ')
    na=input('enter a name: ')
    aut=input('enter author name: ')
    ur=input('enter url: ')
    date=input('enter date: ')
    email=input('enter email: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=email)[0]
    WO.save()
    AO=Accessrecords.objects.get_or_create(name=WO,author=aut,date=date)[0]
    AO.save()
    return HttpResponse('sucessfully inserted data into accessrecords')




def insert_topic(request):
    LOT=Topic.objects.all()
    d={'ram':LOT}
    return render(request,'insert_topic.html',context=d)

def insert_webpage(request):
    LOW=Webpage.objects.all()
    d={'ramesh':LOW}
    return render(request,'insert_webpage.html',context=d)

def insert_accessrecords(request):
    LOA=Accessrecords.objects.all()
    d={'rupesh':LOA}
    return render(request,'insert_accessrecords.html',context=d)