from django.shortcuts import render

# Create your views here.
def login_views(request):
    template_name = "authentication-login.html"
    
    return render(request,template_name)