# django-lazy-services
A helper for switching between test and production versions of a service

## Purpose

Lets you easily switch between versions of a service based on a Django setting entry.
Good for situations where you want to use different versions between production and development and/or test.
In the client code you might use: `from . import my_service` which might go to either `.services.MyService` or `.services.MyFakeService` depending on the content of your settings.

## Usage

Construct your service as a class whose init takes no arguments.

In `services.py`:
```python
class MyService:
    def __init__(self):
        pass
    def hello(self):
        print("hello world")
```

Declare the service.

In `__init__.py`:
```python
from lazy_services import LazyService
my_service = LazyService("MY_SERVICE")
```

Select the service.

In `settings.py`
```python
MY_SERVICE = "my_project.services.MyService"
```

Use the service.

```python
from . import my_serivce
my_service.hello()
```
