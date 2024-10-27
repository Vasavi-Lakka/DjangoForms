from django import forms
from app.models import *


class TopicForm(forms.Form):
    tn=forms.CharField()

class WebpageForm(forms.Form):
    tn=forms.ModelChoiceField(queryset=Topic.objects.all())
    n=forms.CharField()
    u=forms.URLField()

class AccessForm(forms.Form):
    n=forms.ModelChoiceField(queryset=Webpage.objects.all())
    a=forms.CharField()
    da=forms.DateField()
