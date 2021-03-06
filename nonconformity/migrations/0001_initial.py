# Generated by Django 3.1.4 on 2020-12-29 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nonconformity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField(max_length=1000)),
                ('Occurrence Date', models.DateTimeField()),
                ('state', models.CharField(choices=[('NEW_REPORT', 'New Report'), ('IN_EXAMINATION', 'In Examination'), ('IN_ACTION', 'In Action'), ('COMPLETED', 'Completed')], default='NEW_REPORT', max_length=15)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nonconformity.employee', verbose_name='Related Employee')),
            ],
        ),
    ]
