from django.urls import path
from . import views


urlpatterns=[
    path('',views.getIncomepage,name='Incomepage'),
    path('registerIncome/',views.registerIncome,name='registerIncome'),
    path('editincomecate/<int:id>',views.updateIncomecate,name='editcategory'),
    path('delecteincomecate/<int:id>',views.deletecate,name='deletecategory'),
    path('createIncomecata/',views.createIncomecate,name='Incomecata'),
    path('createincomesource/',views.CreateIncomeSource.as_view(),name='createincome'),
    path('updateIncome/<int:id>/',views.UpdateIncome.as_view(),name='updateIncome'),
    path('deleteIncome/<int:id>/',views.deleteIncome,name='deleteincome')
]