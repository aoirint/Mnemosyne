import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import transaction

from filament.forms import *
from filament.models import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        posttype = request.POST['type']
        if posttype == 'delete_filament':
            filament_id = request.POST['filament_id']

            filament = Filament.objects.get(id=filament_id)
            filament.delete()

    filaments = Filament.objects.all().order_by('-created_at')

    return render(request, 'filament/index.html', {
        'title': 'フィラメント | Mnemosyne',
        'filaments': filaments,
    })

def new(request):
    form = FilamentForm(request.POST, request.FILES)

    if request.method == 'POST':
        if form.is_valid():
            filament = update_filament(form)
            return redirect('filament:edit', id=filament.id)

    return render(request, 'filament/edit.html', {
        'title': '新しいフィラメントの登録 | Mnemosyne',
        'form': form,
    })

def edit(request, id):
    filament = Filament.objects.get(id=id)
    form = FilamentForm(request.POST, request.FILES)

    if request.method == 'POST':
        if form.is_valid():
            update_filament(form, filament=filament)
            return redirect('filament:index')

    form = FilamentForm()
    form.fields['material'].initial = filament.material
    form.fields['amount'].initial = filament.amount
    form.fields['price'].initial = filament.price
    form.fields['shop'].initial = filament.shop
    form.fields['url'].initial = filament.url
    form.fields['owner'].initial = filament.owner
    form.fields['name'].initial = filament.name

    return render(request, 'filament/edit.html', {
        'title': '登録済みフィラメントの編集 | Mnemosyne',
        'form': form,
        'filament': filament,
    })

def info(request, id):
    filament = Filament.objects.get(id=id)
    data = {
        'name': filament.name,
        'price': filament.price,
        'amount': filament.amount,
    }

    return HttpResponse(json.dumps(data), content_type='application/json')


# Edit Models
def update_filament(form, filament=None):
    if filament is None:
        filament = Filament()

    filament.material = form.cleaned_data['material']
    filament.amount = form.cleaned_data['amount']
    filament.price = form.cleaned_data['price']
    filament.shop = form.cleaned_data['shop']
    filament.url = form.cleaned_data['url']
    filament.owner = form.cleaned_data['owner']
    filament.name = form.cleaned_data['name']

    image = form.cleaned_data['image']
    if image:
        filament.image_file = image

    filament.save()

    return filament
