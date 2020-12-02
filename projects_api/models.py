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

class Material(models.Model):
    """Construction material model"""
    name_material = models.CharField(max_length=255)
    unit_id = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        """Return string representation of name_material"""
        return self.name_material

class VolumeUnit(models.Model):
    """Construction volume unit model"""
    name_volume_unit = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name volume unit"""
        return self.name_volume_unit

class EnergyUnit(models.Model):
    """Construction energy unit model"""
    name_energy_unit = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name volume unit"""
        return self.name_energy_unit

class BulkUnit(models.Model):
    """Construction bulk unit model"""
    name_bulk_unit = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name bulk unit"""
        return self.name_bulk_unit

class SourceInformation(models.Model):
    """Construction source information model"""
    name_source_information = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name source information"""
        return self.name_source_information

class ConstructiveProcess(models.Model):
    """Constructive process"""
    name_constructive_process = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name constructive process"""
        return self.name_constructive_process

class MaterialSchemeProject(models.Model):
    """MaterialSchemeProject model"""
    material_id = models.ForeignKey(Material, on_delete=models.DO_NOTHING, null=True)
    project_id = models.ForeignKey(Project, on_delete=models.DO_NOTHING, null=True)
    origin_id = models.ForeignKey(Origin, on_delete=models.DO_NOTHING, null=True)
    construction_system = models.CharField(max_length=255, null=True)
    quantity = models.IntegerField()
    section_id = models.ForeignKey(Section, on_delete=models.DO_NOTHING, null=True)
    value = models.DecimalField(max_digits=25, decimal_places=25, null=True)

    def __str__(self):
        """Return string representation of material"""
        return self.material_id

class MaterialSchemeData(models.Model):
    """MaterialSchemeData model"""
    material_id = models.ForeignKey(Material, on_delete=models.DO_NOTHING, null=True)
    standard_id = models.ForeignKey(Standard, on_delete=models.DO_NOTHING, null=True)
    potential_type_id = models.ForeignKey(PotentialType, on_delete=models.DO_NOTHING, null=True)
    unit_id = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, null=True)
    value = models.DecimalField(max_digits=25, decimal_places=25, null=True )

    def __str__(self):
        """Return string representation of material"""
        return self.value

class ConstructiveSystemElement(models.Model):
    """CSE model"""
    project_id = models.ForeignKey(Project, on_delete=models.DO_NOTHING, null=True)
    section_id = models.ForeignKey(Section, on_delete=models.DO_NOTHING, null=True)
    constructive_process_id = models.ForeignKey(ConstructiveProcess, on_delete=models.DO_NOTHING, null=True)
    quantity =  models.IntegerField()
    volume_unit_id = models.ForeignKey(VolumeUnit, on_delete=models.DO_NOTHING, null=True)
    energy_unit_id = models.ForeignKey(EnergyUnit, on_delete=models.DO_NOTHING, null=True)
    bulk_unit_id = models.ForeignKey(BulkUnit, on_delete=models.DO_NOTHING, null=True)
    source_information_id = models.ForeignKey(SourceInformation, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        """Return string representation of ma"""
        return self.project_id

class SourcesElectricityConsumption(models.Model):
    """Sources electricity consumption"""
    name_source_electricity_consumption = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name constructive process"""
        return self.name_source_electricity_consumption

class AnnualConsumptionRequired(models.Model):
    """ACR model"""
    project_id = models.ForeignKey(Project, on_delete=models.DO_NOTHING, null=True)
    quantity =  models.IntegerField()
    unit_id = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        """Return string representation of ACR"""
        return self.project_id

class TypeEnergy(models.Model):
    """Constructive type energy"""
    name_type_energy = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name type energy"""
        return self.name_type_energy

class ElectricityConsumptionData(models.Model):
    """ECD model"""
    annual_consumption_required_id = models.ForeignKey(AnnualConsumptionRequired, on_delete=models.DO_NOTHING, null=True)
    unit_id = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, null=True)
    quantity =  models.IntegerField(null=True)
    type = models.ForeignKey(TypeEnergy, on_delete=models.DO_NOTHING, null=True)
    percentage = models.IntegerField(null=True)

    def __str__(self):
        """Return string representation of ECD"""
        return self.annual_consumption_required_id

class StageSchemeData(models.Model):
    """SSD model"""
    name_stage = models.CharField(max_length=255, null=True)
    abbreviation = models.CharField(max_length=255, null=True)
    unit_stage_id = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, null=True)
    value = models.DecimalField(max_digits=25, decimal_places=25, null=True)
    stage = models.CharField(max_length=255, null=True)

    def __str__(self):
        """Return string representation of ECD"""
        return self.name_stage
