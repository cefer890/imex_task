from django.db import models
from custom_users.models import MyUser as User
# Create your models here.


class ManageTask(models.Model):
    user = models.ManyToManyField(User, related_name='user_email', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    ACTIVE = 0
    DEACTIVE = 1
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DEACTIVE, 'Deactive'),
    )
    status = models.SmallIntegerField(default=ACTIVE, choices=STATUS_CHOICES)

    class Meta:
        verbose_name_plural = 'Manage Tasks'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
