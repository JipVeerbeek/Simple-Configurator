from django.contrib import admin
from .models import Configuration, Adress, ConfigurationLine


class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ["id", "adress_id", "product_id", "status"]


class ConfigurationLineAdmin(admin.ModelAdmin):
    list_display = ["id", "product_question_article_id", "configuration_id"]


class AdressAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "middle_name", "last_name", "adress", "city", "postal_code"]


admin.site.register(Configuration, ConfigurationAdmin)
admin.site.register(ConfigurationLine, ConfigurationLineAdmin)
admin.site.register(Adress, AdressAdmin)
