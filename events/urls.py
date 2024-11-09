from django.urls import path
from .views import *

urlpatterns = [
    path('', EventsListView.as_view(), name='index'),
    path('<int:pk>', EventDetailView.as_view(), name='detail'),
    path('create', EventCreateView.as_view(), name='create'),
    path('update/<int:pk>', EventUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', EventDeleteView.as_view(), name='delete'),
    path('response/<int:pk>', response, name='response'),
    path('comment/create', CommentCreateView.as_view(), name='create_comment'),
    path('comment/update/<int:pk>', CommentUpdateView.as_view(), name='update_comment'),
    path('comment/delete/<int:pk>', CommentDeleteView.as_view(), name='delete_comment'),
]
