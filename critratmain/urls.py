from django.urls import path

from . import views

app_name = 'critratmain'
urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('critrats/', views.critRats, name='critrats')
]