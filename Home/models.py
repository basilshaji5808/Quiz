from django.db import models


# Create your models here.
class Python(models.Model):
    question = models.CharField(max_length=200, null=True)
    opt1 = models.CharField(max_length=200, null=True)
    opt2 = models.CharField(max_length=200, null=True)
    opt3 = models.CharField(max_length=200, null=True)
    opt4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.question


class Django(models.Model):
    question = models.CharField(max_length=200, null=True)
    opt1 = models.CharField(max_length=200, null=True)
    opt2 = models.CharField(max_length=200, null=True)
    opt3 = models.CharField(max_length=200, null=True)
    opt4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.question


class Angular(models.Model):
    question = models.CharField(max_length=200, null=True)
    opt1 = models.CharField(max_length=200, null=True)
    opt2 = models.CharField(max_length=200, null=True)
    opt3 = models.CharField(max_length=200, null=True)
    opt4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.question


class React(models.Model):
    question = models.CharField(max_length=200, null=True)
    opt1 = models.CharField(max_length=200, null=True)
    opt2 = models.CharField(max_length=200, null=True)
    opt3 = models.CharField(max_length=200, null=True)
    opt4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.question


class JavaScript(models.Model):
    question = models.CharField(max_length=200, null=True)
    opt1 = models.CharField(max_length=200, null=True)
    opt2 = models.CharField(max_length=200, null=True)
    opt3 = models.CharField(max_length=200, null=True)
    opt4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.question


class Java(models.Model):
    question = models.CharField(max_length=200, null=True)
    opt1 = models.CharField(max_length=200, null=True)
    opt2 = models.CharField(max_length=200, null=True)
    opt3 = models.CharField(max_length=200, null=True)
    opt4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.question


class PHP(models.Model):
    question = models.CharField(max_length=200, null=True)
    opt1 = models.CharField(max_length=200, null=True)
    opt2 = models.CharField(max_length=200, null=True)
    opt3 = models.CharField(max_length=200, null=True)
    opt4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.question


class Dot_Net(models.Model):
    question = models.CharField(max_length=200, null=True)
    opt1 = models.CharField(max_length=200, null=True)
    opt2 = models.CharField(max_length=200, null=True)
    opt3 = models.CharField(max_length=200, null=True)
    opt4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.question


class Node_JS(models.Model):
    question = models.CharField(max_length=200, null=True)
    opt1 = models.CharField(max_length=200, null=True)
    opt2 = models.CharField(max_length=200, null=True)
    opt3 = models.CharField(max_length=200, null=True)
    opt4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.question
