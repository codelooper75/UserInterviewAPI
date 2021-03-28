from django.shortcuts import render

# Create your views here.
from polls.models import Question, Answer

def answered_questions(request, user_id):
    all_answers = Answer.objects.filter(user=user_id)
    answered_questions = Question.objects.filter(answers__in=all_answers)
    print(answered_questions)

    # print(all_answers)
    context = {
        'answered_questions':answered_questions
    }
    return render(request, 'users/answered_questions_list.html', context)

def all_questions(request, user_id):
    all_questions = Question.objects.all()

    context = {
        'all_questions':all_questions
    }
    return render(request, 'users/all_questions_list.html', context)