from django import forms

from myapp.models import EmployeeDetails




class EmployeeDetailsForm(forms.ModelForm):

    
    class Meta:
            
        model = EmployeeDetails
        fields = "__all__"

        widgets = {
            'emp_id': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'first_name': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'last_name':  forms.TextInput(attrs={'class':'form-control mb-3'}),
            'phone': forms.TextInput(attrs={'class':'form-control mb-3', 'type': 'number', 'min':'0', 'placeholder': '10-digit mobile number'}),
            'email': forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder': 'example@example.com'}),
            'address': forms.Textarea(attrs={'class':'form-control mb-3', 'rows':4}),
            'gender': forms.RadioSelect(attrs={'class':'form-check', 'type': 'radio'}),
            'dob': forms.DateInput(attrs={'class':'form-control mb-3', 'type': 'date'}),
            'date_hired': forms.DateInput(attrs={'class':'form-control mb-3', 'type': 'date'}),
            'status': forms.Select(attrs={'class':'form-select mb-3'}),
            'department': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'position': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'salary': forms.NumberInput(attrs={'class':'form-control mb-3', 'min': '0'}),
            'image': forms.FileInput(attrs={'class':'form-control mb-3'})
        }

        