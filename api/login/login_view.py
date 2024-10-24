from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


# Create your views here.
def login_views(request):
    template_name = "login.html"
    
    if request.user.is_authenticated and request.user.is_active:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, template_name, {'error': 'Credenciales invalidas'})
    return render(request,template_name)

# view for registrer
def registro_views(request):
    template_name = "registro.html"
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, "The passwords do not match.")
            return render(request, template_name)

        if User.objects.filter(username=username).exists():
            messages.error(request, "The username is already in use.")
            return render(request, template_name)
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "The email is already in use")
            return render(request, template_name)

        user = User(
            username=username, 
            email=email, 
            password=make_password(password),
            is_active = 1
            )
        user.save()
        messages.success(request, "Account successfully created.")
    return render(request,template_name)

# view for forgot the assword
def recuperar_views(request):
    template_name = "recuperar.html"
    return render(request,template_name)

# View for logout
def logout_view(request):
    logout(request)
    return redirect('login')