from django.urls import path
from . import views
from .feeds import LatestsPostsFeed

from django.conf import settings
from django.conf.urls.static import static
app_nae = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
          views.post_detail,
          name='post_detail'),
    path('<int:post_id>/share/',
         views.post_share,
         name='post_share'),
    path('tag/<slug:tag_slug>/',
        views.post_list, name='post_list_by_tag'),
    path('feed/', LatestsPostsFeed(), name='post_feed')
]