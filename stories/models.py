from django.db import models

# Create your models here.
class Story(models.Model):
    PARAGRAPH_LIMIT = 5 
    upvotes = models.PositiveIntegerField(default = 1)
    created_at = models.DateTimeField(auto_now_add = True)
    is_open = models.BooleanField(default=True)

    @models.permalink
    def get_absolute_url(self):
        return ('show_story', [self.pk])

    def as_paragraph(self):
        return '\n\n'.join([e.content for e in self.paragraphs.all()])

    def should_close(self):
        return self.paragraphs.count() >= Story.PARAGRAPH_LIMIT
    
    def first_paragraph(self):
        return self.paragraphs.all()[0]

    def __unicode__(self):
        return self.first_paragraph().__unicode__()

    def latest_submission(self):
        self.paragraphs.latest('created_at')

class Paragraph(models.Model):
    content = models.TextField(max_length = 420)
    story = models.ForeignKey(Story, related_name="paragraphs", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.content

