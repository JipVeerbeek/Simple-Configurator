from django.contrib import admin

from .models import Product, ProductQuestion, ProductQuestionArticle


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


class ProductQuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "product", "question"]


class ProductQuestionArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "product_question", "article", "price"]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductQuestion, ProductQuestionAdmin)
admin.site.register(ProductQuestionArticle, ProductQuestionArticleAdmin)
