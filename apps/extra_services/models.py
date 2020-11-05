from django.db import models


class ExtraServiceCategory(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class ExtraService(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    extra_service_category = models.ForeignKey(ExtraServiceCategory, on_delete=models.CASCADE,default=None)





