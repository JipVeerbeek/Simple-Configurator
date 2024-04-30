from django.contrib import admin
from .models import Configuration, Adress, Configuration_line


class AdressAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "middle_name", "last_name", "adress", "city", "postal_code"]


class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ["id", "adress_id", "product_id", "status"]


class ConfigurationLineAdmin(admin.ModelAdmin):
    list_display = ["id", "product_question_article_id", "configuration_id"]


admin.site.register(Adress, AdressAdmin)
admin.site.register(Configuration, ConfigurationAdmin)
admin.site.register(Configuration_line, ConfigurationLineAdmin)
