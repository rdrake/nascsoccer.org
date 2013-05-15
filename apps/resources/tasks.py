from celery import task

from .models import Location
from .utils import get_field_status

@task(default_retry_delay=10 * 60, max_retries=1, ignore_result=True)
def update_field_status():
    try:
        field_status = get_field_status()
    except Exception as exc:
        raise update_field_status.retry(exc=exc)

    for (field, status) in field_status.items():
        print(field)

        try:
            location = Location.objects.get(name=field)
            
            print(location.name)

            location.status = status
            location.save()
        except Exception:
            # If we get an exception chances are the field isn't used by
            # any of our teams.
            pass
