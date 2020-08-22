from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice

#--------------------------------------------------------------------------------------------------
# admin.site.register(Question)         #for display question model in admin panel
# admin.site.register(Choice)         #for display choice model in admin panel
#--------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
#                                                     #for update and change order model form
# admin.site.register(Question,QuestionAdmin)
# admin.site.register(Choice)
#--------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),      #for form up into fieldsets
#     ]

# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
#--------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------
# class ChoiceInline(admin.StackedInline): # "admin.StackedInline" is use for show model list wise 
#     model = Choice
#     extra = 3


# class QuestionAdmin(admin.ModelAdmin): 
#     fieldsets = [                      
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]  #Choice objects are edited on the Question admin page

# admin.site.register(Question, QuestionAdmin)
#--------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------
class ChoiceInline(admin.TabularInline): # "admin.TabularInline" is use for show model table wise 
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin): 
    # list_display = ('question_text', 'pub_date')  # show question extra information
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date'] #for filter
    search_fields = ['question_text'] # search box
    fieldsets = [                      
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]  #Choice objects are edited on the Question admin page

admin.site.register(Question, QuestionAdmin)
#--------------------------------------------------------------------------------------------------