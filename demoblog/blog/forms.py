from django import forms
from django.utils import timezone

from .models import Post


class PostForm(forms.ModelForm):
    is_publish = forms.BooleanField(initial=False, required=False)

    def save(self, user, commit=True):
        self.instance.author = user
        if self.cleaned_data['is_publish']:
            self.instance.published_date = timezone.now()
        else:
            self.instance.published_date = None
        return super(PostForm, self).save(commit)

    class Meta:
        model = Post
        fields = ('title', 'text', 'is_publish')
