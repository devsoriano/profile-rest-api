from rest_framework import serializers

from projects_api import models

class UsesSerializer(serializers.ModelSerializer):
    """Serializes a section use"""

    class Meta:
        model = models.Use
        fields = '__all__'

    def create(self, validated_data):
        """Used to create use"""
        use = models.Use(
            name_use=validated_data['name_use']
        )

        use.save()
        return use

    def update(self, instance, validated_data):
        """Handle updating a use"""
        return super().update(instance, validated_data)

class TypeProjectsSerializer(serializers.ModelSerializer):
    """Serializes a type projects"""

    class Meta:
        model = models.TypeProject
        fields = '__all__'

    def create(self, validated_data):
        """Used to create type project"""
        type_project = models.TypeProject(
            name_type_project=validated_data['name_type_project']
        )

        type_project.save()
        return type_project

    def update(self, instance, validated_data):
        """Handle updating a type project"""
        return super().update(instance, validated_data)

class CountriesSerializer(serializers.ModelSerializer):
    """Serializes a countries"""

    class Meta:
        model = models.Country
        fields = '__all__'

    def create(self, validated_data):
        """Used to create type project"""
        country = models.Country(
            name_country=validated_data['name_country']
        )

        country.save()
        return country

    def update(self, instance, validated_data):
        """Handle updating a country"""
        return super().update(instance, validated_data)

class UsefulLifeSerializer(serializers.ModelSerializer):
    """Serializes a useful life"""

    class Meta:
        model = models.UsefulLife
        fields = '__all__'

    def create(self, validated_data):
        """Used to create type project"""
        useful_life = models.UsefulLife(
            name_useful_life=validated_data['name_useful_life']
        )

        useful_life.save()
        return useful_life

    def update(self, instance, validated_data):
        """Handle updating a country"""
        return super().update(instance, validated_data)

class HousingSchemeSerializer(serializers.ModelSerializer):
    """Serializes a housing scheme"""

    class Meta:
        model = models.HousingScheme
        fields = '__all__'

    def create(self, validated_data):
        """Used to create type project"""
        housing_scheme = models.HousingScheme(
            name_housing_scheme = validated_data['name_housing_scheme']
        )

        housing_scheme.save()
        return housing_scheme

    def update(self, instance, validated_data):
        """Handle updating a country"""
        return super().update(instance, validated_data)

class ProjetcsSerializer(serializers.ModelSerializer):
    """Serializes a project object"""

    class Meta:
        model = models.Project
        fields = '__all__'

    def create(self, validated_data):
        """Used to create a project."""
        project = models.Project(
            name_project=validated_data['name_project'],
            use_id=validated_data['use_id'],
            type_id=validated_data['type_id'],
            country_id=validated_data['country_id'],
            builded_surface=validated_data['builded_surface'],
            living_area=validated_data['living_area'],
            tier=validated_data['tier'],
            useful_life_id=validated_data['useful_life_id']
        )

        project.save()
        return project

    def update(self, instance, validated_data):
        """Handle updating a project"""
        return super().update(instance, validated_data)

class SectionsSerializer(serializers.ModelSerializer):
    """Serializes a section section"""

    class Meta:
        model = models.Section
        fields = '__all__'

    def create(self, validated_data):
        """Used to create section"""
        section = models.Section(
            name_section=validated_data['name_section']
        )

        section.save()
        return section

    def update(self, instance, validated_data):
        """Handle updating a section"""
        return super().update(instance, validated_data)

class OriginsSerializer(serializers.ModelSerializer):
    """Serializes a origin object"""

    class Meta:
        model = models.Origin
        fields = '__all__'

    def create(self, validated_data):
        """Used to create origin"""
        origin = models.Origin(
            name_origin=validated_data['name_origin']
        )

        origin.save()
        return origin

    def update(self, instance, validated_data):
        """Handle updating a section"""
        return super().update(instance, validated_data)

