from django import forms
from .models import Budgets,RegisterBudget

class BudgetForm(forms.ModelForm):
    category = forms.ChoiceField(choices=[])  # Initialize with empty choices

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Get request from kwargs
        super(BudgetForm, self).__init__(*args, **kwargs)

        # Filter data based on condition and set choices for `source` dropdown
       
        if self.request:
            uid = self.request.session.get('uid')  # Assume session has `uid`
            
            if self.request:
                uid = self.request.session.get('uid')
                if uid:
                    sources = RegisterBudget.objects.filter(user_id=uid)
                    source_choices = [(source.name, source.name) for source in sources]
                    self.fields['category'].choices = source_choices

    class Meta:
        model=Budgets
        fields=['category','limit','start_date','end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class RegisterBudgetForm(forms.ModelForm):
    class Meta:
        model=RegisterBudget
        fields=['name']