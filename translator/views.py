from django.shortcuts import render, redirect, get_object_or_404
from .models import Inputs
from .forms import InputForm

from .algorithm1 import alg1
from .algorithm2 import alg2
from .algorithm3 import alg3

def cover(request):
    return render(request, 'translator/cover.html')

def translator(request, alg_id):
    alg_id=str(alg_id)
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            a='/translated'+alg_id
            return redirect(a)
    else:
        form = InputForm()
    return render(request, 'translator/translator'+alg_id+'.html',{'form':form})


def translated(request, alg_id):
    alg_id=str(alg_id)
    content = Inputs.objects.last()
    if alg_id=='1':
        output = alg1(str(content))
    if alg_id=='2':
        output = alg2(str(content))
    if alg_id=='3':
        output = alg3(str(content))

    return render(request, 'translator/translated'+alg_id+'.html', {'output':output})
