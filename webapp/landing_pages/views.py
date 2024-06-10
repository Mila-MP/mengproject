"""Views for the landing pages"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import InstrumentTypeModelForm, ActionForm
from .models import Workflows


@login_required(login_url="/login")
def home_page(request):
    """Returns the home page"""
    return render(request, "landing_pages/home.html")


@login_required(login_url="/login")
def instrument_type_page(request):
    if request.method == "POST":
        form = InstrumentTypeModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("instrument_type_page")
    else:
        form = InstrumentTypeModelForm()

    title = "Instrument Types"
    context = {"form": form, "title": title}

    return render(request, "landing_pages/instrument_type.html", context)


@login_required(login_url="/login")
def create_workflow_page(request):
    if request.method == "POST":
        form = ActionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("create_workflow_page")
    else:
        form = ActionForm()

    title = "Create Workflow"
    context = {"form": form, "title": title}

    return render(request, "landing_pages/create_workflow.html", context)


@login_required(login_url="/login")
def view_workflow_page(request):
    workflows = Workflows.objects.all()
    title = "Manage Workflows"
    context = {"workflows": workflows, "title": title}

    return render(request, "landing_pages/view_workflow.html", context)
