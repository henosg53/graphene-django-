from django.contrib import admin
from .models import Question,Quizzes,Answer,Category
# Register your models here.
admin.site.register(Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]
class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = [
        'answer_text',
        'is_right'
    ]
admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz',
    ]
    list_display = [
        'title',
        'quiz'
    ]
    inlines = [
        AnswerInlineModel,
    ]
admin.site.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'is_right',
        'question'
    ]
admin.site.register(Category)
class CatAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]