from django.urls import path
from . import views as users_views

app_name = 'users'
urlpatterns = [
    path('<user_id>/answered/', users_views.answered_questions, name='answered_questions'),

]
