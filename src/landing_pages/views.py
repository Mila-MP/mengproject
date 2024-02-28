"""Views for the landing pages"""

from django.shortcuts import render


def home_page(request):
    """Returns the home page"""
    return render(request, "landing_pages/home.html")
