from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import transaction

from print3d.forms import *
from filament.models import *
from print3d.models import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        posttype = request.POST['type']
        if posttype == 'delete_print3d':
            print3d_id = request.POST['print3d_id']

            print3d = Print3d.objects.get(id=print3d_id)
            print3d.delete()

    print3ds = Print3d.objects.all().order_by('-created_at')

    return render(request, 'print3d/index.html', {
        'title': '3Dプリント | Mnemosyne',
        'print3ds': print3ds,
    })

def new(request):
    form = Print3dForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            print3d = update_print3d(form)
            return redirect('print3d:index')

    return render(request, 'print3d/edit.html', {
        'title': '新しい3Dプリントの登録 | Mnemosyne',
        'form': form,
    })

def edit(request, id):
    print3d = Print3d.objects.get(id=id)
    form = Print3dForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            update_print3d(form, print3d=print3d)
            return redirect('print3d:index')

    form = Print3dForm()
    form.fields['filament'].initial = print3d.id
    form.fields['amount'].initial = print3d.amount
    form.fields['user'].initial = print3d.user
    form.fields['memo'].initial = print3d.memo

    return render(request, 'print3d/edit.html', {
        'title': '登録済み3Dプリントの編集 | Mnemosyne',
        'form': form,
        'print3d': print3d,
    })

def update_print3d(form, print3d=None):
    if print3d is None:
        print3d = Print3d()

    filament_id = form.cleaned_data['filament']
    print3d.filament = Filament.objects.get(id=filament_id)

    print3d.user = form.cleaned_data['user']
    print3d.amount = form.cleaned_data['amount']
    print3d.memo = form.cleaned_data['memo']

    image = form.cleaned_data['image']
    if image:
        print3d.image_file = image

    print3d.save()
    return print3d
