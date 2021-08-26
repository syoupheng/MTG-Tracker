# Generated by Django 3.2.6 on 2021-08-20 16:29

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expansion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DraftResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('best_of', models.CharField(choices=[('BO1', 'Best of one'), ('BO3', 'Best of three')], default='BO1', max_length=5)),
                ('deck_title', models.CharField(max_length=100, null=True)),
                ('nb_wins', models.IntegerField(validators=[django.core.validators.MaxValueValidator(7, message='Le nombre de victoires ne peut être supérieur à 7 !')])),
                ('nb_losses', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='Le nombre de défaites ne peut être inférieur à 0 !'), django.core.validators.MaxValueValidator(3, message='Le nombre de victoires ne peut être supérieur à 3 !')])),
                ('colors', models.CharField(max_length=5)),
                ('expansion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MTG_Tracker.expansion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]