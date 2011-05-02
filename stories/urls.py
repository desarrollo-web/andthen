from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('stories.views',

   url(r'^new$', 'create', name="create"),
   url(r'^$', 'all', name="all_stories"),
   url(r'^open', 'all', {'open': True},name="add"),
   url(r'^closed', 'all', {'open': False}, name="read"),

   url(r'^(?P<story_id>\d+)$', 'show', name="show_story"),
   url(r'^(?P<story_id>\d+)/full$', 'show', {'full': True}, name="read_story"),
   url(r'^(?P<story_id>\d+)/continue$', 'append', name="continue_story")
)