class UnitsSerializer(serializers.ModelSerializer):
    """Serializes a create unit"""

    class Meta:
        model = models.Unit
        fields = '__all__'

    def create(self, validated_data):
        """Used to create origin"""
        unit = models.Unit(
            name_unit=validated_data['name_unit']
        )

        unit.save()
        return unit

    def update(self, instance, validated_data):
        """Handle updating a section"""
        return super().update(instance, validated_data)

class StandardsSerializer(serializers.ModelSerializer):
    """Serializes a create standards"""

    class Meta:
        model = models.Standard
        fields = '__all__'

    def create(self, validated_data):
        """Used to create standard"""
        standard = models.Standard(
            name_standard=validated_data['name_standard']
        )

        standard.save()
        return standard

    def update(self, instance, validated_data):
        """Handle updating a section"""
        return super().update(instance, validated_data)

class PotentialTypesSerializer(serializers.ModelSerializer):
    """Serializes a potential types"""

    class Meta:
        model = models.PotentialType
        fields = '__all__'

    def create(self, validated_data):
        """Used to create potential type"""
        potentialType = models.PotentialType(
            name_potential_type=validated_data['name_potential_type']
        )

        potentialType.save()
        return potentialType

    def update(self, instance, validated_data):
        """Handle updating a section"""
        return super().update(instance, validated_data)

class MaterialsSerializer(serializers.ModelSerializer):
    """Serializes a section material"""

    class Meta:
        model = models.Material
        fields = '__all__'

    def create(self, validated_data):
        """Used to create material"""
        material = models.Material(
            name_material=validated_data['name_material'],
            unit_id=validated_data['unit_id']
        )

        material.save()
        return material

    def update(self, instance, validated_data):
        """Handle updating a section"""
        return super().update(instance, validated_data)

class VolumeUnitsSerializer(serializers.ModelSerializer):
    """Serializes a create volume unit"""

    class Meta:
        model = models.VolumeUnit
        fields = '__all__'

    def create(self, validated_data):
        """Used to create origin"""
        unit = models.VolumeUnit(
            name_volume_unit=validated_data['name_volume_unit']
        )

        unit.save()
        return unit

    def update(self, instance, validated_data):
        """Handle updating a section"""
        return super().update(instance, validated_data)

class EnergyUnitsSerializer(serializers.ModelSerializer):
    """Serializes a create energy unit"""

    class Meta:
        model = models.EnergyUnit
        fields = '__all__'

    def create(self, validated_data):
        """Used to create origin"""
        unit = models.EnergyUnit(
            name_energy_unit=validated_data['name_energy_unit']
        )

        unit.save()
        return unit

    def update(self, instance, validated_data):
        """Handle updating a section"""
        return super().update(instance, validated_data)

class BulkUnitsSerializer(serializers.ModelSerializer):
    """Serializes a create bulk unit"""

    class Meta:
        model = models.BulkUnit
        fields = '__all__'

    def create(self, validated_data):
        """Used to create origin"""
        unit = models.BulkUnit(
            name_bulk_unit=validated_data['name_bulk_unit']
        )

        unit.save()
        return unit

    def update(self, instance, validated_data):
        """Handle updating a section"""
        return super().update(instance, validated_data)

class SourceInformationSerializer(serializers.ModelSerializer):
    """Serializes a create source information"""

    class Meta:
        model = models.SourceInformation
        fields = '__all__'

    def create(self, validated_data):
        """Used to create origin"""
        source = models.SourceInformation(
            name_source_information = validated_data['name_source_information']
        )

        source.save()
        return source

    def update(self, instance, validated_data):
        """Handle updating a section"""
        return super().update(instance, validated_data)

class ConstructiveProcessSerializer(serializers.ModelSerializer):
    """Serializes a create constructive process"""

    class Meta:
        model = models.ConstructiveProcess
        fields = '__all__'

    def create(self, validated_data):
        """Used to create origin"""
        constructiveProcess = models.ConstructiveProcess(
            name_constructive_process = validated_data['name_constructive_process']
        )

        constructiveProcess.save()
        return constructiveProcess

    def update(self, instance, validated_data):
        """Handle updating a section"""
        return super().update(instance, validated_data)

