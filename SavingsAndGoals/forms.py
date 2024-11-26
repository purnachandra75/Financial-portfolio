from django import forms
from .models import SavingandGoals,RegisterSavingsandGoals

class SavingsandgoalsDetails(forms.ModelForm):

    goal_name = forms.ChoiceField(choices=[])  # Initialize as empty

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SavingsandgoalsDetails, self).__init__(*args, **kwargs)

        if self.request:
            uid = self.request.session.get('uid')
            if uid:
                sources = RegisterSavingsandGoals.objects.filter(user_id=uid)
                source_choices = [(source.name, source.name) for source in sources]
                self.fields['goal_name'].choices = source_choices
    class Meta:
        model=SavingandGoals
        fields=['goal_name','target_amount','current_amount','deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }
    

class RegisteSandGform(forms.ModelForm):
    class Meta:
        model=RegisterSavingsandGoals
        fields=['name'] 