from django import forms
from .models import Assignment, Company
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class AssignmentForm(forms.ModelForm):

    is_invoiced = forms.BooleanField(required=False)
    is_paid = forms.BooleanField(required=False) 
    completed = forms.BooleanField(required=False) 

    def __init__(self, *args, **kwargs):
        super(AssignmentForm, self).__init__(*args, **kwargs)
        self.fields['company'] = forms.ChoiceField(choices= [(comp.name, comp.name) for comp in Company.objects.all()])
        self.fields['interpreter'] = forms.ChoiceField(choices=[(user.username, user.username) for user in User.objects.all()])

    class Meta:
        model = Assignment        

        fields = ('date', 'company', 'language', 'patient', 'po_num', 'type', 'hours', 'hourly_rate', 'miles',
                'mileage_rate', 'address', 'flat_rate', 'parking', 'total', 'interpreter','interpreter_payment', 'is_invoiced', 'is_paid')
        widgets = {
            # 'company': forms.ChoiceWidget(choices=Company_Choices),
            'date': forms.DateTimeInput(attrs={'class': 'form-control mx-2', 'style': 'max-width: 18em'}),
            'language': forms.TextInput(attrs={'class': 'form-control mx-2', 'style': 'max-width: 12em'}),
            'patient': forms.TextInput(attrs={'class': 'form-control mx-2', 'style': 'max-width: 12em'}),
            'po_num': forms.NumberInput(attrs={'class': 'form-control mx-2', 'style': 'max-width: 12em'}),
            'type': forms.TextInput(attrs={'class': 'form-control mx-2', 'style': 'max-width: 6em'}),
            'hours': forms.NumberInput(attrs={'class': 'form-control mx-2', 'style': 'max-width: 6em'}),
            'hourly_rate': forms.NumberInput(attrs={'class': 'form-control mx-2', 'style': 'max-width: 6em'}),
            'miles': forms.TextInput(attrs={'class': 'form-control mx-2', 'style': 'max-width: 6em'}),
            'mileage_rate': forms.NumberInput(attrs={'class': 'form-control mx-2', 'style': 'max-width: 6em'}),
            'address': forms.TextInput(attrs={'class': 'form-control mx-2', 'style': 'max-width: 20em'}),
            'flat_rate': forms.NumberInput(attrs={'class': 'form-control mx-2', 'style': 'max-width: 6em'}),
            'parking': forms.NumberInput(attrs={'class': 'form-control mx-2', 'style': 'max-width: 6em'}),
            'total': forms.NumberInput(attrs={'class': 'form-control mx-2', 'style': 'max-width: 6em'}),
            #'interpreter': forms.TextInput(attrs={'class': 'form-control mx-2', 'style': 'max-width: 12em'}),
            'interpreter_payment': forms.NumberInput(attrs={'class': 'form-control mx-2', 'style': 'max-width: 12em'}),
            }

        

class InterpreterForm(forms.ModelForm):
    completed = forms.BooleanField(required=False) 

    class Meta:
        model = Assignment
        

        fields = ('hours','parking','completed')
        widgets = {
            'hours': forms.NumberInput(attrs={'class': 'form-control mx-2', 'style': 'max-width: 12em'}),
            'parking': forms.NumberInput(attrs={'class': 'form-control mx-2', 'style': 'max-width: 12em'}),
            }

class SignupInterpreterForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ('username','password','email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mx-2', 'style': 'max-width: 12em'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control mx-2', 'style': 'max-width: 12em'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mx-2', 'style': 'max-width: 12em'}),
            }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company

        fields = ('name',)
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control mx-2', 'style': 'max-width: 12em'}),
        }
        
