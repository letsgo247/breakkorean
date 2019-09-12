from django.shortcuts import render
from .algorithm1 import alg1
from .algorithm2 import alg2
from .algorithm3 import alg3

def translator(request):
    output = alg1("훈민정음")
    return render(request, 'translator/translator.html', {'output':output})


# Create your views here.
