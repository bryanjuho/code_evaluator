# Generated by Django 4.0.4 on 2022-05-28 09:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import evaluator.utils


class Migration(migrations.Migration):

    dependencies = [
        ('evaluator', '0016_assignment_answer_code_alter_assignment_attachment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='answer_code',
            field=models.FileField(upload_to=evaluator.utils.FilenameChanger('answer_codes'), validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['c', 'cpp'])], verbose_name='Answer Code'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='evaluator.classroom', verbose_name='Classroom'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='semester',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='classrooms', to='evaluator.semester', verbose_name='Semester'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='file',
            field=models.FileField(upload_to=evaluator.utils.FilenameChanger('submissions'), validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['c', 'cpp'])], verbose_name='File'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
