from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def asignar(request):
    return HttpResponse("Diagnóstico - Asignar: No implementado aún.")

def evaluar(request):
    return HttpResponse("Diagnóstico - Evaluar: No implementado aún.")

def listado(request):
    return HttpResponse("Diagnóstico - Listado: No implementado aún.")

def diagnostico(request):
    return HttpResponseRedirect('/login/')
