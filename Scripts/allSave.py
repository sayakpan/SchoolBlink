import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SchoolData.settings")
django.setup()

from django.utils.text import slugify
from Profiles.models import School_Profiles


def apply_slug_to_existing_objects():
    profiles = School_Profiles.objects.all()
    for profile in profiles:
        if not profile.slug:
            base_slug = slugify(profile.school_name)
            slug = base_slug
            unique_id = profile.id
            while School_Profiles.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{unique_id}"
            profile.slug = slug
            profile.save()


# Usage
apply_slug_to_existing_objects()
