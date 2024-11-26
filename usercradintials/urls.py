from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.loginpage,name='loginpage'),
    path('registration/',views.Registration.as_view(),name='registration'),
    path('forgotpass/',views.Forgotpass.as_view(),name='forgotpass'),
    path('validpass/<str:email>',views.Validmail.as_view(),name='validpass'),
    path('changepass/<str:email>',views.Changepass.as_view(),name='changepass'),
    path('logout/',views.logout,name='logout')
]