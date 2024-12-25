from django import forms

class QRCodeForm(forms.Form):
    recipient_name = forms.CharField(
        label="Имя получателя",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Например: Иванов Иван Иванович'}),
    )
    phone = forms.CharField(
        label="Телефон получателя",
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Например: +7XXXXXXXXXX'}),
    )
    amount = forms.DecimalField(
        label="Сумма перевода",
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder': 'Например: 1000'}),
    )

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        return phone.replace(" ", "")