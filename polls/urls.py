from django.urls import path

from . import views, rest_views

app_name = 'polls'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # path("rest/", rest_views.question_list),
    # path("rest/<int:pk>", rest_views.question_details)
    path("rest/", rest_views.QuestionList.as_view()),
    path("rest/<int:pk>", rest_views.QuestionDetails.as_view())
]