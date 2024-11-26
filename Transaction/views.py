from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import Transactions
from .forms import Transactiondetails
from Incomes.models import IncomeSource

def getTransaction(request):
    sendNotification(request)
    user = request.session.get('user')
    uid = request.session.get('uid')
    somedata = Transactions.objects.filter(user_id=uid)
    return render(request, 'Transaction.html', {'user': user, 'somedata': somedata})

def deleteTransaction(request, id):
    somedata = Transactions.objects.filter(id=id)
    somedata.delete()
    return redirect('Transaction')

class CreateTransaction(View):
    
    def get(self, request, tran):
        user = request.session.get('user')  # This might return a string or an object
        uid = request.session.get('uid')  # Ensure this is correctly stored in the session
        return render(request, 'createTransaction.html', {
            'form': Transactiondetails(request=request, tran=tran),
            'user': user
        })

    def post(self, request, tran):
        user = request.session.get('user')  # This might return a string or an object
        uid = request.session.get('uid')  # Correctly fetch the user ID
        if not uid:
            return HttpResponse('User not logged in', status=401)

        form = Transactiondetails(request.POST, request=request, tran=tran)
        if form.is_valid():
            newdata = form.save(commit=False)
            newdata.user_id = uid  # Ensure you're saving the correct user ID here
            newdata.transaction_type=tran
            newdata.save()
            return redirect('Transaction')
        
        return HttpResponse('bad data....')



class UpdateTransaction(View):
    def get(self, request, id,tran):
        user = request.session.get('user')
        transaction = Transactions.objects.get(id=id)
        return render(request, 'createTransaction.html', {
            'form': Transactiondetails(instance=transaction, request=request,tran=tran),
            'user': user
        })

    def post(self, request, id,tran):
        transaction = Transactions.objects.get(id=id)
        form = Transactiondetails(request.POST, instance=transaction, request=request,tran=tran)
        if form.is_valid():
            form.save()
            return redirect('Transaction')
        return HttpResponse('bad data....')

from django.db.models import Q
def sendNotification(request):
    uid = request.session.get('uid')
    somedata=IncomeSource.objects.filter(frequency='monthly',user_id=uid)
    print(somedata)
    if somedata:
        today = datetime.now().date()
        print("Today's date is:", today)
        print(today.day)
        for sdata in somedata:
            trdata = Transactions.objects.filter(Q(category=sdata.source) &Q(user_id=uid)&(Q(date__day=today.day) | Q(date__month=today.month)))
            print(trdata)
            if not trdata:
                print('send mail......')
    somedata=IncomeSource.objects.filter(frequency='Yearly',user_id=uid)
    if somedata:
        today = datetime.now().date()
        print("Today's date is:", today)
        print(today.year)
        for sdata in somedata:
            print(sdata.source)
            trdata = Transactions.objects.filter(Q(category=sdata.source) &Q(user_id=uid)&(Q(date__year=today.year)))
            print(trdata)
            if not trdata:
                print('send mail......')
            
    