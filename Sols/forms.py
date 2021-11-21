from django import forms
from .models import PortFolio, Contact
from django.views.generic import CreateView


class PortFolioForm(forms.ModelForm):

    class Meta:
        model = PortFolio
        fields = ('client_full_name', 'project_picture', 'project_detail',
                  'category', 'project_url', 'service', 'pic2', 'pic3', 'pic4')
        widgets = {
            'client_full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name', 'name': 'name'}),
            'service': forms.Select(attrs={'class': 'form-control', }),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'project_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'pic2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'pic3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'pic4': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'project_url': forms.URLInput(attrs={'class': 'form-control', 'name': 'subject'}),
            'project_detail': forms.Textarea(attrs={'class': 'form-control', 'name': 'messsage'}),

        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject',
                  'message', )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name', 'id': 'name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email', 'id': 'email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Topic of your message', 'id': 'subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Reasons why you message us', 'id': 'message'}),


        }
