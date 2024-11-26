from django import forms
from .models import Transactions
from Incomes.models import RegisterIncome
from Expenses.models import ExpensesRegister

class Transactiondetails(forms.ModelForm):
    category = forms.ChoiceField(choices=[])  # Initialize with empty choices

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.tran = kwargs.pop('tran', None)
        super(Transactiondetails, self).__init__(*args, **kwargs)

        if self.request:
            uid = self.request.session.get('uid')  # Get user ID from session
            if uid:
                # Determine transaction type from initial or provided data
                transaction_type = self.request.POST.get('transaction_type') or self.tran
                source_choices = []

                if transaction_type == 'Income':
                    sources = RegisterIncome.objects.filter(user_id=uid)  # Fetch income sources
                    source_choices = [(source.name, source.name) for source in sources]
                elif transaction_type == 'Expanse':
                    sources = ExpensesRegister.objects.filter(user_id=uid)  # Fetch expense sources
                    source_choices = [(source.name, source.name) for source in sources]

                # Set category choices dynamically
                self.fields['category'].choices = source_choices

    class Meta:
        model = Transactions
        fields = ['amount', 'category', 'date', 'description']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'date'}),
        }
