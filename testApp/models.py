from django.db import models
from pydantic import BaseModel, Field 
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Actor(models.Model):
    """
      test model for Actors
    """

    name = models.CharField(verbose_name="TestApp name", max_length=90)
    data = models.JSONField(verbose_name="TestApp json data")

    class Meta:
        db_table = ""
        verbose_name = ""
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Film(models.Model):
    """
      test model for  Films
    """

    title = models.CharField(max_length=90)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, blank=True, null= True)
    year = models.DateField(auto_now=False, auto_now_add=False)
    duration = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.JSONField()

    class Meta:
        verbose_name = _("DefaultApp")
        verbose_name_plural = _("Defa   title = ultApps")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("DefaultApp_detail", kwargs={"pk": self.pk})


class MainModel(BaseModel):
    actor: Actor = Field(...)
    film: Film = Field(None)

    class Config:
        arbitrary_types_allowed = True