from django.shortcuts import redirect, render
from django.views import View
from .forms import BudgetForm,RegisterBudgetForm
from .models import Budgets,RegisterBudget
from django.http import HttpResponse

def getbudgetPage(request):
    user=request.session.get('user')
    uid=request.session.get('uid')
    somedata=Budgets.objects.filter(user_id=uid)
    return render(request,'budget.html',{'user':user,'somedata':somedata})

def deletebudget(request,id):
    somedata=Budgets.objects.get(id=id)
    somedata.delete()
    return redirect('Budgetpage')

class CreateBudget(View):
    def get(self,request):
        user=request.session.get('user')
        return render(request,'createBudgets.html',{'user':user,'form':BudgetForm(request=request)})
    def post(self,request):
        user=request.session.get('user')
        uid=request.session.get('uid')
        somedata=BudgetForm(request.POST,request=request)
        if somedata.is_valid():
            newdata=somedata.save(commit=False)
            newdata.user_id=uid
            newdata.save()
            return redirect('Budgetpage')
        return HttpResponse("baddata...///")
    
class UpdateBudget(View):
    def get(self,request,id):
        user=request.session.get('user')
        somedata=Budgets.objects.get(id=id)
        return render(request,'createBudgets.html',{'user':user,'form':BudgetForm(instance=somedata,request=request)})
    def post(self,request,id):
        user=request.session.get('user')
        uid=request.session.get('uid')
        data=Budgets.objects.get(id=id)
        somedata=BudgetForm(request.POST,instance=data,request=request)
        if somedata.is_valid():
            somedata.save()
            
            return redirect('Budgetpage')
        return HttpResponse("baddata...///")
    

def registerBudget(request):
    user=request.session.get('user')
    uid=request.session.get('uid')
    somedata=RegisterBudget.objects.filter(user_id=uid)
    print(somedata)
    return render(request,'registerBudget.html',{'user':user,'somedata':somedata})

def createBudget(request):
    user=request.session.get('user')
    uid=request.session.get('uid')
    if request.method == 'GET':
        return render(request,'createBudgets.html',{'user':user,'form':RegisterBudgetForm})
    if request.method == 'POST':
        somedata=RegisterBudgetForm(request.POST)
        if somedata.is_valid():
            newdata=somedata.save(commit=False)
            newdata.user_id=uid
            newdata.save()
            return redirect('registerBudget')
def updatebudgetrege(request,id):
    somedata=RegisterBudget.objects.get(id=id)
    if request.method=='GET':
        return render(request,'createBudgets.html',{'form':RegisterBudgetForm(instance=somedata)})
    if request.method == 'POST':
        somedata=RegisterBudgetForm(request.POST,instance=somedata)
        if somedata.is_valid():
            somedata.save()
            return redirect('registerBudget')
def deletebudgetrege(request,id):
    somedata=RegisterBudget.objects.get(id=id)
    somedata.delete()
    return redirect('registerBudget')