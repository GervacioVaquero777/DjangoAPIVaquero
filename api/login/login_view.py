from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def login_views(request):
    template_name = "login.html"
    
    if request.user.is_authenticated:
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
    return render(request,template_name)

# view for forgot the assword
def recuperar_views(request):
    template_name = "recuperar.html"
    return render(request,template_name)

# View for logout
def logout_view(request):
    logout(request)
    return redirect('login')