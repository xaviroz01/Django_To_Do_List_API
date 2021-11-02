from django.db import models
from django.db.models.enums import Choices

#status
NOT_COMPLETE = 'NotCompleted'
COMPLETE = 'Completed'
TASK_STATUS_CHOICES = [
    (NOT_COMPLETE, 'Not Completed'),
    (COMPLETE, 'Completed')
]

#type
TASK_TYPE = "Task"
CHORE_TYPE = "Chore"
TYPE_CHOICES = [
    (TASK_TYPE, 'Task'),
    (CHORE_TYPE, 'Chore')
]


class Task(models.Model):

    type = models.CharField(
        max_length=5, 
        choices = TYPE_CHOICES,
        default = TASK_TYPE,)

    task_description = models.TextField()

    status = models.CharField(
        max_length=20, 
        choices = TASK_STATUS_CHOICES,
        default = NOT_COMPLETE,)

    class Meta:
        verbose_name_plural = 'TodoLists'
    

    def __str__(self):
        return f'{self.id} | {self.type}'