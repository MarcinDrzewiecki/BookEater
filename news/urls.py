from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls import patterns
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.post_list),
]

# if settings.DEBUG:
#     # static files (images, css, javascript, etc.)
#     urlpatterns += patterns('',
#         (r'^covers/(?P<path>.*)$', 'django.views.static.serve', {
#         'document_root': settings.MEDIA_ROOT}))
urlpatterns += patterns('',
    # ... the rest of your URLconf goes here ...
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)