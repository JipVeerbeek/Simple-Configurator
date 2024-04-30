from django.contrib import admin
from .models import Product, Product_question


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


class ProductQuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "product_id", "question_id"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Product_question, ProductQuestionAdmin)
