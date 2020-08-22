from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


'''
url pattern (index page) - (url - "localhost:8000/polls/1/")
1. hardcoded path like - tightly-coupled approach
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>

2. URL paths defined in your url configurations by using the {% url %} template tag and URL name of ‘detail’ is defined
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>

3. Namespace url name - In real Django projects, there might be five, ten, twenty apps or more. (reverse name space url find)
app_name = 'polls'
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
------------------------------------------------------------------------------------
urlpatterns = [
	# ex: /polls/
	path('' , views.index, name='index'),
	# ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
Use generic views: Less code is better
a. Convert the URLconf.
b. Delete some of the old, unneeded views.
c. Introduce new views based on Django’s generic views.
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
'''