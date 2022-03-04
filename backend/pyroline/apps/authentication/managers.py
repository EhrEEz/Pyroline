from django.contrib.auth.base_user import BaseUserManager


class AccountManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, first_name, last_name, username, email, role, password=None):
        if not username:
            return ValueError("Username is Required")

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            role=role,
        )
        user.set_password(password)
        user.is_superuser = False
        user.is_active = True
        if role == 3 or role == 4:
            print(role)
            user.is_staff = True
        else:
            user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username, first_name, last_name, email, role, password=None, **extrafields
    ):
        if not password:
            ValueError("Please enter a password")
        if role == 3:
            user = self.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                role=role,
                password=password,
                **extrafields
            )
            user.is_superuser = True
            user.is_staff = True
            user.save(using=self._db)
            return user
        else:
            return ValueError("Not Eligible for superuser")
