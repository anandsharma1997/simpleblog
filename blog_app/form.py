from django import forms
from .models import Post, Category

choice = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choice:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag','categary', 'body', 'header_image']

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class':'form-control'}),
            'categary' : forms.Select(choices=choice_list ,attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'body']

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'})
        }