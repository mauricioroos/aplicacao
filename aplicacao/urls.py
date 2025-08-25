from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name ="url_index"),
    path('produtos', views.produtos, name ="url_produtos"),
    path('cad_produto',views.cad_produto, name="url_cad_produto"),
  #  path('criar_produto',views.criar, name="url_criar_produto"),#
]