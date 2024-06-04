from articles.models import Category, Articles

class DataMixin:
    def get_user_context (self, **kwargs) :
        context = kwargs
        context ['cats'] = Category.objects.all()
        if 'cat_slug' in kwargs:
            context['cat'] = Category.objects.filter(slug=self.kwargs['cat_slug'])[0]
        if 'cat_selected' not in context:
            context ['cat_selected' ] = 0
        return context







