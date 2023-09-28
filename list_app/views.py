from django.shortcuts import render, redirect
from .models import Item


# Create your views here.

def index(request, *args, **kwargs):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})


def add_item(request, *args, **kwargs):
    if request.method == 'POST':
        title = request.POST['title']
        item = Item(title=title)
        item.save()
    return redirect('index')


def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect('index')
