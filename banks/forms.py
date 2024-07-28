from django import forms
from .models import Bank, Branch

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['name', 'description']

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name', 'address', 'email', 'capacity']