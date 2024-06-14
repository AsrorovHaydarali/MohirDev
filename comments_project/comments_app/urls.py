from django.urls import path
from .views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("comment_list/", CommentListView.as_view(), name="comment_list"),
    path(
        "comment_list/comment/<int:pk>",
        CommentDetailView.as_view(),
        name="comment_detail",
    ),
    path(
        "comment_list/comment/create",
        CommentCreateView.as_view(),
        name="comment_create",
    ),
    path(
        "comment_list/comment/<int:pk>/update",
        CommentUpdateView.as_view(),
        name="comment_update",
    ),
    path(
        "comment_list/comment/<int:pk>/delete",
        CommentDeleteView.as_view(),
        name="comment_delete",
    ),
]
