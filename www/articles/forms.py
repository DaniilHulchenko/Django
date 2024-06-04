from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class ArticlesForm(ModelForm):
    class Meta:
        model= Articles
        fields = '__all__'
        # fields = ['title', 'anons', 'description']
        widgets = {
            'title': TextInput(attrs={
                'placeholder' : "Enter name of article"
            }),
            'anons': TextInput(attrs={
                'placeholder': "Enter preview for article"
            }),
            'description': Textarea(attrs={
                'placeholder': "Enter description for article"
            }),
        }
