"""admin utility"""
from django.contrib import admin
from firstapp.models import Question, Choice
# Register your models here.


class ChoiceAdmin(admin.ModelAdmin):
    """customize choice model admin"""
    list_display = ('id', 'choice_text', 'votes')
    readonly_fields = ('id',)


class QuestionAdmin(admin.ModelAdmin):
    """customize question model admin"""
    list_display = ('id', 'question_text', 'published_date')
    readonly_fields = ('id',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
