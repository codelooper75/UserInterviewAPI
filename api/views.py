from rest_framework import generics, permissions
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from polls.models import Poll, Question, Answer

from api import serializers
# class QuestionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,  mixins.CreateModelMixin):
#     #n ViewSet groups bunch of views (list, create, retrive, update, partila_update, destroy)
#
#     """Manage ingredients in the database"""
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#
#     def perform_create(self, serializer):
#         """Create a new object"""
#         serializer.save(user=self.request.user)
#


class QuestionViewSet(viewsets.ModelViewSet):
    """
        A viewset that provides default `create()`, `retrieve()`, `update()`,
        `partial_update()`, `destroy()` and `list()` actions.
        """

    queryset = Question.objects.all()
    serializer_class =serializers.QuestionSerializer


class PollViewSet(viewsets.ModelViewSet):
    """
        A viewset that provides default `create()`, `retrieve()`, `update()`,
        `partial_update()`, `destroy()` and `list()` actions.
        """
    serializer_class = serializers.PollSerializer
    queryset = Poll.objects.all()

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        #n default action is "list" seems like
        if self.action == 'retrieve':
            return serializers.PollDetailSerializer

        return self.serializer_class


class PollQuestionAddRemove(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,):
    """
    Create will add question(s)
    Destroy will remove questions(s)

     """


#n Class based view removes question but faild to return proper data so there is error
# def remove_question_from_poll(request, poll_id, question_id):
#     poll = Poll.objects.get(pk=poll_id)
#     question = Question.objects.get(pk=question_id)
#
#     poll.questions.remove(question)
#     poll.save()
#     serializer = serializers.PollDetailSerializer(poll)
#     print(serializer.data)
#     return Response(serializer.data)
#     # productobj= get_object_or_404(Product, id=id)
#     #
#     # shoppingcart= ShoppingCart()
#     #
#     # shoppingcart.products.remove(productobj)
#
#     # return render(request, 'thispage.html')




# class PollListCreate(generics.ListCreateAPIView): #note GET for list, POST for crating new instance
#
#     serializer_class = PollSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         # user = self.request.user
#         return Poll.objects.all()
#
#     # def perform_create(self, serializer): #note adding current user as user
#     #     serializer.save(user=self.request.user)


