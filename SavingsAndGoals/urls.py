
from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.getSaveandGolepage,name='SavingeandGoal'),
    path('createSavingeandGoal/',views.CreateSavingsandGoals.as_view(),name='createSavingsandGoals'),
    path('updateSaveingsAndGoals/<int:id>',views.Updatesavingsandgoals.as_view(),name='Updatesavingsandgoals'),
    path('deleteSavingsandgoals/<int:id>/',views.deleteSavingsandgoals,name='deleteSavingsandgoals'),


    path('registersavingsandGoals/',views.registerSaveingsandGoals,name='regiSavingsAndGoals'),
    path('createSandGregi/',views.CreategoalsRegister.as_view(),name='createSandGregi'),
    path('updateSandGregi/<int:id>',views.UpdateSandGRegister.as_view(),name='updateSandGregi'),
    path('deleteSandGregi/<int:id>/',views.deleteSandGRegi,name='deleteSandGregi')


]
