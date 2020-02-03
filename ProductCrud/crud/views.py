from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from .models import Product
from .models import Category
from .forms import UploadFileForm
from googletrans import Translator

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, "index.html",{"products": products})

def createProduct(request):
    if request.method == 'GET':
        return render(request,"create-product.html")
    else:
        translator = Translator()
        name = request.POST.get("name")
        description = request.POST.get("description")
        description_translate = translator.translate(description, dest = "az").text
        price = request.POST.get("price")
        image = request.FILES['image']
        new_product = Product(name = name, description = description, description_translate = description_translate , price = price, category = Category.objects.get(id = 1), image = image)
        new_product.save()
        return redirect("/")


def deleteProduct(request,id):
    product = get_object_or_404(Product,id = id)
    product.delete()
    return redirect("/")

def updateProduct(request,id):
    if request.method == 'GET':
        product = get_object_or_404(Product, id = id)
        return render(request,"update-product.html",{"product": product})
    else:
        translator = Translator()
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        image = request.FILES['image']

        product = get_object_or_404(Product, id = id)
        product.name = name
        product.description =description
        product.description_translate = translator.translate(description, dest="az").text
        product.price = price
        product.image = image
        product.save()

        return redirect("/")
