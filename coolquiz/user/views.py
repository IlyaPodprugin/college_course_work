from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import RegisterForm
from main.models import Take


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


def view_profile(request, username):
    if not request.user.is_authenticated:
        return redirect('login_page')
    takes = Take.objects.filter(user_id=request.user.id)
    print(len(takes))
    highest_score = takes.order_by('-percent_efficiency')[0]
    context = {
        'user': request.user,
        'passed_quizzes_count': len(takes),
        'highest_percent_efficiency': highest_score.percent_efficiency,
    }
    return render(request, 'user/userprofile.html', context)
