from django.urls import path, include
from . import views


urlpatterns = [
    path('image/convert-bw/', views.convert_black_and_white),
    path('image/convert-bw/<uuid:id>', views.convert_black_and_white),
]
