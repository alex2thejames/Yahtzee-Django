# Generated by Django 2.2.7 on 2019-12-20 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yahtzee_app', '0003_account_waiting_for_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('players', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_id', to='yahtzee_app.Account')),
            ],
        ),
    ]
