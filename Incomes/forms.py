from django import forms
from .models import IncomeSource,RegisterIncome





class IncomesourceForm(forms.ModelForm):
    source = forms.ChoiceField(choices=[])  # Initialize with empty choices

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Get request from kwargs
        super(IncomesourceForm, self).__init__(*args, **kwargs)

        # Filter data based on condition and set choices for `source` dropdown
       
        if self.request:
            uid = self.request.session.get('uid')  # Assume session has `uid`
            
            if uid:
                # Fetch source names for the given user ID
                sources = RegisterIncome.objects.filter(user_id=uid)
                source_choices = [(source.name, source.name) for source in sources]
                
                # Update choices for `source` dropdown
                self.fields['source'].choices = source_choices

    class Meta:
        model = IncomeSource
        fields = ['amount', 'source', 'frequency', 'date','description']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'date'}),
        }

class RegisterForm(forms.ModelForm):
    class Meta:
        model=RegisterIncome
        fields=['name']    
