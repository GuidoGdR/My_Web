from django.db import models

# Create your models here.

class My_tool(models.Model):
    
    name = models.CharField(max_length=50)
    
    logo = models.ImageField( upload_to="img/language/", height_field=None, width_field=None, max_length=None )
    
    class Meta:
        verbose_name_plural = "Mis herramientas"
    
    def __str__(self) -> str:
        return f"name={self.name}, logo={self.logo}"


class Woroked_for_enterprice(models.Model):
    
    name = models.CharField(max_length=50)
    
    logo = models.ImageField( upload_to="img/enterprice/", height_field=None, width_field=None, max_length=None )
    
    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        
        db_table = "Worked_for"
        
    def __str__(self) -> str:
        return f"name={self.name}, logo={self.logo}"
    
    