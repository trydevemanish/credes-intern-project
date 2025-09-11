from django.db import models

# Create your models here.
class Task(models.Model):
    TASKS_STATUS=[
        ('todo','Todo'),
        ('in_progress','In_Progress'),
        ('done','Done'),
    ]

    title=models.CharField(max_length=120)
    description=models.TextField(max_length=300)
    status=models.TextField(choices=TASKS_STATUS,default='todo')
    assigned_to=models.ForeignKey("users.CustomUser",related_name='tasks',null=True,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} assigned to {self.assigned_to.full_name}'
