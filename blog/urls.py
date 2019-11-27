
from django.urls import path
from django.conf import settings
from blog import views

urlpatterns = [

    path('',views.allblogs,name='allblogs'),

]
