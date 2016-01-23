# -*- coding: utf-8 -*-
from django.shortcuts import render


def home(request):
    return render(request, 'common/home.html')


def faq(request):
    return render(request, 'common/faq.html')