class MaterialSchemeProjectSerializer(serializers.ModelSerializer):
    """Material Scheme a material object"""

    class Meta:
        model = models.MaterialSchemeProject
        fields = '__all__'

    def create(self, validated_data):
        """Used to create a material."""
        material_scheme = models.MaterialSchemeProject(
            material_id=validated_data['material_id'],
            project_id=validated_data['project_id'],
            origin_id=validated_data['origin_id'],
            construction_system=validated_data['construction_system'],
            quantity=validated_data['quantity'],
            section_id=validated_data['section_id'],
            provider_distance=validated_data['provider_distance']
        )

        material_scheme.save()
        return material_scheme

    def update(self, instance, validated_data):
        """Handle updating a material"""
        return super().update(instance, validated_data)

class MaterialSchemeDataSerializer(serializers.ModelSerializer):
    """Material Scheme a material scheme data object"""

    class Meta:
        model = models.MaterialSchemeData
        fields = '__all__'

    def create(self, validated_data):
        """Used to create a material scheme data"""
        material_scheme_data = models.MaterialSchemeData(
            material_id=validated_data['material_id'],
            standard_id=validated_data['standard_id'],
            potential_type_id=validated_data['potential_type_id'],
            unit_id=validated_data['unit_id'],
            value=validated_data['value']
        )

        material_scheme_data.save()
        return material_scheme_data

    def update(self, instance, validated_data):
        """Handle updating a material"""
        return super().update(instance, validated_data)

class ConstructiveSystemElementSerializer(serializers.ModelSerializer):
    """Serializer CSY"""

    class Meta:
        model = models.ConstructiveSystemElement
        fields = '__all__'

    def create(self, validated_data):
        """Used to create a CSE"""
        constructive_system_element = models.ConstructiveSystemElement(
            project_id=validated_data['project_id'],
            section_id=validated_data['section_id'],
            constructive_process_id=validated_data['constructive_process_id'],
            quantity=validated_data['quantity'],
            volume_unit_id=validated_data['volume_unit_id'],
            energy_unit_id=validated_data['energy_unit_id'],
            bulk_unit_id=validated_data['bulk_unit_id'],
            source_information_id=validated_data['source_information_id']
        )

        constructive_system_element.save()
        return constructive_system_element

    def update(self, instance, validated_data):
        """Handle updating a material"""
        return super().update(instance, validated_data)

class SourcesElectricityConsumptionSerializer(serializers.ModelSerializer):
    """Serializes a create SEC"""

    class Meta:
        model = models.SourcesElectricityConsumption
        fields = '__all__'

    def create(self, validated_data):
        """Used to create origin"""
        sec = models.SourcesElectricityConsumption(
            name_source_electricity_consumption = validated_data['name_source_electricity_consumption']
        )

        sec.save()
        return sec

    def update(self, instance, validated_data):
        """Handle updating a section"""
        return super().update(instance, validated_data)

class AnnualConsumptionRequiredSerializer(serializers.ModelSerializer):
    """Serializer ACR"""

    class Meta:
        model = models.AnnualConsumptionRequired
        fields = '__all__'

    def create(self, validated_data):
        """Used to create a ACR"""
        ACR = models.AnnualConsumptionRequired(
            project_id=validated_data['project_id'],
            quantity=validated_data['quantity'],
            unit_id=validated_data['unit_id']
        )

        ACR.save()
        return ACR

    def update(self, instance, validated_data):
        """Handle updating a ACR"""
        return super().update(instance, validated_data)

class ElectricityConsumptionDataSerializer(serializers.ModelSerializer):
    """Serializer ECD"""

    class Meta:
        model = models.ElectricityConsumptionData
        fields = '__all__'

    def create(self, validated_data):
        """Used to create a ACR"""
        ECD = models.ElectricityConsumptionData(
            annual_consumption_required_id=validated_data['annual_consumption_required_id'],
            unit_id=validated_data['unit_id'],
            quantity=validated_data['quantity'],
            type=validated_data['type'],
            percentage=validated_data['percentage']
        )

        ECD.save()
        return ECD

    def update(self, instance, validated_data):
        """Handle updating a ECD"""
        return super().update(instance, validated_data)

