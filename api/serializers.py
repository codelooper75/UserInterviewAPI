from rest_framework import serializers
from polls.models import Poll, Question, Answer

from rest_framework import serializers

from polls.models import Poll, Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    """Serializer for question objects"""

    class Meta:
        model = Question
        fields = ('id','body',)
        read_only_fields = ('id',)

class PollSerializer(serializers.ModelSerializer):
    """Serializer for poll objects"""
    # created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S") #todo fix format from  "2021-02-17T13:38:01.904004Z" to something decent

    questions = serializers.PrimaryKeyRelatedField(  # n lists only id of ingridents (for other field user will user detail view)
        many=True,
        queryset=Question.objects.all()
    )

    class Meta:
        model = Poll
        fields = ('id', 'title', 'description', 'questions', 'created_at', 'started_at', )
        read_only_fields = ('id', 'created_at', 'started_at',)



class PollDetailSerializer(PollSerializer):
    """Serialize a recipe detail"""
    #n here we are nesting serializers inside each other
    questions = QuestionSerializer(many=True, read_only=True) #n now it returns list of object with all the fields. Without "read_only" it won't work







# class IngredientSerializer(serializers.ModelSerializer):
#     """Serializer for ingredient objects"""
#
#     class Meta:
#         model = Ingredient
#         fields = ('id', 'name')
#         read_only_fields = ('id',)
#
#
# class RecipeSerializer(serializers.ModelSerializer):
#     """Serialize a recipe"""
#     #n ingredients and tags are not part of serializer, they are references to other models, so we need to add two vars
#     ingredients = serializers.PrimaryKeyRelatedField( #n lists only id of ingridents (for other field user will user detail view)
#         many=True,
#         queryset=Ingredient.objects.all()
#     )
#     tags = serializers.PrimaryKeyRelatedField(
#         many=True,
#         queryset=Tag.objects.all()
#     )
#
#     class Meta:
#         model = Recipe
#         fields = (
#             'id', 'title', 'ingredients', 'tags', 'time_minutes', 'price', 'link'
#         )
#         read_only_fields = ('id',)
#
#
# class RecipeDetailSerializer(RecipeSerializer):
#     """Serialize a recipe detail"""
#     #n here we are nesting serializers inside each other
#     ingredients = IngredientSerializer(many=True, read_only=True) #n now it returns list of object with all the fields. Without "read_only" it won't work
#     tags = TagSerializer(many=True, read_only=True)




#
# class PollSerializer(serializers.ModelSerializer):
#     created_at = serializers.ReadOnlyField()           #note we should not be able to change it
#     started_at = serializers.ReadOnlyField()     #note we should not be able to change it
#
#     class Meta:
#         model = Poll
#         fields = ['id','title','description','created_at','started_at']



    # title = models.CharField(verbose_name='Заголовок', max_length=200)
    # description = models.TextField(verbose_name='Описание', blank=True, null=True)
    # created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    # started_at = models.DateTimeField(verbose_name='Начат',auto_now=False, auto_now_add=False,blank=True, null=True)
    # questions = models.ManyToManyField(Question, related_name='poll', blank=True)






#
# class TodoCompleteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Todo
#         fields = ['id']
#         read_only_fields = ['title','memo','created','datecompleted','important'] #
