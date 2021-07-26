from .models import ModelDept, ModelEmpolyee
from django.forms import ModelForm, widgets
from django import forms

from re import *

class FormDeptCreate(ModelForm):
    class Meta:
        model = ModelDept
        fields = '__all__'
        widgets = {
            'department': forms.TextInput(attrs = {'class': 'form-control'}),
        }

    def clean(self):
        print("perform clean")
        cleaned_data = super().clean()
        dep = cleaned_data.get('department')
        deptCheck = ModelDept.objects.filter(department = dep)

        if (deptCheck):
            print("inside check")
            msg = "This department already exists"
            self.add_error('department', msg)

        dep_rule="^[A-Za-z]{1,25}\s?[A-Za-z]{0,25}\s?[A-Za-z]{0,25}$"
        matcher1=fullmatch(dep_rule,dep)

        if matcher1 is None:
            msg="Please enter alphabetic characters only"
            self.add_error('department',msg)    

class FormCreateEmp(ModelForm):
    class Meta:
        model=ModelEmpolyee
        fields = '__all__'
        widgets={
                'emp_id':forms.NumberInput(attrs={'class':'form-control'}),
                'name':forms.TextInput(attrs={'class':'form-control'}),
                'dept':forms.Select(attrs={'class':'form-control'}),
            }
    def clean(self):
        cleaned_data=super().clean()
        cleanEmpid=cleaned_data.get("emp_id")
        cleanName=cleaned_data.get("name")


        if (len(str(cleanEmpid))!=4):
            msg=("Please enter 4 digits number")
            self.add_error('emp_id',msg)

        employ=ModelEmpolyee.objects.get(emp_id=cleanEmpid)
        if(employ is not None):
            msg="Employee Id already exists"
            self.add_error("emp_id",msg)

        
        name_rule="^[A-Za-z]{1,25}\s?[A-Za-z]{0,25}\s?[A-Za-z]{0,25}$"
        matcher2=fullmatch(name_rule,cleanName) 
        if matcher2 is None:
            msg="Please enter alphabetic characters only"
            self.add_error('name',msg)

        



        



