from django.db import migrations, models

def cleanup_duplicate_estudiantes(apps, schema_editor):
    Estudiante = apps.get_model('diagnostico', 'Estudiante')
    # Get all students
    estudiantes = Estudiante.objects.all()
    # Keep track of student names we've seen
    seen_names = {}
    # Identify duplicates
    for estudiante in estudiantes:
        if estudiante.nombre in seen_names:
            # If this name was seen before, update this duplicate with a unique name
            estudiante.nombre = f"{estudiante.nombre}_{estudiante.id}"
            estudiante.save()
        else:
            seen_names[estudiante.nombre] = True

class Migration(migrations.Migration):

    dependencies = [
        ('diagnostico', '0004_alter_diagnostico_tipo_solucion'),
    ]

    operations = [
        migrations.RunPython(cleanup_duplicate_estudiantes),
        migrations.AlterField(
            model_name='estudiante',
            name='nombre',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nombre del estudiante'),
        ),
        migrations.AlterModelOptions(
            name='estudiante',
            options={'verbose_name': 'Estudiante', 'verbose_name_plural': 'Estudiantes'},
        ),
    ]