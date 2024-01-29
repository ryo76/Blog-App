from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control-lg'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control-sm'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control-sm'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','password1','password2')
    
    #Boostrapify username, pass and pass confirm
    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control-sm'
        self.fields['password1'].widget.attrs['class']='form-control-sm'
        self.fields['password2'].widget.attrs['class']='form-control-sm'