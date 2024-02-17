from django.contrib.auth.models import AbstractUser
from django.db import models


class Schools(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return f'{self.name}'


class Classes(models.Model):
    name = models.CharField(max_length=126)

    def __str__(self):
        return f'{self.name}'


class User(AbstractUser):
    surname = models.CharField(max_length=126)
    is_teacher = models.BooleanField(
        ("is teacher"),
        default=False,
        help_text=("Является пользователь учителем"))
    number_class = models.CharField(max_length=12)
    school = models.CharField(max_length=126)


class Subject(models.Model):
    name = models.CharField(max_length=56)

    def __str__(self):
        return f'{self.name}'


class Teacher(models.Model):
    name = models.CharField(max_length=126)

    def __str__(self):
        return f'{self.name}'


class Tests(models.Model):
    school = models.ForeignKey(to=Schools, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    number_class = models.ForeignKey(to=Classes, on_delete=models.CASCADE)
    teacher = models.ForeignKey(to=Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='test_images')

    def __str__(self):
        return f'{self.school} ==  {self.number_class} == {self.subject}'


class Questions(models.Model):
    test = models.ForeignKey(Tests, on_delete=models.CASCADE, related_name='questions')
    question = models.TextField()
    answer1 = models.CharField(max_length=512)
    answer2 = models.CharField(max_length=512)
    answer3 = models.CharField(max_length=512)
    true_answer = models.CharField(max_length=512)

    def __str__(self):
        return f'{self.test.school} ==  {self.test.number_class}'
