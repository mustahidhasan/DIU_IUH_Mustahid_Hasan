from django.db import models

# Create your models here.

class bus_details(models.Model):
    bus_name = models.CharField(max_length=100, blank=True)
    lisence_no = models.CharField(max_length=100, blank=False)

class bus_route(models.Model):
    lisence_no = models.CharField(max_length=100, blank=False)

    point_one = models.CharField(max_length=50, blank=True)
    point_two = models.CharField(max_length=50, blank=True)
    point_three = models.CharField(max_length=50, blank=True)
    point_four = models.CharField(max_length=50, blank=True)
    point_five = models.CharField(max_length=50, blank=True)
    point_six = models.CharField(max_length=50, blank=True)
    point_seven = models.CharField(max_length=50, blank=True)
    point_eight = models.CharField(max_length=50, blank=True)
    point_nine = models.CharField(max_length=50, blank=True)
    point_ten = models.CharField(max_length=50, blank=True)

class bus_fare(models.Model):
    lisence_no = models.CharField(max_length=100, blank=False)
    start_point = models.CharField(max_length=50, blank=False, null=False)
    end_point = models.CharField(max_length=50, blank=False,null=False)
    fair = models.FloatField(blank=False, null=False)