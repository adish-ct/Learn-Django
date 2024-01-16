"""
Exception:

Exceptions are used to indicate errors in the program. It helps to handle these exceptions that are
occurred during the execution of the program.

"""

from django.db import models

class Model(models.Model):
    id = models.AutoField(primary_key=True)

# 1. Object.DoesNotExist Exception
    
    # Handle the case where Raised when a query for a single object returns no results.

try:
    my_model_instance = Model.objects.get(id=1)
except Model.DoesNotExist:
    # Handle the case where the object does not exist
    pass


# 2. Object.MultipleObjectsReturned Exception

    # Handle the case where Raised when a query for a single object returns multiple results.

try:
    my_model_instance = Model.objects.get(id=1)
except Model.MultipleObjectsReturned:
    # Handle the case where multiple objects are returned
    pass


# 3. Object.ValidationErrors Exception

    # Raised when form or model validation fails.

from django.core.exceptions import ValidationError

try:
    # Some validation logic
    raise ValidationError("Validation failed!")
except ValidationError as e:
    # Handle the validation error
    print(e)

# 4. django.http.Http404
    
    # Raised when the requested resource is not found. Raised to indicate that the requested resource could not be found (404 Not Found).
    

from django.http import Http404

def my_view(request):
    try:
        # Some logic
        raise Http404("Requested resource not found.")
    except Http404:
        # Handle the 404 error
        pass


# 5. django.core.exceptions.PermissionDenied
    
    # Raised when a user attempts an action for which they do not have permission.

from django.core.exceptions import PermissionDenied

def my_view(request):
    if not user_has_permission(request.user):
        raise PermissionDenied("You do not have permission to perform this action.")


# 6 django.db.utils.IntegrityError
    
    # Raised when a database integrity constraint is violated.

from django.db import IntegrityError

try:
    # Some database operation
    pass
except IntegrityError:
    # Handle the integrity error
    pass


# custom exceptions

class MyCustomError(Exception):
    pass

try:
    # Some logic
    raise MyCustomError("An error occurred.")
except MyCustomError:
    # Handle your custom error
    pass

