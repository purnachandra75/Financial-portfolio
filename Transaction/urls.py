
from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.getTransaction,name='Transaction'),
    path('createtransaction/<str:tran>',views.CreateTransaction.as_view(),name='CreateTransaction'),
    path('updateTransaction/<int:id>/<str:tran>',views.UpdateTransaction.as_view(),name='UpdateTransaction'),
    path('deleteTransaction/<int:id>/',views.deleteTransaction,name='deleteTransaction')


]
