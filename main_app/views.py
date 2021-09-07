from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse('<h1> about the Ghpstcllector<h1>')

def ghost_index(request):
    return render(request, 'ghost/index.html', {'ghost': ghost})

def ghosts_detail(request, ghost_id):
    ghost = Ghost.objects.get(id=ghost_id)
    return render(request, 'ghost/detail.html', {'ghost':ghost})

class Ghost:
    def __init__(self, name, decription, age):
        self.name = name
        self.decription = decription
        self.age = age

ghost =[
    Ghost('Danny Phataom', 'Going Ghostttt', 16),
    Ghost('Casper', "Your friendly GHost", 100000)

]