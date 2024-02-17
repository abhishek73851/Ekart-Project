from ecommapp.models import Product
from django.forms import ModelForm


class ViewProduct(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        # fields = [
        #     "product_id",
        #     "product_name",
        #     "category",
        #     "desc",
        #     "price",
        #     "image",
        # ]
