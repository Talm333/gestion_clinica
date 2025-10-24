from django.db import migrations, models

def remove_duplicate_roles(apps, schema_editor):
    Rol = apps.get_model('login', 'rol')
    # Get all roles
    roles = Rol.objects.all()
    # Keep track of role names we've seen
    seen_names = {}
    # Identify duplicates
    for role in roles:
        if role.nombre in seen_names:
            # If this name was seen before, update this duplicate with a unique name
            role.nombre = f"{role.nombre}_{role.id}"
            role.save()
        else:
            seen_names[role.nombre] = True

class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(remove_duplicate_roles),
        migrations.AlterField(
            model_name='rol',
            name='nombre',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nombre del rol'),
        ),
        migrations.AlterField(
            model_name='rol',
            name='descripcion',
            field=models.CharField(max_length=100, verbose_name='Descripción'),
        ),
    ]