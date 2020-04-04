from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Name",
        }),
        max_length=200,
        label=''
    )

    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            "placeholder": "Email",
        }),
        label=''
    )

    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput({
            "placeholder": "Subject"
        }),
        label=''
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Message"}),
        max_length=1000,
        label=''
    )
