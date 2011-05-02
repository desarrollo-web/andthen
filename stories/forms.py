from django.forms import ModelForm
from stories.models import Paragraph

class ParagraphForm(ModelForm):
    class Meta:
        model = Paragraph
        exclude = ('created_at', 'upvotes')
