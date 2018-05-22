from django.db import models
from account.models import *
# Create your models here.
class Skill(models.Model):
    name= models.CharField(verbose_name='Skill',max_length=20)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    skills_opened= models.ManyToManyField(Skill,related_name='rel_t9o_set',blank=True)
    college_com = models.CharField(verbose_name='College or Company', max_length=500, blank=False, null=False)
    year = models.CharField(verbose_name='Year', max_length=4, blank=True, null=True)
    address = models.TextField(verbose_name='Address', max_length=400, blank=True, null=False)
    City = models.CharField(verbose_name='City', max_length=60,blank=True, null=False)
    state = models.CharField(verbose_name='state', max_length=80)
    rating =models.PositiveIntegerField(default='500')
    def __str__(self):
        return self.user.email

class Teacher(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    skills_allowed= models.ManyToManyField(Skill,related_name='rel_t0o_set',blank=True)
    college_com = models.CharField(verbose_name='College or Company', max_length=500, blank=False, null=False)
    year = models.CharField(verbose_name='Year', max_length=4,blank=True, null=True)
    address = models.TextField(verbose_name='Address', max_length=400, blank=True, null=False)
    City = models.CharField(verbose_name='City', max_length=60,blank=True, null=False)
    state = models.CharField(verbose_name='state', max_length=60)
    ifsccode = models.CharField(verbose_name='IFSC Code',max_length=255, null=True, blank=True)
    bank_name = models.CharField(verbose_name='bank_name', max_length=70)
    account_no = models.CharField(verbose_name='account_no',max_length=70)
    total_earned =models.PositiveIntegerField(default='0')
    rating =models.PositiveIntegerField(default='500')
    def __str__(self):
        return self.user.email



class Question(models.Model):
    doubt= models.TextField(verbose_name='Question')
    skill_related = models.ForeignKey(Skill,related_name='rel_t1o_set',on_delete=models.CASCADE,null=True,blank=True)
    asked_by = models.ForeignKey(MyUser,related_name='rel_t3o_set',on_delete=models.CASCADE,null=True)
    solved_by = models.ForeignKey(MyUser,related_name='rel_to_set',on_delete=models.CASCADE,null=True,blank=True)
    is_taken= models.BooleanField(default=False)
    is_solved=models.BooleanField(default=False)
    base_price=models.PositiveIntegerField(default='30')
    def __str__(self):
        return self.doubt


class Courses(models.Model):
    name= models.CharField(max_length=50)
    skill_related= models.ForeignKey(Skill,related_name='rel1_t1o_set',on_delete=models.CASCADE,null=True,blank=True)
    cost=models.PositiveIntegerField(default='20000')
    def __str__(self):
        return self.name + str(self.skill_related)