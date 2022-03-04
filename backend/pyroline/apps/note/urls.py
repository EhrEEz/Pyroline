from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path(
        "<str:subject>/",
        views.SyllabusView.as_view(),
    ),
    path(
        "<str:subject>/<str:chapter>/",
        views.TopicView.as_view(),
    ),
    # path("program/history/<int:program>/<str:user>/",
    #      views.ProgramHistoryView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
