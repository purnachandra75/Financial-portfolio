from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.getexpensesPage,name='Expensespage'),
    path('createExpenses/',views.CreateExpenses.as_view(),name='createExpenses'),
    path('updateExpense/<int:id>',views.updateExpenses.as_view(),name='updateExpenses'),
    path('deleteExpense/<int:id>',views.deleteExpenses,name='deleteExpense'),
    path('expenseRegistration/',views.registerExpanses,name='regsExpanses'),
    path('createExpansecate/',views.createExpansescata,name='expanseCate'),
    path('updateExpansescate/<int:id>',views.updateExpanseCate,name='updateexpansescate'),
    path('deleteexpansescate/<int:id>',views.deleteExpansescate,name='deleteexpansescate')

]