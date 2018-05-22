from django.conf.urls import include, url
from . import views

urlpatterns = [
url(r'^student/dashboard/$',views.stu_dashboard,name='student_dashboard'),
url(r'^teacher/dashboard/$',views.tea_dashboard,name='teacher_dashboard'),
url(r'^student/askquestion/$',views.Questionf,name='ask_question'),
]