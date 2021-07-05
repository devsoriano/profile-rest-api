from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from projects_api import models
from projects_api import serializers
from profiles_api import permissions

class UserPlatformViewSet(viewsets.ModelViewSet):
    """Handle creating and updating user"""
    serializer_class = serializers.UserPlatformSerializer
    queryset = models.UserPlatform.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('email', )

class TransportsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating transports"""
    serializer_class = serializers.TransportsSerializer
    queryset = models.Transport.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', )

class UsesViewSet(viewsets.ModelViewSet):
    """Handle creating and updating uses"""
    serializer_class = serializers.UsesSerializer
    queryset = models.Use.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_use', )

class TypeProjectsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating type projects"""
    serializer_class = serializers.TypeProjectsSerializer
    queryset = models.TypeProject.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_type_project', )

class CountriesViewSet(viewsets.ModelViewSet):
    """Handle creating and updating countries"""
    serializer_class = serializers.CountriesSerializer
    queryset = models.Country.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_country', )

class ExternalDistanceViewSet(viewsets.ModelViewSet):
    """Handle creating and updating countries"""
    serializer_class = serializers.ExternalDistanceSerializer
    queryset = models.ExternalDistance.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', )

class UsefulLifeViewSet(viewsets.ModelViewSet):
    """Handle creating and updating useful life"""
    serializer_class = serializers.UsefulLifeSerializer
    queryset = models.UsefulLife.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_useful_life', )

class HousingSchemeViewSet(viewsets.ModelViewSet):
    """Handle creating and updating housing Scheme"""
    serializer_class = serializers.HousingSchemeSerializer
    queryset = models.HousingScheme.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_housing_scheme', )

class ProjectsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.ProjectsSerializer
    queryset = models.Project.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=id',)

class MaterialsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating materials"""
    serializer_class = serializers.MaterialsSerializer
    queryset = models.Material.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ['=id', 'name_material']

class SectionsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating sections"""
    serializer_class = serializers.SectionsSerializer
    queryset = models.Section.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_section', )

class OriginsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating origins"""
    serializer_class = serializers.OriginsSerializer
    queryset = models.Origin.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_origin', )

class UnitsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating units"""
    serializer_class = serializers.UnitsSerializer
    queryset = models.Unit.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_unit', )

class StandardsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating standards"""
    serializer_class = serializers.StandardsSerializer
    queryset = models.Standard.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_standard', )

class PotentialTypesViewSet(viewsets.ModelViewSet):
    """Handle creating and updating potential types"""
    serializer_class = serializers.PotentialTypesSerializer
    queryset = models.PotentialType.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_potential_type', )

class VolumeUnitsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating volume units"""
    serializer_class = serializers.VolumeUnitsSerializer
    queryset = models.VolumeUnit.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_volume_unit', )

class EnergyUnitsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating energy units"""
    serializer_class = serializers.EnergyUnitsSerializer
    queryset = models.EnergyUnit.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_energy_unit', )

class BulkUnitsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating bulk units"""
    serializer_class = serializers.BulkUnitsSerializer
    queryset = models.BulkUnit.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_bulk_unit', )

class SourceInformationViewSet(viewsets.ModelViewSet):
    """Handle creating and updating source information"""
    serializer_class = serializers.SourceInformationSerializer
    queryset = models.SourceInformation.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_source_information', )

class ConstructiveProcessViewSet(viewsets.ModelViewSet):
    """Handle creating and updating source information"""
    serializer_class = serializers.ConstructiveProcessSerializer
    queryset = models.ConstructiveProcess.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_constructive_process', )

class MaterialSchemeProjectViewSet(viewsets.ModelViewSet):
    """Handle creating and updating material scheme project"""
    serializer_class = serializers.MaterialSchemeProjectSerializer
    queryset = models.MaterialSchemeProject.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('material_id', )

