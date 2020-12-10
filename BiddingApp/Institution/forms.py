
from django.forms import ModelForm
from Institution.models import Skills,Jobs
from django import forms

class SkillCreationForm(ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'
        widgets = {
            'skill': forms.TextInput(attrs = {'class': 'form-control'}),
        }

    def clean(self):
        print("perform clean")
        cleaned_data = super().clean()
        skl = cleaned_data.get('skill')
        skl_chk = Skills.objects.filter(skill = skl)

        if (skl_chk):
            msg = "This skill already exists"
            self.add_error('skill', msg)
    
class JobCreationForm(ModelForm):
    class Meta:
        model=Jobs
        fields='__all__'
        widgets = {
            'skillset': forms.Select(attrs = {'class': 'form-control'}),
            'jobTitle':forms.TextInput(attrs = {'class': 'form-control'}),
            'experience':forms.NumberInput(attrs = {'class': 'form-control'}),
            'hourlyRate':forms.NumberInput(attrs = {'class': 'form-control'}),
        }
