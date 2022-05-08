from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from django.contrib.auth.models import User


def login_page(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
        return render(request, 'user/login.html')


# def signup_page(request):
#     if request.user.is_authenticated:
#         return redirect('quizzes')
#     else:
#         form = CreateUserForm()
#         if request.method == 'POST':
#             form = CreateUserForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('login_page')
#         context = {
#             'form': form,
#         }
#         return render(request, 'user/signup.html', context)


def logout_user(request):
    logout(request)
    return redirect('login_page')


class RegisterUser(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login_page')
    template_name = 'user/signup.html'

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password == password2:
                User.objects.create_user(username, password=password)
                return redirect(self.success_url)
        return render(request, self.template_name, {"form": self.form_class})
