from django import forms
from .models import Pizza, Topping, Comment

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']
        labels = {'name': ''}

class ToppingForm(forms.ModelForm):
    class Meta:
        Model = Topping
        fields = ['name']
        labels = {'name':''}

class CommentForm(forms.ModelForm):
    class Meta:
        Model = Comment
        fields = ['name']
        labels = {'name':''}
