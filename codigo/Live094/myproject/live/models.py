from django.db import models
from django.contrib.auth.models import User
from myproject.core.models import TimeStampedModel


class Live(TimeStampedModel):
    number = models.IntegerField('número')
    title = models.TextField('título')
    guest = models.ForeignKey(
        User,
        related_name='guests',
        verbose_name='convidados',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    like = models.PositiveIntegerField('gostou', null=True, blank=True)
    unlike = models.PositiveIntegerField('não gostou', null=True, blank=True)

    class Meta:
        ordering = ('number',)
        verbose_name = "live"
        verbose_name_plural = "lives"

    def __str__(self):
        return self.title

    @property
    def like_frequence(self):
        if self.like:
            return self.unlike / self.like

    def to_dict_json(self):
        data = {
            'pk': self.pk,
            'title': self.title,
            'like': self.like,
            'unlike': self.unlike,
        }
        if self.guest:
            data['guest'] = self.guest.get_full_name()
        return data
