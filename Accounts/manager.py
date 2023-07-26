from django.contrib.auth.base_user import BaseUserManager


# Custom User Manager
class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            uniqueuser = self.generate_unique_username(email)
        uniqueuser = username
        user = self.model(username=uniqueuser, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(username, email, password, **extra_fields)

    def generate_unique_username(self, email):
        username = email.split("@")[0]  # Example: Use email prefix as the username
        base_username = username
        suffix_num = 1
        while self.model.objects.filter(username=username).exists():
            username = f"{base_username}{suffix_num}"
            suffix_num += 1
        return username
