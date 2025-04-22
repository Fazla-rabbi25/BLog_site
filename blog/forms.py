from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author','title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}), 
        }

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('author', 'text')
        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}), 
        }
# The above code defines two forms using Django's ModelForm class. The PostForm is used for creating and updating blog posts, while the CommentForm is used for adding comments to posts. Each form specifies the model it corresponds to and the fields that should be included. Additionally, custom widgets are applied to enhance the appearance of the form fields in HTML.
# The PostForm includes fields for the author, title, and text of the post, while the CommentForm includes fields for the author's name and the comment text. The widgets attribute is used to apply CSS classes to the form fields for better styling in templates.