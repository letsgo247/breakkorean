from django.shortcuts import render, redirect, get_object_or_404
from .models import Inputs
from .forms import InputForm

from .algorithm1 import alg1
from .algorithm2 import alg2
from .algorithm3 import alg3

def cover(request):
    return render(request, 'translator/cover.html')

def translator1(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('translated1')
    else:
        form = InputForm()
    return render(request, 'translator/translator1.html',{'form':form})


def translator2(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('translated2')
    else:
        form = InputForm()
    return render(request, 'translator/translator2.html',{'form':form})


def translator3(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('translated3')
    else:
        form = InputForm()
    return render(request, 'translator/translator3.html',{'form':form})


def translated1(request):
    content = Inputs.objects.last()
    output = alg1(str(content))
    return render(request, 'translator/translated1.html', {'output':output})


def translated2(request):
    content = Inputs.objects.last()
    output = alg2(str(content))
    return render(request, 'translator/translated2.html', {'output':output})


def translated3(request):
    content = Inputs.objects.last()
    output = alg3(str(content))
    print(output)
    return render(request, 'translator/translated3.html', {'output':output})
