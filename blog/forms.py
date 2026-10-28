import re
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=3,
        max_length=100,
        error_messages={
            "required": "Please enter your name.",
            "min_length": "Name must be at least %(limit_value)d characters.",
        },
    )
    email = forms.EmailField(
        error_messages={
            "required": "Please enter your email address.",
            "invalid": "Please enter a valid email address.",
        },
    )
    subject = forms.CharField(
        min_length=5,
        max_length=150,
        error_messages={
            "required": "Please enter a subject.",
            "min_length": "Subject must be at least %(limit_value)d characters.",
        },
    )
    message = forms.CharField(
        min_length=10,
        max_length=1000,
        error_messages={
            "required": "Please write a message.",
            "min_length": "Message must be at least %(limit_value)d characters.",
            "max_length": "Message cannot be longer than %(limit_value)d characters.",
        },
    )

    # custom validation for a single field: clean_<fieldname>
    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if not re.fullmatch(r"[A-Za-z .'-]+", name):
            raise forms.ValidationError("Name can only contain letters and spaces.")
        return name

    def clean_message(self):
        message = self.cleaned_data["message"].strip()
        if len(message) < 10:
            raise forms.ValidationError("Message is too short.")
        return message