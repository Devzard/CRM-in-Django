from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    input_field_class = 'w-full h-full px-3 py-3 font-sans text-sm font-normal transition-all bg-transparent border rounded-md peer border-blue-gray-200 text-blue-gray-700 outline outline-0 placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 focus:border-2 focus:border-gray-900 focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50'

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':f'{input_field_class}', 'placeholder':' '}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':f'{input_field_class}', 'placeholder':' '}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':f'{input_field_class}', 'placeholder':' '}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1','password2')
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = f'{self.input_field_class}'
        self.fields['username'].widget.attrs['placeholder'] = ' '
        self.fields['username'].label = 'User Name'
        self.fields['username'].help_text = '<span class="text-sm text-slate-500"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = f'{self.input_field_class}'
        self.fields['password1'].widget.attrs['placeholder'] = ' '
        self.fields['password1'].label = 'Password'
        self.fields['password1'].help_text = '<ul class="text-xs text-slate-500"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = f'{self.input_field_class}'
        self.fields['password2'].widget.attrs['placeholder'] = ' '
        self.fields['password2'].label = 'Confirm Password'
        self.fields['password2'].help_text = '<ul class="text-xs text-slate-500"><li>Enter the same password as before, for verification.</li></ul>'