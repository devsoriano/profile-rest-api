"""Projects Django"""
from django.db import models
from django.contrib.auth.models import User

class Use(models.Model):
    """Construction use model"""
    name_use = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name_material"""
        return self.name_use

class TypeProject(models.Model):
    """Construction type project model"""
    name_type_project = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of type project model"""
        return self.name_type_project

class Country(models.Model):
    """Construction type country model"""
    name_country = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of country model"""
        return self.name_country

class UsefulLife(models.Model):
    """Construction useful life model"""
    name_useful_life = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of useful life model"""
        return self.name_useful_life

class HousingScheme(models.Model):
    """Construction housing scheme model"""
    name_housing_scheme = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of housing scheme model"""
        return self.name_housing_scheme

class Project(models.Model):
    """Project model"""
    name_project = models.CharField(max_length=255)
    use_id = models.ForeignKey(Use, on_delete=models.DO_NOTHING, null=True)
    type_id = models.ForeignKey(TypeProject, on_delete=models.DO_NOTHING, null=True)
    country_id = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True)
    useful_life_id = models.ForeignKey(UsefulLife, on_delete=models.DO_NOTHING, null=True)
    housing_scheme_id = models.ForeignKey(HousingScheme, on_delete=models.DO_NOTHING, null=True)
    builded_surface = models.IntegerField()
    living_area = models.IntegerField()
    tier = models.IntegerField()

    def __str__(self):
        """Return string representation of project"""
        return self.name_project

class Material(models.Model):
    """Construction material model"""
    name_material = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name_material"""
        return self.name_material

class Section(models.Model):
    """Section model"""
    name_section = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name_section"""
        return self.name_section

class Origin(models.Model):
    """Origin model"""
    name_origin = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name_origin"""
        return self.name_origin

class ConstructionSystem(models.Model):
    """Construction system model"""
    name_construction_system = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name_construction_system"""
        return self.name_construction_system

class Unit(models.Model):
    """Construction unit model"""
    name_unit = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name unit"""
        return self.name_unit

class Standard(models.Model):
    """Construction standard model"""
    name_standard = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name standard"""
        return self.name_standard

class PotentialType(models.Model):
    """Construction potential type model"""
    name_potential_type = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name potential type"""
        return self.name_potential_type

class MaterialSchemeProject(models.Model):
    """MaterialSchemeProject model"""
    material_id = models.ForeignKey(Material, on_delete=models.DO_NOTHING, null=True)
    project_id = models.ForeignKey(Project, on_delete=models.DO_NOTHING, null=True)
    origin_id = models.ForeignKey(Origin, on_delete=models.DO_NOTHING, null=True)
    construction_system_id = models.ForeignKey(ConstructionSystem, on_delete=models.DO_NOTHING, null=True)
    quantity = models.IntegerField()
    unit_id = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, null=True)
    section_id = models.ForeignKey(Section, on_delete=models.DO_NOTHING, null=True)
    provider_distance = models.DecimalField(max_digits = 15, decimal_places = 10)

    def __str__(self):
        """Return string representation of material"""
        return self.material_id

class MaterialSchemeData(models.Model):
    """MaterialSchemeData model"""
    material_id = models.ForeignKey(Material, on_delete=models.DO_NOTHING, null=True)
    standard_id = models.ForeignKey(Standard, on_delete=models.DO_NOTHING, null=True)
    potential_type_id = models.ForeignKey(PotentialType, on_delete=models.DO_NOTHING, null=True)
    unit_id = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, null=True)
    value = models.DecimalField(max_digits = 15, decimal_places = 10)

    def __str__(self):
        """Return string representation of material"""
        return self.value
