from django import forms
from .models import Post, Comment, Category

class PostForm(forms.ModelForm):
    # here to override fields in Post model:
    status = forms.ChoiceField(choices=Post.OPTIONS)
    # ModelChoiceField is very useful if you want to show data from another table as a dropdown on the form:
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select")
    class Meta:
        model = Post  # we define whick field of Post model we will use in this form
        fields = (  # you may also use exclude
            'title',
            'image',
            'content',
            'category',
            'status'
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
      