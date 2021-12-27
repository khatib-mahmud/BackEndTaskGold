from django import forms
from django.forms import fields
from myapp.models import Mobile
class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = '__all__'
        
        widgets ={
            'Brand_Name': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Brand Name','pattern':'[A-Za-z|\s]+','title':'Name should contain only characters!'}),

            'Model': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Model-No.'}),
            
            'Color': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Color','pattern':'[^0-9]+','title':'No numbers'}),
            
            'JAN_Code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'JAN Code','title':'only distinct Code'}),

            
        }