from rest_framework import routers

from apps.note import viewsets as noteRentalViews
from apps.question import viewsets as questionRentalViews
from apps.authentication import viewsets as authenticationRentalViews

router = routers.DefaultRouter()
router.register(r"Program", noteRentalViews.ProgramViewset)
router.register(r"Subject", noteRentalViews.SubjectViewset)
router.register(r"ChapterSet", noteRentalViews.ChapterSetViewset)
router.register(r"Chapter", noteRentalViews.ChapterViewset)
router.register(r"Topic", noteRentalViews.TopicViewset)
router.register(r"Description", noteRentalViews.DescriptionViewset)
router.register(r"Question", questionRentalViews.QuestionViewSet)
router.register(r"QuestionPaper", questionRentalViews.QuestionPaperViewSet)
router.register(r"QuestionSet", questionRentalViews.QuestionSetterViewSet)
router.register(r"Answer", questionRentalViews.AnswerViewSet)
router.register(r"User", authenticationRentalViews.UserViewSet)
