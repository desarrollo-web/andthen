from django.shortcuts import render_to_response, redirect, get_object_or_404
from stories.forms import ParagraphForm
from stories.models import Paragraph, Story
from django.template import RequestContext

def create(request):
    return render_to_response('create.html', 
                              {'form': ParagraphForm()},
                              context_instance= RequestContext(request))

def _save_paragraph(request, story=None, template=None):
    form = ParagraphForm(request.POST)
    if form.is_valid():
        p = form.save(commit=False)
        p.story = story or Story.objects.create()
        p.save()
        if p.story.should_close():
            p.story.is_open = False
            p.story.save()
        return redirect(p.story)
    else:
        return render_to_response(template, {'form': form, 'story':story}, context_instance=RequestContext(request))
        
def all(request, open = None):

    if request.method == 'POST':
        return _save_paragraph(request, template='create.html')

    stories = Story.objects.all().order_by('-created_at')
    if open is not None:
        stories = stories.filter(is_open = open)
    return render_to_response(
            'all.html',
            {'stories': stories,
                'all': open is None,
                'open': open})


def show(request, story_id, full=False):
    story = get_object_or_404(Story, pk=story_id)
    if request.method == 'POST':
        return _save_paragraph(request, story, template='append.html') 

    return render_to_response(
            'show.html', 
            {
              'story': story,
              'full': full,
            })

def append(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    return render_to_response('append.html', 
            {'form': ParagraphForm(initial={'story':story}), 'story': story},
                              context_instance=RequestContext(request))
           
