from django.shortcuts import render, redirect
from django.template.response import TemplateResponse

# Create your views here.

from . models import Articles, Category
from . forms import ArticlesForm
from django.views.generic import DetailView, ListView



# test
def layout(request):
    data={
        'cat_selected':0,
        'cat': Category.objects.all()
    }
    print(data['cat'])
    return render(request, 'main/layout.html', data)


def articles_pages(request, pk):
    items = Articles.objects.all()
    data={
        'items': items,
        'page_num':pk,
        'cat_selected':0,
    }
    return render(request, 'articles/layout_articles_pages.html', data)

class Articles_Details(DetailView):
    model = Articles
    template_name = 'articles/layout_articles_details.html'
    context_object_name = 'art'
    slug_url_kwarg = 'art_slug'

    extra_context = None
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = Articles.objects.filter(slug=self.kwargs['art_slug'])[0].cat_id
        return context





# def show_category(request, pk):
#     data={
#         'items': Articles.objects.filter(cat_id = pk),
#         # 'cat': Category.objects.all(),
#         'cat_selected': pk,
#         'cat': Category.objects.filter(id=pk),
#     }
#     return render(request, 'articles/layout_articles_pages.html', data)
# def show_category(request, cat_slug):
#     data={
#         'items': Articles.objects.filter(cat__slug = cat_slug),
#         # 'items': Articles.objects.filter(cat_id=Category.objects.filter(slug=slug)[0].id),
#         'cat_selected': Category.objects.filter(slug=cat_slug)[0].id,
#         'cat': Category.objects.filter(slug=cat_slug),
#     }
#     return render(request, 'articles/layout_articles_pages.html', data)

# from main.utils import DataMixin
# class Show_Category_Art(DataMixin, ListView):
class Show_Category_Art(ListView):
    paginate_by = 6
    model = Articles
    template_name = 'articles/layout_articles_pages.html'
    context_object_name = 'items'
    allow_empty = False

    def get_queryset(self):
        # print(Articles.objects.filter(cat__slug = self.kwargs['slug']))
        if self.kwargs['cat_slug'] == 'all':
            return Articles.objects.all().select_related('cat')
        else:
            return Articles.objects.filter(cat__slug = self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs['cat_slug'] != 'all':
            context['cat'] =  Category.objects.filter(slug=self.kwargs['cat_slug'])
            context['cat_selected'] = Category.objects.filter(slug=self.kwargs['cat_slug'])[0].id
        else:
            context['cat'] = [{'name': 'All'}]
            context['cat_selected'] = 0

        return context

        # return self.get_user_context(cat_selected=Category.objects.filter(slug=self.kwargs['cat_slug'])[0].id,cat=)




def create(request):
    error=''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Something wrong !!!'
    form = ArticlesForm()
    data={
        'form' : form,
        'error' : error
    }
    return render(request, 'articles/create.html', data)