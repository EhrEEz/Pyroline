from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path(
        "<str:subject>/",
        views.FilteredQuestionPaperListView.as_view(),
    ),
    path(
        "<str:subject>/<str:year>/",
        views.FilteredQuestionSetListView.as_view(),
    ),
    path(
        "<str:subject>/chapters/<str:chapter>/<str:topic>",
        views.TopicWiseQuestionView.as_view(),
    ),
    path(
        "<str:subject>/chapters/<str:chapter>/",
        views.ChapterWiseQuestionView.as_view(),
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
