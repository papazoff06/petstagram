from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'petstagram_two.accounts'

    def ready(self):
        import petstagram_two.accounts.signals

