from django import forms
from demo.blog.models import Post
from demo.blog.mixins import FormFieldMixin


class PostBaseForm(FormFieldMixin, forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class PostCreateForm(PostBaseForm):
    pass


class PostUpdateForm(PostBaseForm):
    pass
