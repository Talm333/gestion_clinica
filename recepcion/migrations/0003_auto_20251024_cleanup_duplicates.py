from django.db import migrations, models

def cleanup_duplicate_clientes(apps, schema_editor):
    Equipo = apps.get_model('recepcion', 'Equipo')
    # Get all equipos
    equipos = Equipo.objects.all()
    # Keep track of client names we've seen
    seen_names = {}
    # Identify duplicates
    for equipo in equipos:
        if equipo.cliente in seen_names:
            # If this client name was seen before, update this duplicate with a unique name
            equipo.cliente = f"{equipo.cliente}_{equipo.id}"
            equipo.save()
        else:
            seen_names[equipo.cliente] = True

class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0002_rename_nombre_equipo_cliente_equipo_fecha_and_more'),
    ]

    operations = [
        migrations.RunPython(cleanup_duplicate_clientes),
        migrations.AlterModelOptions(
            name='equipo',
            options={'verbose_name': 'Equipo', 'verbose_name_plural': 'Equipos'},
        ),
        migrations.AlterField(
            model_name='equipo',
            name='cliente',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nombre del cliente'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='problema',
            field=models.TextField(verbose_name='Descripción del problema'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='tipo',
            field=models.CharField(max_length=50, verbose_name='Tipo de equipo'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de recepción'),
        ),
    ]