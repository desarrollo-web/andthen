from stories.models import Paragraph, Story
from django import forms

class ParagraphForm(forms.ModelForm):
    story = forms.ModelChoiceField(queryset=Story.objects.all(), widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Paragraph
        exclude = ('created_at', 'upvotes', 'story')
