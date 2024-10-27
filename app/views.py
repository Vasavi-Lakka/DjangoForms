from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse



def insertTopic(request):
    ETFO=TopicForm()#emptyTopicFormObject
    d={'ETFO':ETFO}
    
    if request.method=="POST":
        TFDO=TopicForm(request.POST)#TopicFormDataObject
        if TFDO.is_valid():
            tn=request.POST['tn']
            TO=Topic.objects.get_or_create(topic_name=tn)
            return HttpResponse('Topic is created')
        else:
            return HttpResponse('invalid data')


    return render(request, 'insertTopic.html', d)

def insertWebpage(request):
    #EWFO=WebpageForm()#emptyWebpageFormObject
    #d={'EWFO':EWFO}
    d={'EWFO':WebpageForm()}

    if request.method=="POST":
        WFDO=WebpageForm(request.POST)#WebpageFormDataObject
        if WFDO.is_valid():
            tn=request.POST['tn']
            TO=Topic.objects.get(topic_name=tn)
            n=request.POST['n']
            u=request.POST['u']
            WO=Webpage.objects.get_or_create(topic_name=TO, name=n, url=u)
            return HttpResponse('Webpage is created')
        else:
            return HttpResponse("Invalid data")


    return render(request, 'insertWebpage.html', d)

def insertAccess(request):
    EAFO=AccessForm()#emptyAccessFormObject
    d={'EAFO':EAFO}

    if request.method=="POST":
        AFDO=AccessForm(request.POST)#AccessFormDataObject
        if AFDO.is_valid():
            n=request.POST['n']
            WO=Webpage.objects.get(id=n)
            a=request.POST['a']
            da=request.POST['da']
            AO=AccessRecord.objects.get_or_create(name=WO, author=a, date=da)
            return HttpResponse("Access is created")
        else:
            return HttpResponse("invalid data")


    return render(request, 'insertAccess.html', d)