from django.apps import AppConfig
# Some code here taken from boutique ado project

class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals