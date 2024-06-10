from django.db import models


class InstrumentType(models.Model):
    instrument_type_name = models.CharField(max_length=500)


class Instrument(models.Model):
    instrument_type = models.ForeignKey(InstrumentType, on_delete=models.CASCADE)
    instrument_name = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Oven(Instrument):
    max_temp = models.IntegerField()
    max_dim_W = models.IntegerField()
    max_dim_L = models.IntegerField()
    max_dim_H = models.IntegerField()
    max_capacity = models.IntegerField()


class Mixer(Instrument):
    max_speed = models.IntegerField()
    min_speed = models.IntegerField()


class ActionType(models.Model):
    action_type_name = models.CharField(max_length=500)


class Action(models.Model):
    action_type = models.ForeignKey(ActionType, on_delete=models.CASCADE)
    action_name = models.CharField(max_length=500)


class Workflows(models.Model):
    workflow_name = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    created_by = models.CharField(max_length=500, blank=True)
