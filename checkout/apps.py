from django.apps import AppConfig
# code from boutique abo

class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals
        