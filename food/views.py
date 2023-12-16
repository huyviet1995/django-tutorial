from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ItemForm
from .models import Item
from django.template import loader

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'food/index.html', context)

def item(req):
    return HttpResponse('This is an item view')

def detail(req, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(req, 'food/detail.html', context)

def create_item(req):
    form = ItemForm(req.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    context = {
        'form': form
    }
    return render(req, 'food/item-form.html', context)

def update_item(req, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(req.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    context = {
        'form': form,
        'item': item
    }
    return render(req, 'food/item-form.html', context)

def delete_item(req, item_id):
    item = Item.objects.get(pk=item_id)
    if req.method == 'POST':
        item.delete()
        return redirect('food:index')
    context = {
        'item': item
    }
    return render(req, 'food/item-delete.html', context)