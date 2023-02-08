from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signin/', views.sign_in, name="sign_in"),
    path('signup/', views.sign_up, name="sign_up"),
    path('logout/', views.log_out, name="log_out"),
    path('videos/<str:cat>/<int:pos>', views.videos, name="videos"),
    path('articles/<str:cat>', views.articles, name="articles"),
    path('forget/', views.forget_password, name="forget_password"),
    path('demosurvey/', views.demo_survey, name="demo"),

]
