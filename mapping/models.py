from django.db import models

# Create your models here.
class Person(models.Model):
    full_name=models.CharField(max_length=50,default="True")
    adhaar=models.CharField(max_length=20)
    def __unicode__(self):
        return self.full_name


class Car(models.Model):
    car_name=models.CharField(max_length=30)
    car_number=models.CharField(max_length=20,default="True")
    Owner=models.ForeignKey(Person,on_delete=models.CASCADE)
    def __unicode__(self):
        return self.car_name

class Department(models.Model):
    department_id=models.CharField(max_length=10)
    department_name=models.CharField(max_length=30)
    budget=models.CharField(max_length=10)
    def __unicode__(self):
        return self.department_name

class Student(models.Model):
    student_name=models.CharField(max_length=30)
    age=models.CharField(max_length=3)
    address=models.CharField(max_length=50)
    roll_number=models.CharField(max_length=10)
    allocated_department=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __unicode__(self):
        return self.student_name

class Game(models.Model):
    name=models.CharField(max_length=30)
    number_of_players=models.CharField(max_length=2)
    def __unicode__(self):
        return self.name

class Athlete(models.Model):
    athlete_name=models.CharField(max_length=30)
    age=models.CharField(max_length=3)
    games=models.ManyToManyField(Game)
    def __unicode__(self):
        return self.athlete_name

class Registration(models.Model):
    registration_id=models.ForeignKey(Athlete,on_delete=models.CASCADE)
    game_name=models.ManyToManyField(Game)
    registration_date=models.DateField()
    comment=models.CharField(max_length=100, blank=True)
    def __str__(self):
        return str(self.registration_id)
