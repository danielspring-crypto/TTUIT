from django.db import models

# Create your models here.
class Supervisor(models.Model):
	supervisor = models.CharField(max_length=30)
	supervisor_ph = models.CharField(max_length=30, null=True)
	supervisor_email = models.EmailField(max_length=50, null=True)
	group = models.IntegerField()

	def __str__(self):
		return self.supervisor

class Seminar1(models.Model):
	student_name = models.CharField(max_length=30)
	thesis_title = models.CharField(max_length=100)
	student_roll = models.CharField(max_length=30)
	student_ph = models.CharField(max_length=30, null=True)
	student_email = models.EmailField(max_length=50, null=True)
	supervisor = models.ForeignKey(Supervisor, models.CASCADE)
	comment = models.TextField(default="good")
	result = models.BooleanField(default=False)
	date = models.DateField()

	def __str__(self):
		return self.student_name


	





