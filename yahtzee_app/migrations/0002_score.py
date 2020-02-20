# Generated by Django 2.2.7 on 2019-12-19 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yahtzee_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Score', models.IntegerField(verbose_name='score')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('scored_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='past_scores', to='yahtzee_app.Account')),
            ],
        ),
    ]