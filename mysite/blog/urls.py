from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
app_nae = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
          views.post_detail,
          name='post_detail'),
    path('<int:post_id>/share/',
         views.post_share,
         name='post_share'),
]