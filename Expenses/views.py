from django.shortcuts import render,redirect
from django.views import View

from .forms import ExpensesdetaildForm,ExpenseRegistrationForm
from .models import ExpensesInfo,ExpensesRegister

def getexpensesPage(request):
    user=request.session.get('user')
    uid=request.session.get('uid')
    somedata=ExpensesInfo.objects.filter(user_id=uid)
    return render(request,'expenses.html',{'user':user,'somedata':somedata})

def deleteExpenses(request,id):
    somedata=ExpensesInfo.objects.get(id=id)
    somedata.delete()
    return redirect('Expensespage')
class updateExpenses(View):
    def get(self,request,id):
        somedata=ExpensesInfo.objects.get(id=id)
        user=request.session.get('user')
        return render(request,'createExpenses.html',{'user':user,'form':ExpensesdetaildForm(instance=somedata,request=request)})
    def post(self,request,id):
        somedata=ExpensesInfo.objects.get(id=id)
        newdata=ExpensesdetaildForm(request.POST,instance=somedata,request=request)
        if newdata.is_valid():
            newdata.save()
            return redirect('Expensespage') 

class CreateExpenses(View):
    def get(self,request):
        user=request.session.get('user')
        return render(request,'createExpenses.html',{'user':user,'form':ExpensesdetaildForm(request=request)})
    def post(self,request):
        uid=request.session.get('uid')
        somedata=ExpensesdetaildForm(request.POST,request=request)
        if somedata.is_valid():
            newdata=somedata.save(commit=False)
            newdata.user_id=uid
            newdata.save()
            return redirect('Expensespage')


def registerExpanses(request):
    uid=request.session.get('uid')
    user=request.session.get('user')
    somedata=ExpensesRegister.objects.filter(user_id=uid)
    
    return render(request,'RegisterExpenses.html',{'somedata':somedata,'user':user})

def createExpansescata(request):
    uid=request.session.get('uid')
    user=request.session.get('user')
    if request.method=='GET':

        return render(request,'createExpenses.html',{'user':user,'form':ExpenseRegistrationForm()})
    if request.method =='POST':
        somedata=ExpenseRegistrationForm(request.POST)
        if somedata.is_valid():
            newdata=somedata.save(commit=False)
            newdata.user_id=uid
            newdata.save()
            return redirect('regsExpanses')


def updateExpanseCate(request,id):
    user=request.session.get('user')
    somedata=ExpensesRegister.objects.get(id=id)
    if request.method =='GET':
        return render(request,'createExpenses.html',{'form':ExpenseRegistrationForm(instance=somedata),'user':user})
    if request.method == 'POST':
        somedata=ExpenseRegistrationForm(request.POST,instance=somedata)
        if somedata.is_valid():
            somedata.save()
            return redirect('regsExpanses')
def deleteExpansescate(request,id):
    somedata=ExpensesRegister.objects.get(id=id)
    somedata.delete()
    return redirect('regsExpanses')