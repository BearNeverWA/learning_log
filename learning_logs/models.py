# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text

class Entry(models.Model):
    """有关某个主题的某个知识"""
    topic = models.ForeignKey(Topic)
