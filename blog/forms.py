from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
# Finally, we can say which field(s) should end up in our form. In this scenario we want only 
# title and text to be exposed – author should be the person who is currently logged in (you!) 
# and created_date should be automatically set when we create a post (i.e. in the code), right?

# And that's it! All we need to do now is use the form in a view and display it in a template

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)