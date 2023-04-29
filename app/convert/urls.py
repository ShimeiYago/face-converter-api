from django.urls import path
from convert import apis

urlpatterns = [
    path('convert/', apis.ConvertView.as_view(), name="convert"),
]
