from django.shortcuts import render
from django.http import HttpResponse

def index_view(rquest):
    return HttpResponse("<h1>Home page</h1>")
def about_view(rquest):
    return HttpResponse("<h1>about page</h1>")
def contact_view(rquest):
    return HttpResponse("<h1>contact page</h1>")