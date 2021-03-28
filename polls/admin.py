from django.contrib import admin
from .models import Question, Answer, Poll
#
# admin.site.register(Question)
# admin.site.register(Answer)
# admin.site.register(Poll)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id',"body",)
    list_display_links = ("body",)
    search_fields = ('body',)

    readonly_fields = ('id',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id','question','body','user')
    list_display_links = ("question",)
    search_fields = ('question','body','user')
    list_filter = ("question",'user')

    readonly_fields = ('id',)


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'started_at', )
    list_display_links = ("title",)
    search_fields = ('title', 'description',)
    # list_filter = ("question", 'user')

    readonly_fields = ('id',)
