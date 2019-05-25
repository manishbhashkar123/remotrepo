from django.db import models
from multiselectfield import MultiSelectField

class FeedbackData(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField()
    date=models.DateTimeField()
    feedback=models.TextField(max_length=2000)

class ContactData(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100)

    COURSES_CHOICES = (
        ('Py','Python'),
        ('Dj','Django'),
        ('API','REST API'),
        ('UI','UI')
    )
    courses = MultiSelectField(max_length=200,choices=COURSES_CHOICES)

    LOCATION_CHOICES = (
        ('Hyd','Hyderabad'),
        ('Bang','Bangalore'),
        ('Che','Chennai'),
        ('Pune','Pune')
    )
    locations = MultiSelectField(max_length=200, choices=LOCATION_CHOICES)

    SHIFT_CHOICES = (
        ('Morg','Morning'),
        ('Aftn','AfterNoon'),
        ('Evng','Evening'),
        ('Ngt','Night')
    )
    shifts = MultiSelectField(max_length=200,choices=SHIFT_CHOICES)

    gender = models.CharField(max_length=100)
    batch_start_date = models.DateField(max_length=100)


class CoursesData(models.Model):
    course_id=models.IntegerField()
    course_name=models.CharField(max_length=100)
    course_dur=models.IntegerField()
    course_fee=models.IntegerField()
    start_date=models.DateField(max_length=100)
    start_time=models.TimeField(max_length=100)
    trainer_name=models.CharField(max_length=100)
    trainer_exp=models.IntegerField()

