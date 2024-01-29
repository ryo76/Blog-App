from django import forms
from .models import Post

catchoices = [('Effortless Outfits','Effortless Outfits'),
              ('Shop Our Picks','Shop Our Picks'),
              ('Brand Profiles','Brand Profiles'),
              ('Buying Guide','Buying Guide'),
              ('Casual Style','Casual Style'),
              ('Formal Attire','Formal Attire'),
              ('Spring & Summer','Spring & Summer'),
              ('Style Tips & Tricks','Style Tips & Tricks'),
              ]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body','snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of your post'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title-tag of your post'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=catchoices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','category','body','snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of your post'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title-tag of your post'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=catchoices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
        }