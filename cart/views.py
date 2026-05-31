from django.shortcuts import render,redirect,get_object_or_404
from store.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def cart(request,total=0,quantity=0,total_after_tax=0 ,cart_item=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.filter(cart=cart,is_active=True)

        for item in cart_item:
            total += (item.quantity * item.product.product_price)
            quantity += item.quantity
        total_after_tax =  total + 10
        
    except ObjectDoesNotExist:
        pass
    context = {
        'total':total,
        'quantity':quantity,
        'cart_item':cart_item,
        'total_after_tax':total_after_tax,
    }
    return render(request,'store/cart.html',context)

@login_required(login_url='login_account')
def add_to_cart(request,product_id):
    product = Products.objects.get(id=product_id)

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))  # get the cart id present in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product,cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            quantity = 1,
        )
        cart_item.save()
    return redirect('cart')


def remove_cart_item(request, product_id):
    product = get_object_or_404(
        Products,
        id=product_id
    )
    cart = get_object_or_404(
        Cart,
        cart_id=_cart_id(request)
    )
    cart_item = get_object_or_404(
        CartItem,
        cart=cart,
        product=product,
        is_active=True
    )
    cart_item.delete()
    return redirect('cart')
        

def count_decrease(request,product_id):
    try:
        product = Products.objects.get(id=product_id)
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(cart=cart,product=product,is_active=True)

        if cart_item.quantity <= 1:
            cart_item.delete()
        else:
            cart_item.quantity -= 1
            cart_item.save()
        return redirect('cart')
    except ObjectDoesNotExist:
        pass

@login_required(login_url='login_account')
def checkout(request,total=0,quantity=0,cart_item=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart,is_active=True)

        for item in cart_items:
            total += (item.quantity * item.product.product_price)
            quantity += item.quantity
    except ObjectDoesNotExist:
        pass
    context = {
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        
    }
    return render(request,'store/checkout.html',context)
    
