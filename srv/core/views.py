from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import logout
from friendlyname.random_words import random_username


def logo_page(request):
    if request.user.is_authenticated():
        return render(request, "testpage.html")
    else:
        return render(request, "landing.html")


def prompt_calpoly(request):
    return render(request, "prompt-calpoly.html", {"user": request.user})


def fourohfour(request):
    return render(request, "404.html")


def test_page(request):
    return render(request, "testpage.html")


def gen_username(request):
    username = random_username("adjectives", "colors", "nouns")
    if request.GET.get('f', '') == 'no':
        return render(request, "gen-username.html", {
            "username": username,
            "first": False
        })
    return render(request, "gen-username.html", {
        "username": username,
        "first": True
    })


def select_class(request):
    return render(request, "select-class.html")


def denied(request):
    return render(request, "denied.html")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
