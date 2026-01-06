from django.shortcuts import render
from django.http import HttpResponse
from .models import Item


# Create your views here.


def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list':item_list
    }
    # return HttpResponse(item_list)
    return render(request,"myapp/index.html", context)


def detail(request,id):
    item = Item.objects.get(id=id)
    context = {
        'item':item
    }
    # return HttpResponse(f'This is the detail view for an item with id as {item}')
    return render(request,"myapp/detail.html",context)



def item(request):
    return HttpResponse('<h1>This is an item!</h1>')