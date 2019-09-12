from django.shortcuts import render, redirect, get_object_or_404
from .models import Input
from .forms import InputForm

from .algorithm1 import alg1
from .algorithm2 import alg2
from .algorithm3 import alg3

def translator(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('translated')
    else:
        form = InputForm()
    return render(request, 'translator/translator.html',{'form':form})


def translated(request):
    content = Input.objects.last()
    print(content)
    output = alg1(str(content))
    return render(request, 'translator/translated.html', {'output':output})



# Create your views here.