class MaterialSchemeProjectOriginalViewSet(viewsets.ModelViewSet):
    """Handle creating and updating material scheme project"""
    serializer_class = serializers.MaterialSchemeProjectOriginalSerializer
    queryset = models.MaterialSchemeProjectOrigianal.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('material_id', )

class MaterialSchemeDataViewSet(viewsets.ModelViewSet):
    """Handle creating and updating material scheme data"""
    serializer_class = serializers.MaterialSchemeDataSerializer
    queryset = models.MaterialSchemeData.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('value', )

class ConstructiveSystemElementViewSet(viewsets.ModelViewSet):
    """Handle creating and updating CSE"""
    serializer_class = serializers.ConstructiveSystemElementSerializer
    queryset = models.ConstructiveSystemElement.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('project_id', )

class SourcesElectricityConsumptionViewSet(viewsets.ModelViewSet):
    """Handle creating and updating create source electricity consumption"""
    serializer_class = serializers.SourcesElectricityConsumptionSerializer
    queryset = models.SourcesElectricityConsumption.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_source_electricity_consumption', )

class AnnualConsumptionRequiredViewSet(viewsets.ModelViewSet):
    """Handle creating and updating create ACR"""
    serializer_class = serializers.AnnualConsumptionRequiredSerializer
    queryset = models.AnnualConsumptionRequired.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('project_id', )

class ElectricityConsumptionDataViewSet(viewsets.ModelViewSet):
    """Handle creating and updating create ECD"""
    serializer_class = serializers.ElectricityConsumptionDataSerializer
    queryset = models.ElectricityConsumptionData.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('annual_consumption_required_id', )

class StageSchemeDataViewSet(viewsets.ModelViewSet):
    """Handle creating and updating create SSD"""
    serializer_class = serializers.StageSchemeDataSerializer
    queryset = models.StageSchemeData.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=id', )

class TypeEnergyViewSet(viewsets.ModelViewSet):
    """Handle creating and updating create TypeEnergy"""
    serializer_class = serializers.TypeEnergySerializer
    queryset = models.TypeEnergy.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=id', )

class ElectricityConsumptionDeconstructiveProcessViewSet(viewsets.ModelViewSet):
    """Handle creating and updating create ECDP"""
    serializer_class = serializers.ElectricityConsumptionDeconstructiveProcessSerializer
    queryset = models.ElectricityConsumptionDeconstructiveProcess.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=id', )

class TreatmentOfGeneratedWasteViewSet(viewsets.ModelViewSet):
    """Handle creating and updating create TOGW"""
    serializer_class = serializers.TreatmentOfGeneratedWasteSerializer
    queryset = models.TreatmentOfGeneratedWaste.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=id', )

class SourceInformationDataViewSet(viewsets.ModelViewSet):
    """Handle creating and updating Source information data"""
    serializer_class = serializers.SourceInformationDataSerializer
    queryset = models.SourceInformationData.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('value', )

class TypeEnergyDataViewSet(viewsets.ModelViewSet):
    """Handle creating and updating Type Energy Data"""
    serializer_class = serializers.TypeEnergyDataSerializer
    queryset = models.TypeEnergyData.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('value', )

class StatesViewSet(viewsets.ModelViewSet):
    """Handle creating and updating states"""
    serializer_class = serializers.StatesSerializer
    queryset = models.State.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', )

class CitiesViewSet(viewsets.ModelViewSet):
    """Handle creating and updating cities"""
    serializer_class = serializers.CitiesSerializer
    queryset = models.City.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', )

class LocalDistancesViewSet(viewsets.ModelViewSet):
    """Handle creating and updating local distances"""
    serializer_class = serializers.LocalDistancesSerializer
    queryset = models.LocalDistance.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', )


class AirportsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating airports"""
    serializer_class = serializers.AirportsSerializer
    queryset = models.Airports.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=id',)


class FlightInfoViewSet(viewsets.ModelViewSet):
    """Handle creating and updating flight costs"""
    serializer_class = serializers.FlightInfoSerializer
    queryset = models.FlightInfo.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=departureAirportId')
