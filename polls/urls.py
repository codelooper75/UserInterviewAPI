from django.urls import path, include

from polls import views as polls_views




app_name = 'polls'
urlpatterns = [
    path('', polls_views.all_polls_list, name='all_polls_list'),
    path('<poll_id>/', polls_views.poll_details, name='poll_details'),


]

