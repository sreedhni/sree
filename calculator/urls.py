"""
URL configuration for calculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path
from operations.views import HelloWorldView,GoodMorningView,GoodAfterNoonView,AdditionView,SubstractionView,MultiplicationView,CubeView,DivisionView,FactorialView,IndexView,OperationView,SignUpView,ContactView,BmiView,SalaryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/',HelloWorldView.as_view(),name="helloworld"),
    path("goodmorning/",GoodMorningView.as_view(),name="goodmorning"),
    path("goodafternoon/",GoodAfterNoonView.as_view(),name="goodafternoon"),
    path("addition/",AdditionView.as_view(),name="addition"),
    path("sub/",SubstractionView.as_view(),name="substraction"),
    path("multi/",MultiplicationView.as_view(),name="multiplication"),
    path("cube/",CubeView.as_view(),name="cube"),
    path("div/",DivisionView.as_view(),name="division"),
    path("fac/",FactorialView.as_view(),name="factorial"),
    path("operation/",OperationView.as_view(),name="operations"),
    path("signup/",SignUpView.as_view()),
    path("contact/",ContactView.as_view()),
    path("bmi/",BmiView.as_view(),name="bmi"),
    path("salary/",SalaryView.as_view()),
    path("",IndexView.as_view(),name="index")
]