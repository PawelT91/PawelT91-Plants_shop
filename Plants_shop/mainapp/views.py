from django.shortcuts import render, get_object_or_404
from .models import CactusSubfamily, CactusGenus, ViewCactus


def main(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def error(request):
    return render(request, 'error.html')

def cactus_plants(request):
    CactusSubfamils = CactusSubfamily.objects.all()
    return render(request, 'cactus_plants.html', {'CactusSubfamils': CactusSubfamils})


def cactus_genus(request, id):
    Subfamilys = get_object_or_404(CactusSubfamily, id=id)
    Genus = CactusGenus.objects.filter(subfamily_id=id)
    return render(request, 'cactus_genus.html', {'Subfamilys': Subfamilys, 'Genus': Genus})


def cactus_view(request, id):
    Genus = get_object_or_404(CactusGenus, id=id)
    Cactus = ViewCactus.objects.filter(genus_id=id)
    return render(request, 'cactus_view.html', {'Genus': Genus, 'Cactus': Cactus})

