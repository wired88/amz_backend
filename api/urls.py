from django.urls import path
from .views import *

app_name = "api"
urlpatterns = [
    path("contact/", ContactAPIView.as_view()),
    path("create-objects/", CreateObjectsAPIView.as_view()),
    path("html-css-live-viewer/", ComponentCreateTextRequestView.as_view()),
]


