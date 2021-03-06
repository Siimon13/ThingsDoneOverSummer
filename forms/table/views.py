from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import loader
from django.core.urlresolvers import reverse

from .models import Join
# Create your views here.

def index(request):
    apt_list = Join.objects
    order_by = request.GET.get('order_by', 'title')
    #print(order_by)
    apt_list = apt_list.order_by(order_by)
    paginator = Paginator(apt_list, 4)
    #print apt_list
    
    page = request.GET.get('page')
    try:
        apts = paginator.page(page)
    except PageNotAnInteger:
        apts = paginator.page(1)
    except EmptyPage:
        apts = paginator.page(paginator.num_pages)
    
    print 'unsorted'

    for j in apts.object_list:
        print j

    print 'sorted'

    for j in sorted(apts.object_list):
        print j

    return render(request, 'table/index.html', {'apts' : apts})

def input(request):
    j = Join(title = request.POST.get('title'), address = request.POST.get('address'))
    try:
        j.save()
        return index(request)
    except:
        return index(request)
