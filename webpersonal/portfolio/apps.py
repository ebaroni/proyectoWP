from django.apps import AppConfig

# se creó esta clase , agrego verboses y clase Meta
class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
    verbose_name = 'Portafolio'