class StageSchemeDataSerializer(serializers.ModelSerializer):
    """Serializer SSD"""

    class Meta:
        model = models.StageSchemeData
        fields = '__all__'

    def create(self, validated_data):
        """Used to create a SSD"""
        SSD = models.StageSchemeData(
            name_stage=validated_data['name_stage'],
            abbreviation=validated_data['abbreviation'],
            unit_stage_id=validated_data['unit_stage_id'],
            value=validated_data['value'],
            stage=validated_data['stage'],
        )

        SSD.save()
        return SSD

    def update(self, instance, validated_data):
        """Handle updating a SSD"""
        return super().update(instance, validated_data)

class TypeEnergySerializer(serializers.ModelSerializer):
    """Serializes a type energy"""

    class Meta:
        model = models.TypeEnergy
        fields = '__all__'

    def create(self, validated_data):
        """Used to create origin"""
        TypeEnergy = models.TypeEnergy(
            name_type_energy = validated_data['name_type_energy']
        )

        TypeEnergy.save()
        return TypeEnergy

    def update(self, instance, validated_data):
        """Handle updating a section"""
        return super().update(instance, validated_data)

class ElectricityConsumptionDeconstructiveProcessSerializer(serializers.ModelSerializer):
    """Serializer ECDP"""

    class Meta:
        model = models.ElectricityConsumptionDeconstructiveProcess
        fields = '__all__'

    def create(self, validated_data):
        """Used to create a ECDP"""
        SSD = models.ElectricityConsumptionDeconstructiveProcess(
            unit_id=validated_data['unit_id'],
            source_information_id=validated_data['source_information_id'],
            quantity=validated_data['quantity'],
            section_id=validated_data['section_id'],
            stage=validated_data['project_id'],
        )

        SSD.save()
        return SSD

    def update(self, instance, validated_data):
        """Handle updating a ECDP"""
        return super().update(instance, validated_data)

class TreatmentOfGeneratedWasteSerializer(serializers.ModelSerializer):
    """Serializer TOGW"""

    class Meta:
        model = models.TreatmentOfGeneratedWaste
        fields = '__all__'

    def create(self, validated_data):
        """Used to create a TOGW"""
        SSD = models.TreatmentOfGeneratedWaste(
            landfill=validated_data['landfill'],
            recycling=validated_data['recycling'],
            reuse=validated_data['reuse'],
            section_id=validated_data['section_id'],
            stage=validated_data['project_id'],
        )

        SSD.save()
        return SSD

    def update(self, instance, validated_data):
        """Handle updating a ECDP"""
        return super().update(instance, validated_data)


class SourceInformationDataSerializer(serializers.ModelSerializer):
    """Material Scheme a material scheme data object"""

    class Meta:
        model = models.SourceInformationData
        fields = '__all__'

    def create(self, validated_data):
        """Used to create a material scheme data"""
        source_information_data = models.SourceInformationData(
            sourceInformarion_id=validated_data['sourceInformarion_id'],
            potential_type_id=validated_data['potential_type_id'],
            unit_id=validated_data['unit_id'],
            value=validated_data['value']
        )

        source_information_data.save()
        return source_information_data

    def update(self, instance, validated_data):
        """Handle updating a material"""
        return super().update(instance, validated_data)

class TypeEnergyDataSerializer(serializers.ModelSerializer):
    """Material Scheme a material scheme data object"""

    class Meta:
        model = models.TypeEnergyData
        fields = '__all__'

    def create(self, validated_data):
        """Used to create a material scheme data"""
        type_energy_data = models.TypeEnergyData(
            type_energy_id=validated_data['type_energy_id'],
            potential_type_id=validated_data['potential_type_id'],
            unit_id=validated_data['unit_id'],
            value=validated_data['value']
        )

        type_energy_data.save()
        return type_energy_data

    def update(self, instance, validated_data):
        """Handle updating a material"""
        return super().update(instance, validated_data)