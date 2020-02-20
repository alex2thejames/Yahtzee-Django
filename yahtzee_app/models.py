from __future__ import unicode_literals
from django.db import models
import re


class AccountManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['r_first_name']) < 2:
            errors["first_name"] = "First Name should be at least 2 characters"
        if len(postData['r_last_name']) < 2:
            errors["last_name"] = "Last Name should be at least 2 characters"
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['r_email']):
            errors['r_email'] = "Invalid email address!"
        if len(postData['r_password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if postData['r_password'] != postData['r_cpassword']:
            errors["password"] = "Passwords do not match!"

        return errors

    def another_validator(self, postData):
        errors = {}
        curr = Account.objects.filter(email=postData['email'])
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['r_email'] = "Invalid email address!"
        elif len(curr) < 1:
            errors["email"] = "Incorrect email or password"
        elif postData['password'] != curr[0].password:
            errors["password"] = "Incorrect email or password"
        return errors


class Account(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    waiting_for_game = models.BooleanField(null=True)
    game_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AccountManager()

class Score(models.Model):
    scored_user=models.ForeignKey(Account,related_name='past_scores' ,on_delete=models.CASCADE)
    Score=models.IntegerField(verbose_name='score')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

# class Game(models.Model):
#     players = models.ForeignKey(Account,related_name='game_id',on_delete=models.CASCADE)
    
    