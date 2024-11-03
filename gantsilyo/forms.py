from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Product



class AdminUserCreationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('employee', 'Employee'),
        ('admin', 'Admin'),
    ]
    
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect, label="Role")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        role = self.cleaned_data.get('role')
        if role == 'admin':
            user.is_staff = True
            user.is_superuser = True
        else:
            user.is_staff = True
            user.is_superuser = False
        if commit:
            user.save()
        return user

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']