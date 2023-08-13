from django.urls import path
from blog import views
urlpatterns = [
    path('', views.home, name='index'),
    path('page1/', views.page1, name='page1'),
    path('page2/',views.page2,  name='page2')
]