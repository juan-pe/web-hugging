from aldryn_apphooks_config.fields import AppHookConfigField
from aldryn_apphooks_config.managers import AppHookConfigManager
from django.db import models
from faq.cms_appconfig import FaqConfig


class FaqEntry(models.Model):
    app_config = AppHookConfigField(FaqConfig)

    question = models.TextField(
        blank=True,
        default=''
    )

    answer = models.TextField()

    objects = AppHookConfigManager()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'Faq entries'
