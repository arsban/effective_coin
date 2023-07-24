from django import forms

class CurrencyForm(forms.Form):
    selected_date = forms.DateField(label='Выберите дату', widget=forms.DateInput(attrs={'type': 'date'}))
