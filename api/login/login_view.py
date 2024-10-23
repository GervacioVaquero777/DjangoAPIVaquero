from django.shortcuts import render

# Create your views here.
def login_views(request):
    template_name = "login.html"
    
    return render(request,template_name)

# Create your views here.
def registro_views(request):
    template_name = "registro.html"
    
    return render(request,template_name)

# Create your views here.
def recuperar_views(request):
    template_name = "recuperar.html"
    
    return render(request,template_name)