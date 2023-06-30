from django import forms
from .models import Datavisualization



class myform(forms.ModelForm):
    class Meta:
        model=Datavisualization
        fields='__all__'
        widgets={
            'end_year':forms.TextInput(attrs={'class':'form-control'}),
            'intensity':forms.TextInput(attrs={'class':'form-control'}),
            'sector':forms.TextInput(attrs={'class':'form-control'}),
            'topic':forms.TextInput(attrs={'class':'form-control'}),
            'url':forms.TextInput(attrs={'class':'form-control'}),
            'region':forms.TextInput(attrs={'class':'form-control'}),
            'start_year':forms.TextInput(attrs={'class':'form-control'}),
            'impact':forms.TextInput(attrs={'class':'form-control'}),
            'added':forms.TextInput(attrs={'class':'form-control'}),
            'published':forms.TextInput(attrs={'class':'form-control'}),
            'country':forms.TextInput(attrs={'class':'form-control'}),
            'relevance':forms.TextInput(attrs={'class':'form-control'}),
            'pestle':forms.TextInput(attrs={'class':'form-control'}),
            'source':forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'likelihood':forms.TextInput(attrs={'class':'form-control'}),
        }
    




