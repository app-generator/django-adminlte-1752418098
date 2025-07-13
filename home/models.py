# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Projetos(models.Model):

    #__Projetos_FIELDS__
    id_clickup = models.CharField(max_length=255, null=True, blank=True)
    nome = models.CharField(max_length=255, null=True, blank=True)
    lider = models.CharField(max_length=255, null=True, blank=True)

    #__Projetos_FIELDS__END

    class Meta:
        verbose_name        = _("Projetos")
        verbose_name_plural = _("Projetos")


class Forum(models.Model):

    #__Forum_FIELDS__
    cod_proj = models.ForeignKey(Projetos, on_delete=models.CASCADE)
    data_forum = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.TextField(max_length=255, null=True, blank=True)
    acao = models.BooleanField()
    data_fup = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Forum_FIELDS__END

    class Meta:
        verbose_name        = _("Forum")
        verbose_name_plural = _("Forum")



#__MODELS__END
