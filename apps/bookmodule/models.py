from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)

class Address(models.Model):
    # ID field is created automatically by Django
    city = models.CharField(max_length=100)  # String field for the city name

    def __str__(self):
        return self.city  # Display city name in the admin or query results

class Student(models.Model):
    # ID field is created automatically by Django
    name = models.CharField(max_length=100)  # String field for the student's name
    age = models.IntegerField()              # Integer field for the age
    address = models.ForeignKey(             # Foreign key relationship
        Address, 
        on_delete=models.CASCADE,            # Delete students if the address is deleted
        related_name="students"              # Reverse name for querying students by address
    )

    def __str__(self):
        return self.name  # Display student name in the admin or query results
