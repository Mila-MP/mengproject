from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("instrument_type/", views.instrument_type_page, name="instrument_type_page"),
    path("create_workflow/", views.create_workflow_page, name="create_workflow_page"),
    path("view_workflow/", views.view_workflow_page, name="view_workflow_page"),
]
