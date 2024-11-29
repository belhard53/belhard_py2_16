from typing import Any
from django import forms
from .models import Students, Course
from django.core.exceptions import ValidationError

 
class CourseAddForm(forms.Form):
    
    langs = [
        ('py','Python'),
        ('js','JavaScript'),
        ('c','C++'),
        ('an','Android'),
    ]
    
    name = forms.ChoiceField(choices=langs, label='Название', required=True)
    course_num = forms.IntegerField(min_value=1, max_value=100, required=True)
    start_date = forms.DateField(widget=forms.DateInput(
                                attrs={'type':'date', 'class':"data1" }))    
    end_date = forms.DateField(widget=forms.DateInput(
                                attrs={'type':'date', 'class':"data1" }))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    


class CourseAddForm2(forms.ModelForm):
    model = Course
    fields = '__all__'
    
class StudentAddForm(forms.ModelForm):   
    class Meta:
        model = Students
        fields = '__all__'
        # fields = ['surname', 'name', 'sex', 'age', 'course', 'active', 'photo']
        
        
        widgets = {
            'start_date': forms.SelectDateWidget
        }
        
    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 7:
            raise ValidationError('возраст не подходит')
        return age
    
    # def save(self, commit: bool = ...) -> Any:    
    #     return super().save(commit)
        
        
    