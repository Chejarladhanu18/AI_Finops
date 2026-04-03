from rest_framework import viewsets
from .models import *
from .serializers import *


# =========================
# READ-ONLY APIs
# =========================

class NavbarViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Navbar.objects.all()
    serializer_class = NavbarSerializer


class MenuItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class DropdownItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DropdownItem.objects.all()
    serializer_class = DropdownItemSerializer


class HeroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer


class InfrastructureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InfrastructureCard.objects.all()
    serializer_class = InfrastructureSerializer


class VisibilityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Visibility.objects.all()
    serializer_class = VisibilitySerializer


class VisibilityCardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VisibilityCard.objects.all()
    serializer_class = VisibilityCardSerializer


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class FooterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer


class FooterSectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FooterSection.objects.all()
    serializer_class = FooterSectionSerializer


class FooterItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FooterItem.objects.all()
    serializer_class = FooterItemSerializer


# =========================
# FULL CRUD APIs
# =========================

class DemoViewSet(viewsets.ModelViewSet):
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer


class DemoFormViewSet(viewsets.ModelViewSet):
    queryset = DemoForm.objects.all()
    serializer_class = DemoFormSerializer


# 🔥 ADD THIS (VERY IMPORTANT)
class DemoFormSubmissionViewSet(viewsets.ModelViewSet):
    queryset = DemoFormSubmission.objects.all()
    serializer_class = DemoFormSubmissionSerializer


class PortfolioDataViewSet(viewsets.ModelViewSet):
    queryset = PortfolioData.objects.all()
    serializer_class = PortfolioDataSerializer