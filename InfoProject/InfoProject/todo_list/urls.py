from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home,name="home"),
    path('delete/<list_id>',views.delete,name="delete"),
    path('update/<list_id>',views.update,name="update"),
]
