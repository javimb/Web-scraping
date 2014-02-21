from datetime import date
from itertools import chain

from django.db import models


class FilmManager(models.Manager):

    def get_today_films(self):
        return self.filter(day=date.today())

    def get_today_films_order_by_hour(self):
        pre = self.get_today_films().filter(hour__gte='06:00').order_by('hour')
        post = self.get_today_films().filter(hour__lt='06:00').order_by('hour')
        return list(chain(pre, post))

    def get_today_films_by_channel_order_by_hour(self, channel):
        pre = self._get_today_films_by_channel(channel).filter(hour__gte='06:00').order_by('hour')
        post = self._get_today_films_by_channel(channel).filter(hour__lt='06:00').order_by('hour')
        return list(chain(pre, post))

    def _get_today_films_by_channel(self, channel):
        return self.get_today_films().filter(channel=channel)


class Film(models.Model):
    title = models.CharField(max_length=50)
    channel = models.CharField(max_length=50)
    day = models.DateField(auto_now_add=True)
    hour = models.TimeField()
    rating = models.CharField(max_length=4)
    url = models.URLField()

    objects = FilmManager()

    def __unicode__(self):
        return self.title

