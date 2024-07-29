from django.db import models

class UserData(models.Model):
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    class Meta:
        db_table = 'tb_users'

    def __int__(self):
        return self.user_id if self.user_id else str(self.id)