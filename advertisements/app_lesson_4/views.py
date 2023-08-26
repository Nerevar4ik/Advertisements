from django.shortcuts import render
from django.http import HttpResponse

def less4(response):
    return HttpResponse('Домашка по 4 занятию')