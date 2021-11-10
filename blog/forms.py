from django import forms

"""
:author: widget tells Django to load forms.TextInput as HTML text input
        element in templates
:body: forms.TextArea widget to render the field as HTML text area element
:attrs= dictionary which allows us to specify CSS classes
        - to help formatting the template for view
"""


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Name'
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Leave a comment!'
        })
    )
