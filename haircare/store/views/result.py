from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from django.views import View


# Create your views here.
class IndexR(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('res') 


    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/result')

def result(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    type = request.session.get('type')
    density = request.session.get('density')
    condition = request.session.get('condition')
    hairfall = request.session.get('hairfall')
    dandruff = request.session.get('dandruff')
    discoloration = request.session.get('discoloration')

    categories = Category.get_all_categories()
    
    products = Products.get_products_by_type_density(type,density).filter(problem__contains=condition)
    if hairfall == "yes":
        products = products | Products.get_products_by_type_density(type,density).filter(problem__contains="hairfall")
    if dandruff == "yes":
        products = products | Products.get_products_by_type_density(type,density).filter(problem__contains="dandruff")
    if discoloration != "no":
        products = products | Products.get_products_by_type_density(type,density).filter(problem__contains=discoloration)

    data = {}
    data['products'] = products
    data['categories'] = categories

    print(type, density, condition, hairfall, dandruff, discoloration)
    print('you are : ', request.session.get('email'))
    return render(request, 'result.html', data)