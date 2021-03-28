from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
router.register('questions', views.QuestionViewSet)
router.register('polls', views.PollViewSet)
# router.register('questions', views.QuestionViewSet, basename='foobar') #now name for reverse will be 'foobar-list' by default 'questions-list'

#api/  list (name 'api-root')
#api/questions  list (name 'questions-list')
#api/questions/<pk>  list (name 'question-detail')

#n upper url now is: http://127.0.0.1:8000/api/.....

urlpatterns = [

    path('', include(router.urls)),
    path('polls/<poll_id>/remove_question/<question_id>/', views.remove_question_from_poll, name="remove_question_from_poll" )
    # Polls
    # path('polls', views.PollListCreate.as_view()), #note list of all polls / create new one

    # path('todos', views.TodoListCreate.as_view()), #note current (uncompleted) todos
    # path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
    # path('todos/<int:pk>/complete', views.TodoComplete.as_view()),
    # path('todos/<int:pk>/uncomplete', views.TodoUncomplete.as_view()),
    # path('todos/completed', views.TodoCompletedList.as_view()),
    #
    # #  Auth
    # #note so you can access API without logging in in web version (mobile users)
    # path('signup', views.signup),
    # path('login', views.login), #note here user gets his token
]

