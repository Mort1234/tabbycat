# Generated by Django 5.0.6 on 2024-11-05 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adjfeedback", "0016_question_and_more"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.AlterModelTable(
                    name=table,
                    table=f'registration_{table}',
                )
                for table in ('booleananswer', 'floatanswer', 'integeranswer', 'manyanswer', 'stringanswer', 'question')
            ],
            state_operations=[
                migrations.RemoveField(
                    model_name="booleananswer",
                    name="content_type",
                ),
                migrations.RemoveField(
                    model_name="booleananswer",
                    name="question",
                ),
                migrations.RemoveField(
                    model_name="floatanswer",
                    name="content_type",
                ),
                migrations.RemoveField(
                    model_name="floatanswer",
                    name="question",
                ),
                migrations.RemoveField(
                    model_name="integeranswer",
                    name="content_type",
                ),
                migrations.RemoveField(
                    model_name="integeranswer",
                    name="question",
                ),
                migrations.RemoveField(
                    model_name="manyanswer",
                    name="content_type",
                ),
                migrations.RemoveField(
                    model_name="manyanswer",
                    name="question",
                ),
                migrations.RemoveField(
                    model_name="stringanswer",
                    name="question",
                ),
                migrations.RemoveField(
                    model_name="stringanswer",
                    name="content_type",
                ),
                migrations.RemoveField(
                    model_name="question",
                    name="for_content_type",
                ),
                migrations.RemoveField(
                    model_name="question",
                    name="tournament",
                ),
                migrations.DeleteModel(
                    name="booleananswer",
                ),
                migrations.DeleteModel(
                    name="floatanswer",
                ),
                migrations.DeleteModel(
                    name="integeranswer",
                ),
                migrations.DeleteModel(
                    name="manyanswer",
                ),
                migrations.DeleteModel(
                    name="Question",
                ),
                migrations.DeleteModel(
                    name="stringanswer",
                ),
            ],
        ),
    ]
