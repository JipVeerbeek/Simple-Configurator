from django.contrib import admin
from .models import Configuration, Address, ConfigurationLine


class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ["id", "address", "product", "status"]


class ConfigurationLineAdmin(admin.ModelAdmin):
    list_display = ["id", "product_question_article", "configuration"]


class AddressAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "middle_name", "last_name", "address", "city"]


admin.site.register(Configuration, ConfigurationAdmin)
admin.site.register(ConfigurationLine, ConfigurationLineAdmin)
admin.site.register(Address, AddressAdmin)
