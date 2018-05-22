# Generated by Django 2.0.3 on 2018-04-02 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='skill_related',
        ),
        migrations.AddField(
            model_name='courses',
            name='skill_related',
            field=models.ManyToManyField(blank=True, related_name='rel1_t0o_set', to='student.Skill'),
        ),
    ]
