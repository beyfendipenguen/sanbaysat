from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import UserAccount
# Create your models here.


class Factory(models.Model):
    factory_user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    factory_address = models.CharField(max_length=150)
    factory_name = models.CharField(max_length=150)
    factory_city = models.CharField(max_length=30)
    factory_country = models.CharField(max_length=30)

    class Meta:
        verbose_name = _("Factory")
        verbose_name_plural = _("Factorys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Factory_detail", kwargs={"pk": self.pk})
