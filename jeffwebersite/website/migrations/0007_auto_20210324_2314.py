# Generated by Django 3.1.7 on 2021-03-24 20:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20210324_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blocksswivels',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='bopaccumulatorswellcontrol',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='casingtubingrunning',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='cementing',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='coiltubing',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='compressor',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='drillingrig',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='drillstring',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='enginesgensetsscr',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='fishingtool',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='flowback',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='frac',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='handlingtool',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='manifold',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='miscellaneou',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='mudpumpsconditioning',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='nitrogen',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='octg',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='offshore',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='pumps',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='slickline',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='snubbing',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='subsea',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='thrutubing',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='topdrive',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='wellserviceworkover',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='welltest',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
        migrations.AlterField(
            model_name='wireline',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0653622c-407d-481d-af3b-73d61bb08321'), editable=False),
        ),
    ]
