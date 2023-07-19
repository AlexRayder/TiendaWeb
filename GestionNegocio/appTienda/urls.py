from django.urls import path
from . import views

urlpatterns = [
    path('categoria', views.CategoriaList.as_view()),
    path('categoria/(?P<pk>[0-9]+)$', views.CategoriaDetail.as_view()),
    path('producto', views.ProductoList.as_view()),
    path('producto/(?P<pk>[0-9]+)$', views.ProductoDetail.as_view()),
]
