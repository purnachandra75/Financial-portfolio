
from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.getbudgetPage,name='Budgetpage'),
    path('createbuget/',views.CreateBudget.as_view(),name='createbudget'),
    path('updatebudget/<int:id>',views.UpdateBudget.as_view(),name='updateBudget'),
    path('daletebuget/<int:id>/',views.deletebudget,name='deletebudget'),

    path('rigisterBudget/',views.registerBudget,name='registerBudget'),
    path('createBudget/',views.createBudget,name='createBudget'),
    path('editbudgetregi/<int:id>',views.updatebudgetrege,name='updatebudgetRege'),
    path('deletebudgetrege/<int:id>',views.deletebudgetrege,name='deletebudgetrege')
]
