from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .views import (
    AnswerViewSet, OptionViewSet, QuestionViewSet,
    QuestionTypeViewSet, SectionViewSet, SurveyViewSet,
)


router = DefaultRouter()
router.register(r'surveys', SurveyViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'question-types', QuestionTypeViewSet)
router.register(r'options', OptionViewSet)
router.register(r'answers', AnswerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
