from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse

# from www.articles.models import Category
from articles.models import Articles, Category
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from main.forms import RegisterUserForm, LoginUserForm

from main.forms import LoginUserForm

from main.forms import EditAccountDetails

# Create your views here.

menu =[
    {'title': 'Main', 'url_name': 'home'},
    {'title': 'About us', 'url_name': 'about'},
    {'title': 'Feedback', 'url_name': 'feedback'},
    {'title' : 'hello', 'url_name': 'home'},
]


def index(request):
    # return render(request, 'main/index.html', {'menu': menu})

    data={
        # 'cat': Category.objects.all(),
        # 'cat_selected': 0,
    }
    # print(data['cat'])
    # print(render(request, 'main/index.html', data))
    return render(request, 'main/index.html', data);

def about(request):
    return render(request, 'main/about.html')

def feedback(request):
    return render(request, 'main/feedback.html')
    # HttpResponse("")
    # return render(request, 'main/layout.html', context=)

def location(request):
    return render(request, 'main/location.html')

class Register(CreateView):
    # form_class = UserCreationForm
    form_class = RegisterUserForm
    template_name = 'main/reg.html'
    success_url = reverse_lazy('home')


from django.shortcuts import render, redirect
# def registration(request):
#     error=''
#     if request.method == "POST":
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         else:
#             error = 'Something wrong !!!'
#     return render(request, 'main/reg.html')
class Login(LoginView):
    form_class = LoginUserForm
    template_name='main/reg.html'


from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect('home')

class Account(DetailView):
    template_name = 'main/account.html'
    model = User
    # context_object_name = 'user_form'
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    # def get_queryset(self):
    #     return None
class Edit_Account(CreateView):
    # form_class=UserChangeForm
    form_class=EditAccountDetails
    template_name = 'main/edit_account.html'
    context_object_name = 'user_edit'

