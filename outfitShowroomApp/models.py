from django.db import models

# Create your models here.
class Prenda(models.Model):
    #Campo para la relación
    #models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    id_pr = models.AutoField(auto_created=True, primary_key=True)
    disenador = models.CharField(max_length=40)
    precio = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    
    TALLAS = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    talla = models.CharField(max_length=1, choices=TALLAS)
    origen = models.CharField(max_length=40)
    cuidados = models.CharField(max_length=40)
    materiales = models.CharField(max_length=40)

    def __str__(self):
        return "{} ".format(self.nombre, self.disenador, self.id_pr, self.precio, self.talla, self.origen, self.cuidados, self.materiales)

class Outfit(models.Model):
    id_out = models.AutoField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=40)
    desc = models.CharField(max_length=4000)
    precio = models.DecimalField(decimal_places=2, max_digits=5, default=0)

    def __str__(self):
        return self.nombre, self.desc, self.precio, self.id_out

class Ocasion(models.Model):
    nombre = models.CharField(max_length=40)
    desc = models.CharField(max_length=4000)
    id_oc = models.AutoField(auto_created=True, primary_key=True)

    def str(self):
        return self.nombre, self.desc, self.id_oc

class Estilo(models.Model):
    id_est = models.AutoField(auto_created=True, primary_key=True)
    desc = models.CharField(max_length=4000)
    nombre = models.CharField(max_length=40)

    def str(self):
        return self.nombre, self.desc, self.id_est