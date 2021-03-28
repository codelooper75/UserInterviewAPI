
from django.shortcuts import render, redirect
from django.http import HttpResponse


from polls.models import Question, Answer, Poll

def all_polls_list(request):
    all_polls_list = Poll.objects.all()

    context = {
        'all_polls_list':all_polls_list
    }
    return render(request, 'polls/all_polls_list.html', context)

def poll_details(request, poll_id):
    poll = Poll.objects.get(id=poll_id)

    # q = Question.objects.filter(poll__title='Поведение на дороге') #поиск всех вопрос по названию опроса

    answered = Question.objects.filter(answers__user='1',poll = poll_id ) #отвеченные из этого опроса, текущим юзером
    answers = Answer.objects.filter(user='1',question__poll = poll) #ответы на вопросы из этого опроса
    print(answers)
    context = {
        'poll':poll,
        'answered':answered

    }
    return render(request, 'polls/poll_details.html', context)

# def home(request):
#     # polls = Poll.objects.all()
#     context = {
#         # 'polls' : polls
#     }
#     return render(request, 'polls/home.html', context)
#
# def create(request):
#     context = {
#     }
#     return render(request, 'polls/create.html', context)
#
# def vote(request):
#     context = {
#     }
#     return render(request, 'polls/vote.html', context)
#
#
#
# # def vote(request, poll_id):
# #     poll = Poll.objects.get(pk=poll_id)
# #
# #     if request.method == 'POST':
# #
# #         selected_option = request.POST['poll']
# #         if selected_option == 'option1':
# #             poll.option_one_count += 1
# #         elif selected_option == 'option2':
# #             poll.option_two_count += 1
# #         elif selected_option == 'option3':
# #             poll.option_three_count += 1
# #         else:
# #             return HttpResponse(400, 'Invalid form')
# #
# #         poll.save()
# #
# #         return redirect('results', poll.id)
# #
# #     context = {
# #         'poll' : poll
# #     }
# #     return render(request, 'poll/vote.html', context)
# #
# def results(request, poll_id):
#     # poll = Poll.objects.get(pk=poll_id)
#     context = {
#         # 'poll' : poll
#     }
#     return render(request, 'polls/results.html', context)