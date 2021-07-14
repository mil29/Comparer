from django import forms


class IngredientsForm(forms.Form):
    ingredients = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Please enter the ingredients'}))
    