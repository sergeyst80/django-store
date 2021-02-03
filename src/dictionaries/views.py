from django.shortcuts import render
from dictionaries.models import Authors, Countries, Genres, Publishers, Series


authors = Authors.objects.all()
countries = Countries.objects.all()
genres = Genres.objects.all()
publishers = Publishers.objects.all()
series = Series.objects.all()

# Create your views here.
def dicts_page(request):
    context = {
        'authors': authors,
        'countries': countries,
        'genres': genres,
        'publishers': publishers,
        'series': series
        }
    return render(request, template_name='main.html', context=context)
