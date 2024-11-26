from django import forms
from .models import ExpensesInfo,ExpensesRegister

class ExpensesdetaildForm(forms.ModelForm):
    category = forms.ChoiceField(choices=[])  # Initialize as empty

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ExpensesdetaildForm, self).__init__(*args, **kwargs)

        if self.request:
            uid = self.request.session.get('uid')
            if uid:
                sources = ExpensesRegister.objects.filter(user_id=uid)
                source_choices = [(source.name, source.name) for source in sources]
                self.fields['category'].choices = source_choices

    class Meta:
        model = ExpensesInfo
        fields = ['amount', 'category', 'description', 'is_recurring']

class ExpenseRegistrationForm(forms.ModelForm):
    class Meta:
        model=ExpensesRegister
        fields=['name','type']

