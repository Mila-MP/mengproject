from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/login")
def create_component(request):
    return render(request, "landing_page/home.html")
