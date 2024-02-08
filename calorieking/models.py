from django.db import models

# Create your models here.
class ApiData(models.Model):
    query = models.CharField(max_length=200)
    calories = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)

    def __str__(self):

        return self.query, self.calories, self.carbs, self.protein
    
class CalorieResult(models.Model):
    meal1 = models.IntegerField()
    meal2 = models.IntegerField()
    meal3 = models.IntegerField()
    goal1 = models.IntegerField()
    month1 = models.IntegerField(default=12)
    day1 = models.IntegerField(default=1)
    year1 = models.IntegerField(default=23)
    
    
    def cal_result(self):
        return self.meal1 + self.meal2 + self.meal3
    def goal(self):
        return int(float(self.goal1))
    def month(self):
        return int(float(self.month1))
    def day(self):
        return int(float(self.day1))
    def year(self):
        return int(float(self.year1))
  
    
class Macros(models.Model):
    carb1 = models.IntegerField()
    carb2 = models.IntegerField()
    carb3 = models.IntegerField()
    pro1 = models.IntegerField()
    pro2 = models.IntegerField()
    pro3 = models.IntegerField()
    def carb_result(self):
        return self.carb1 + self.carb2 + self.carb3
    
    def pro_result(self):
        return self.pro1 + self.pro2 + self.pro3
