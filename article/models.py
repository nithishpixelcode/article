from django.contrib.auth.models import User, Group
from django.db import models
import datetime

class Country(models.Model):
    """
    International Organization for Standardization (ISO) 3166-1 Country list
     * ``iso`` = ISO 3166-1 alpha-2
     * ``name`` = Official country names used by the ISO 3166/MA in capital letters
     * ``printable_name`` = Printable country names for in-text use
     * ``iso3`` = ISO 3166-1 alpha-3
     * ``numcode`` = ISO 3166-1 numeric
    
    Note::
    This model is fixed to the database table 'country' to be more general.
    Change ``db_table`` if this cause conflicts with your database layout.
    Or comment out the line for default django behaviour.
    """
    iso = models.CharField(max_length=2, null=True, default='IN')
    name = models.CharField(max_length=128, null=False, default='India')
    printable_name = models.CharField(max_length=128, null=True, default='India')
    iso3 = models.CharField(max_length=3, null=True, default='IND')
    numcode = models.PositiveSmallIntegerField(null=True, default=91 )
    
    class Meta:
        ordering = ['numcode', 'name',]
        verbose_name_plural = 'Countries'
    
    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    country  = models.ForeignKey(Country, default = 1)
    profile_pic = models.ImageField(upload_to="images/profile_pics", default="images/default_profile.png")

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