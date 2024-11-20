from django.apps import AppConfig


class PeopleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'people'
    label = 'people'
    migrations_module = 'people.Infrastructure.migrations'

    def ready(self):
        import people.admin
