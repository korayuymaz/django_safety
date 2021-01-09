from django.db import models

from datetime import datetime

from django.urls import reverse


class Employee(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Nonconformity(models.Model):
    STATES = [
        ('NEW_REPORT', 'New Report'),
        ('IN_EXAMINATION', 'In Examination'),
        ('IN_ACTION', 'In Action'),
        ('COMPLETED', 'Completed')
    ]
    TYPE = [
        ('NEAR_MISS', 'Near Miss'),
        ('WORK_ACCIDENT', 'Work Accident'),
        ('UNSAFE_ACT', 'Unsafe Act'),
        ('UNSAFE_CONDITION', 'Unsafe Condition'),
    ]
    description = models.TextField(max_length=1000)
    occ_date = models.DateTimeField(default=datetime.now())
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name="Related Employee",
    )
    state = models.CharField(
        max_length=15,
        choices=STATES,
        default='NEW_REPORT',
    )

    type = models.CharField(
        max_length=20,
        choices=TYPE,
        default='NEAR_MISS',
    )

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('nonconformity:detail', kwargs={'pk': self.pk})
