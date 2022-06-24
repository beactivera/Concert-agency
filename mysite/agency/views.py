from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Hello, world. You're at the agency index.")
    return render(request, 'agency/index.html')


def profile(request):
    # return HttpResponse("Your profile is here.")
    return render(request, 'agency/profile.html')


def festivals(request):
    # return HttpResponse("Your festival is here.")
    return render(request, 'agency/festivals.html')


def tickets(request):
    # return HttpResponse("Your tickets are here.")
    return render(request, 'agency/tickets.html')


def genres(request):
    # return HttpResponse("Your genres are here.")
    return render(request, 'agency/genres.html')


def instrumets(request):
    return HttpResponse("Your instruments are here.")


def concerts(request):
    return HttpResponse("Your concerts are here.")


def artists(request):
    return HttpResponse("Your artists are here.")