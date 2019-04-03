from __future__ import unicode_literals

from django.db import models


class Diary(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True)
    content = models.CharField(max_length=512, blank=True, null=True)
    read_string = models.CharField(max_length=64, blank=True, null=True)
    like_string = models.CharField(max_length=64, blank=True, null=True)
    img_url = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diary'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class LvyouNote(models.Model):
    field_id = models.CharField(db_column='_id', max_length=256, blank=True, null=True)  # Field renamed because it started with '_'.
    img_url = models.CharField(max_length=256, blank=True, null=True)
    like = models.CharField(max_length=10, blank=True, null=True)
    look_num = models.CharField(max_length=128, blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    note_url = models.CharField(max_length=256, blank=True, null=True)
    intro = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lvyou_note'


class Spot(models.Model):
    spot_name = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    hot_rate = models.FloatField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    month_sold = models.IntegerField(blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    province = models.TextField(blank=True, null=True)
    spot_type = models.IntegerField(blank=True, null=True)
    diary_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spot'


class User(models.Model):
    username = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    is_login = models.IntegerField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_vip = models.IntegerField(blank=True, null=True)
    is_manager = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'