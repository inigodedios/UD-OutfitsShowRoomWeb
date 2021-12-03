from django.db import models
from datetime import datetime

# Create your models here.

class Prenda(models.Model):
    #Campo para la relación
    #models.ForeignKey(Empresa, on_delete=models.CASCADE)
    
    TALLAS = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('U', 'Unique Size'),
    )

    TIPOS_PRENDA = (
        (' ', ' '), #La base de datos necesita rellenar las filas con algo
        ('Abrigo', 'Abrigo'),
        ('Accesorio', 'Accesorio'),
        ('Blazer', 'Blazer'),
        ('Body', 'Body'),
        ('Botines', 'Botines'),
        ('Camisa', 'Camisa'),
        ('Camiseta', 'Camiseta'),
        ('Cazadora', 'Cazadora'),
        ('Chaqueta', 'Chaqueta'),
        ('Jeans', 'Jeans'),
        ('Pantalón', 'Pantalón'),
        ('Plumífero', 'Plumífero'),
        ('Sudadera', 'Sudadera'),
        ('Top', 'Top'),
        ('Vestido', 'Vestido'),
        ('Zapatos', 'Zapatos'),
    )

    id_pr = models.AutoField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=4000)
    disenador = models.CharField(max_length=4000)
    talla = models.CharField(max_length=1, choices=TALLAS)
    precio = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    tipo_prenda = models.CharField(max_length=100, choices=TIPOS_PRENDA, default=" ") #TODO ¿Por qué es encesario poner un default en tipo y no en talla?
    origen = models.CharField(max_length=4000)
    materiales = models.CharField(max_length=4000)
    cuidados = models.CharField(max_length=4000)
    
    def __str__(self):
        return "{}".format(self.id_pr, self.nombre, self.disenador, self.talla, self.precio, self.tipo_prenda, self.origen, self.materiales, self.cuidados)

class Ocasion(models.Model):
    id_oc = models.AutoField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=4000)
    desc = models.CharField(max_length=4000)
    
    def __str__(self):
        return "{} {}".format(self.id_oc, self.nombre, ) #TODO por qué dos {}?

class Estilo(models.Model):
    id_est = models.AutoField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=4000)
    desc = models.CharField(max_length=4000)
    
    def __str__(self):
        return "{} ".format(self.id_est, self.nombre, )

class Outfit(models.Model):
    id_out = models.AutoField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=4000)
    desc = models.CharField(max_length=4000)
    precio = models.DecimalField(decimal_places=2, max_digits=5, default=0)

    #RELACIONES BASES DE DATOS
    estilo = models.ForeignKey(Estilo, null=False, blank=False, on_delete=models.CASCADE, related_name='outfits') #related_name indica el nombre de la relación (outfits de un determinado estilo - estilo.outfits.all(), estilo.outfits.count(), estilo.outfits.filter(precio>50).all())
    prendas = models.ManyToManyField(Prenda)
    ocasiones = models.ManyToManyField(Ocasion)

    def __str__(self):
        return "{} ".format(self.id_out, self.nombre, self.precio, )

class OutfitShowroom(models.Model):
    id_out = models.AutoField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=4000)
    eslogan = models.CharField(max_length=4000)
    
    def __str__(self):
        return "{} ".format(self.id_out, self.nombre, self.eslogan,)