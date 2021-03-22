from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.db.models import Q

from mainapp import models, forms
from users import utils as users_utils
from references import models as refs_models


# Create your views here.
class HomePage(generic.TemplateView):
    model = models.BookCard
    template_name = "mainapp/homepage.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = self.model.objects.all().order_by('-pk')[0:5]
        hirated_books = self.model.objects.all().order_by('-rating')[0:5]
        context['objects'] = books
        context['hirated_books'] = hirated_books
        return context


class BooksCatalog(generic.ListView):
    paginate_by = 12
    model = models.BookCard
    ordering = ['-pk']
    template_name = "mainapp/books_catalog.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # new_books = self.model.objects.all().order_by('-pk')[0:5]
        # context['new_books'] = new_books
        # context['hirated_books'] = hirated_books
        search =  self.request.GET.get('search')
        context['search_form'] = forms.CatalogSearchForm(
            initial={
                'search': search
            }
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')

        if search:
            authors = refs_models.Authors.objects.filter(name__icontains=search)

            if search:
                queryset = queryset.filter(
                    Q(authors__in=authors) | 
                    Q(isbn__icontains=search) |
                    Q(name__icontains=search)
                )

        return queryset


class DetailBookView(generic.DetailView):
    model = models.BookCard
    template_name = "mainapp/detail_book.html"


class SendBookCommentView(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        comment = self.request.POST.get('comment')
        pk = self.request.POST.get('pk')
        rating = self.request.POST.get('rating')

        if comment and pk:
            bookcard = models.BookCard.objects.filter(pk=pk).first()
            comments = bookcard.comments.all()
            sum = 0.0
            count = 0

            if comments and rating:
                
                for item in comments:
                    if item.rating:
                        sum += item.rating
                        count += 1

                bookcard.rating = (int(rating) + sum) / (count + 1)
                bookcard.save()
            
            comments = models.BookComments.objects.create(
                bookcard=models.BookCard.objects.filter(pk=pk).first(),
                user=users_utils.get_current_customer(self),
                comment=comment,
                rating = rating
            )
            comments.save()
        
        return reverse('detail-book', args=[pk])