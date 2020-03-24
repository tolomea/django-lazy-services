import lazy_services
from django.conf import settings

settings.configure(SERVICE="tests.services.Service")


service = lazy_services.LazyService("SERVICE")


def test_attribute():
    service.val = 6
    assert service.val == 6


def test_function():
    service.set_val(6)
    assert service.get_val() == 6


def test_change_setting_no_effect(settings):
    assert service.base == 7
    settings.SERVICE = "tests.service.Service2"
    assert service.base == 7
