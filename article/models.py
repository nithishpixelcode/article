from django.contrib.auth.models import User, Group
from django.db import models
import datetime

class UserProfile(models.Model):
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user.username
    
class Navigation(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    order = models.IntegerField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    publish = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=datetime.datetime.now())
    
    class Meta:
        ordering = ['order',]
        
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return '%s/' % (self.slug)

    def save(self, **kwargs):
        super(Navigation, self).save(**kwargs)
        try:
            ping_google()
        except Exception:
            pass