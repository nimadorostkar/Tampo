from .models import Comment, Newsletter, Contact
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')



class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('email',)





class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'body')
