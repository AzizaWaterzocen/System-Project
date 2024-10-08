import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

def set_default_periods(apps, schema_editor):
    Attendance = apps.get_model('login', 'Attendance')
    for attendance in Attendance.objects.all():
        attendance.periods = 1  # or another suitable default integer value
        attendance.save()

class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_delete_temp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('period_id', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)])),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='attendance',
            name='periods',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)]),  # Change default to a valid integer
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.class')),
                ('fac_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=100)),
                ('leave_type', models.CharField(choices=[('ml', 'Medical Leave'), ('od', 'On Duty')], default=None, max_length=9)),
                ('approved', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('stud_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.student')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='timetable',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='timetable',
            name='periods_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.slot'),  # Change default to a valid integer
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='timetable',
            unique_together={('class_id', 'course_id', 'day', 'periods_id')},
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='periods',
        ),
    ]
