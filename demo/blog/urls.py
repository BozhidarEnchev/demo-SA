from django.urls import path, include
from demo.blog.views import *

urlpatterns = [
    path('', PostView.as_view(), name='post-dashboard'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/', include([
        path('update/', PostUpdateView.as_view(), name='post-update'),
        path('delete/', PostDeleteView.as_view(), name='post-delete'),
    ])),
    path('<int:pk>/', PostDetailView.as_view(), name='post-details'),
    path('post-comment/', post_comment, name='post-comment'),
    path('<int:pk>/comment-delete/', delete_comment, name='delete-comment')
]
