from django.urls import path

from . import views
app_name = 'quiz'

urlpatterns = [
    path('',views.Home,name='home'),
    path('python/',views.Python_Quiz,name='python'),
    path('django/',views.Django_Quiz,name='django'),
    path('angular/',views.Angular_Quiz,name='angular'),
    path('php/',views.PHP_Quiz,name='php'),
    path('java/',views.Java_Quiz,name='java'),
    path('javascript/',views.JavaScript_Quiz,name='javascript'),
    path('dot_net/',views.Dot_Net_Quiz,name='dot_net'),
    path('react/',views.React_Quiz,name='react'),
    path('nodejs/',views.Node_Js_Quiz,name='nodejs'),
]