from django import forms
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, ButtonHolder, Submit, Fieldset


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
        #     'author': forms.Select(attrs={'class': 'form-control'}),
        #     'body': forms.Textarea(attrs={'class': 'form-control'}),
        # }
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'well'
        self.helper.layout = Layout(
            Div(
                Fieldset('', 'title', 'title_tag', 'author', 'body', css_class='col-md-6')
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )