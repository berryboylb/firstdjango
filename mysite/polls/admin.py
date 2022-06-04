from django.contrib import admin

from .models import Choice, Question
# Register your models here.


class ChoiceInline(admin.TabularInline):
    #.tabularline is the view otners like stackedLine
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': [
    #      'pub_date'], 'classes': ['collapse']}),
    # ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
