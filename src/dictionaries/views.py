from django.shortcuts import render
from . import models
# from dictionaries.models import Authors, Countries, Genres, Publishers, Series

models_dict = {
    'Authors': models.Authors,
    'Countries': models.Countries.objects.all(),
    'Genres': models.Genres.objects.all(),
    'Publishers': models.Publishers.objects.all(),
    'Series': models.Series.objects.all()
}

# authors = models.Authors
# countries = models.Countries.objects.all()
# genres = models.Genres.objects.all()
# publishers = models.Publishers.objects.all()
# series = models.Series.objects.all()


# Create your views here.
# def main_page(request):
#     return render(request, template_name='main.html', context={'models_dict': models_dict})


def dict_view(request):
    context = {'object': models.Authors.objects.all()}
    return render(request, template_name='dict_view.html', context=context)

def dict_detail(request, pk):
    context = {'object': models.Authors.objects.get(pk=pk)}
    return render(request, template_name='dict_detail.html', context=context)

def dict_update(request, pk):
    context = {'object': models.Authors.objects.get(pk=pk)}
    return render(request, template_name='dict_detail.html', context=context)

def dict_delete(request, pk):
    context = {'object': models.Authors.objects.get(pk=pk)}
    return render(request, template_name='dict_detail.html', context=context)