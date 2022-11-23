from django.urls import path
from cnab import views

urlpatterns = [
    path("cnab/", views.ListCreateCnabView.as_view()),
]
