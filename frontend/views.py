from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "frontend/index.html")

def detail(request, status_uuid):
    return render(request, "frontend/detail.html", {"status_uuid" : status_uuid})

def edit(request, status_uuid):
    return render(request, "frontend/edit.html", {"status_uuid" : status_uuid})