from django.db import models

class StatesList(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50)

    class Meta:
        db_table = "statelist"

    def __str__(self) -> str:
        return self.state_name

class DistrictList(models.Model):
    district_id = models.IntegerField(primary_key=True)
    district_name = models.CharField(max_length=100)
    state_id = models.IntegerField()

    class Meta:
        db_table = "districtlist"

    def __str__(self) -> str:
        return self.district_name





