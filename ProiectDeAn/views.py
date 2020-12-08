from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'client/home.html'


class Login(TemplateView):

    @staticmethod
    def auth(request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and not user.is_authenticated:
            login(request, user)
        return redirect('/')
