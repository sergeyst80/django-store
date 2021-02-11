from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from django.urls import reverse


# Create your views here.

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
    models.Authors.objects.get(pk=pk).delete()
    return render(request, template_name='dict_delete.html', context=context)


def dict_add(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        models.Authors.objects.create(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth)
        return HttpResponseRedirect(reverse('dict-view'))
    
    context = {} 
    return render(request, template_name='dict_add.html', context=context)


def dict_update(request, pk):
    author = models.Authors.objects.get(pk=pk)
    print(author.first_name, author.last_name, author.date_of_birth)
    if request.method == "POST":
        author.first_name = request.POST.get('first_name')
        author.last_name = request.POST.get('last_name')
        author.date_of_birth = request.POST.get('date_of_birth')
        author.save()
        return HttpResponseRedirect(reverse('dict-view'))
    
    context = {'author': author} 
    return render(request, template_name='dict_update.html', context=context)