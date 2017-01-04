from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        widgets = {
          'title': forms.TextInput(attrs={'size':50, 'style':"font-size:26px;"}),
          'text': forms.Textarea(attrs={'rows':10, 'cols':65, 'style':"font-size:20px;"}),
          'post_type': forms.Select(attrs={'style':"font-size:16px"}),
        }
        fields = ('title','text','post_type')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        widgets = {
          'text': forms.Textarea(attrs={'cols':65, 'rows':1, 'placeholder':'留言...', 'onkeyup':'AutoGrowTextArea(this)', 'onkeypress':'DetectEnterKeyPress(event)'}),
        }
        fields = ('text',)

#測試用form
class MyForm(forms.Form):
	CHOICES = (
    ('FR', '一般文章'),
    ('SO', '作品'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
	)
	field = forms.ChoiceField(choices=CHOICES)