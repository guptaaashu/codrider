from django.contrib import admin

# Register your models here.
from . models import *

# Register your models here.
admin.site.register(Question)
admin.site.register(Skill)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Courses)
