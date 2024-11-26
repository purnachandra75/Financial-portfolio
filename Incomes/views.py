from django.shortcuts import redirect, render
from django.views import View
from .models import IncomeSource,RegisterIncome
from .forms import IncomesourceForm,RegisterForm
from django.http import HttpResponse
# Create your views here.
def getIncomepage(request):
    uid=request.session.get('uid')
    user=request.session.get('user')
    somedata=IncomeSource.objects.filter(user_id=uid)
    print(somedata)
    return render(request,'incomepage.html',{'somedata':somedata,'user':user})

def deleteIncome(request,id):
    somedata=IncomeSource.objects.get(id=id)
    somedata.delete()
    return redirect('Incomepage')
    

class UpdateIncome(View):
    def get(self,request,id):
        somedata=IncomeSource.objects.get(id=id)
        user=request.session.get('user')
        return render(request,'createIncomesource.html',{'form':IncomesourceForm(instance=somedata,request=request),'user':user})
    def post(self,request,id):
        uid=request.session.get('uid')
        somedata=IncomeSource.objects.get(id=id)
        somedata=IncomesourceForm(request.POST,instance=somedata,request=request)
        if somedata.is_valid():
            newdata=somedata.save(commit=False)
            newdata.user_id=uid
            newdata.save()
            return redirect('Incomepage')

class CreateIncomeSource(View):
    def get(self,request):
        user=request.session.get('user')
        return render(request,'createIncomesource.html',{'form':IncomesourceForm(request=request),'user':user})
    def post(self,request):
        uid=request.session.get('uid')
        
        somedata=IncomesourceForm(request.POST,request=request)
        
        if somedata.is_valid():
           
            newdata=somedata.save(commit=False)
            newdata.user_id=uid
            newdata.save()
            return redirect('Incomepage')
        return HttpResponse('bad data......')

def updateIncomecate(request,id):
    user=request.session.get('user')
    uid=request.session.get('uid')
    somedata=RegisterIncome.objects.get(id=id)
    if request.method=='GET':
        return render(request,'createIncomesource.html',{'user':user,'form':RegisterForm(instance=somedata)})
    if request.method == 'POST':
        somedata=RegisterForm(request.POST,instance=somedata)
        if somedata.is_valid():
            somedata.save()
           
        return redirect('registerIncome')
    
def deletecate(request,id):
    somedata=RegisterIncome.objects.get(id=id)
    somedata.delete()
    return redirect('registerIncome')
    
def createIncomecate(request):
    user=request.session.get('user')
    uid=request.session.get('uid')
    if request.method=='GET':
        return render(request,'createIncomesource.html',{'user':user,'form':RegisterForm()})
    if request.method == 'POST':
        somedata=RegisterForm(request.POST)
        if somedata.is_valid():
            newdata=somedata.save(commit=False)
            newdata.user_id=uid
            newdata.save()
        return redirect('registerIncome')
def registerIncome(request):
    uid=request.session.get('uid')
    user=request.session.get('user')
    somedata=RegisterIncome.objects.filter(user_id=uid)
    
    return render(request,'RegisteIncome.html',{'somedata':somedata,'user':user})