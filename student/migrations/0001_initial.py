# Generated by Django 2.0.3 on 2018-03-30 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doubt', models.TextField(verbose_name='Question')),
                ('is_taken', models.BooleanField(default=False)),
                ('is_solved', models.BooleanField(default=False)),
                ('base_price', models.PositiveIntegerField(default='30')),
                ('asked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_t3o_set', to=settings.AUTH_USER_MODEL)),
                ('solved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_to_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Skill')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_com', models.CharField(max_length=500, verbose_name='College or Company')),
                ('year', models.CharField(blank=True, max_length=4, null=True, verbose_name='Year')),
                ('address', models.TextField(blank=True, max_length=400, verbose_name='Address')),
                ('City', models.CharField(blank=True, max_length=60, verbose_name='City')),
                ('state', models.CharField(max_length=80, verbose_name='state')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_com', models.CharField(max_length=500, verbose_name='College or Company')),
                ('year', models.CharField(blank=True, max_length=4, null=True, verbose_name='Year')),
                ('address', models.TextField(blank=True, max_length=400, verbose_name='Address')),
                ('City', models.CharField(blank=True, max_length=60, verbose_name='City')),
                ('state', models.CharField(max_length=60, verbose_name='state')),
                ('ifsccode', models.CharField(blank=True, max_length=255, null=True, verbose_name='IFSC Code')),
                ('bank_name', models.CharField(max_length=70, verbose_name='bank_name')),
                ('account_no', models.CharField(max_length=70, verbose_name='account_no')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
