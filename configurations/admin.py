from django.contrib import admin
from .models import Configuration, Address, ConfigurationLine


class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ["id", "address_id", "product_id", "status"]


class ConfigurationLineAdmin(admin.ModelAdmin):
    list_display = ["id", "product_question_article_id", "configuration_id"]


class AddressAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "middle_name", "last_name", "address", "city", "postal_code"]


admin.site.register(Configuration, ConfigurationAdmin)
admin.site.register(ConfigurationLine, ConfigurationLineAdmin)
admin.site.register(Address, AddressAdmin)
