from django.contrib import admin
from .models import Product, ProductQuestion, ProductQuestionArticle


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


class ProductQuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "product_id", "question_id"]


class ProductQuestionArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "product_question_id", "article_id", "price"]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductQuestion, ProductQuestionAdmin)
admin.site.register(ProductQuestionArticle, ProductQuestionArticleAdmin)
