from django.conf import settings
from django.utils.functional import LazyObject
from django.utils.module_loading import import_string


class LazyService(LazyObject):
    def __init__(self, setting_name):
        self.__dict__["_setting_name"] = setting_name
        super().__init__()

    def _setup(self):
        service = getattr(settings, self._setting_name)
        if "service" in service:
            assert "services" in service, service
        self._wrapped = import_string(service)()
