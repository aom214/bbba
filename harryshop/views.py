from django.shortcuts import render,redirect,get_object_or_404
from harryshop.models import Product,Category,CartItem
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.db.models import Sum,F
# Create your views here.
def shop(request):
    if request.user.is_authenticated:
        category=Category.objects.all()
        product=Product.objects.all()
        params={"category":category,"product":product}
        return render(request, 'shop.html',params)
    else:
        messages.warning(request, 'YOU CAN VISIT SHOP ONLY AFTER LOGIN')
        return redirect('/sign')
def products(request,product_cate, product_id):
    PRODUCT=Product.objects.filter(id=product_id)
    p = Category.objects.get(name=product_cate)
    pro=Product.objects.filter(product_category=p)
    product = get_object_or_404(Product, pk=product_id)
    if request.method=="POST":
        product_quantity=int(request.POST.get('quantity',1))
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        cart_item.quantity=product_quantity
        cart_item.save()
        request.session.save()
    car=CartItem.objects.filter(user=request.user)

    cart_items=CartItem.objects.filter(user=request.user,product=product_id).exists()
    param={'product':PRODUCT,'allprod':pro,'cartitemss':cart_items}
    return render(request,'product.html',param)
def addtocart(request,product_id):
    return redirect('product.product_category/product.product_name')
def cart(request):
    if request.method=="POST":
        product_quantity=int(request.POST.get('quantity',1))
        productid=request.POST.get('productid')
        cart_items, created = CartItem.objects.get_or_create(user=request.user, product=productid)
        cart_items.quantity=int(product_quantity)
        cart_items.save()
    cart_it = CartItem.objects.filter(user=request.user)
    total_price = cart_it.annotate(item_total=F('quantity') * F('product__product_price')).aggregate(total=Sum('item_total'))['total'] or 0
    total_TAX=total_price*5/100
    product=Product.objects.all()
    if cart_it:
        delevery_fees=60
        price_after_tax_delevery=total_price+ total_TAX + delevery_fees
    else:
        delevery_fees = 0
        price_after_tax_delevery=total_price+ total_TAX
    params = {'cartitemss': cart_it, 'total_price': total_price,'total_tax':total_TAX,'price_includes':price_after_tax_delevery,'delevery_fees':delevery_fees,'product':product}
    return render(request,'cart.html',params)

def removeproduct(request,product_id):
    cart_ite, created = CartItem.objects.get_or_create(user=request.user, product=product_id)
    cart_ite.delete()
    return redirect('/shop/cart')