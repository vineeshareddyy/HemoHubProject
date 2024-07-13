from django.db import models

class PersonData(models.Model):
    Person_Name = models.CharField(max_length=500)
    Blood_Type = models.CharField(max_length=200)
    Component = models.CharField(max_length=500)
    Quantity = models.IntegerField()
    Expiry_Date = models.DateField(null=True)

    def __str__(self):
        return self.Person_Name

class Notification(models.Model):
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    person_data = models.ForeignKey(PersonData, on_delete=models.CASCADE)
