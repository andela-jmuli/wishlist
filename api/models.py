from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Bucketlist(models.Model):
    """ Bucketlist model class """
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=100, blank=True, default='None')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bucketlists')

    def __unicode__(self):
        return "{} : {}".format(self.id, self.name)

    class Meta:
        unique_together = ("name", "created_by")


class BucketlistItem(models.Model):
    """ Bucketlist item model class """
    item_name = models.CharField(max_length=50, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    bucketlist = models.ForeignKey(Bucketlist, on_delete=models.CASCADE, related_name='bucketlist_items')
    is_done = models.BooleanField(default=False)

    def __unicode__(self):
        return "{}".format(self.item_name)

    class Meta:
        unique_together = ("item_name", "bucketlist")
