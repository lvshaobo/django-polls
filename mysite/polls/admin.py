from django.contrib import admin

# Register your models here.

from .models import Question
from .models import Choice

"""
admin.site.register(Question)
"""

"""
class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text', 'pub_date']
"""

"""
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Choice)
"""

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')




admin.site.register(Question, QuestionAdmin)
