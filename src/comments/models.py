from django.db import models

# Create your models here.
class Comment(models.Model):
    task=models.ForeignKey("tasks.Task",null=True,related_name="comments" ,on_delete=models.CASCADE)
    author=models.ForeignKey("users.CustomUser",null=True,related_name="comments" , on_delete=models.CASCADE)
    text=models.CharField(max_length=400)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.author and self.task:
            return f'{self.author.full_name} added comment on {self.task.title}'
        return f'{self.author} added comment on task with id:{self.task}'