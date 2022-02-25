from django.shortcuts import render, redirect, get_object_or_404
from .models import Product,Category, Review,ContactUs,order
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect, request
from django.views.generic import ListView,DetailView,CreateView
from datetime import date
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import ReviewForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib import messages
from django.contrib.auth.models import User


class home(ListView):
    
    model = Product
    template_name = 'index.html'
    ordering = ['-product_created_date']
   

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['categories'] = Category.objects.all()
        context['latest_products'] = Product.objects.filter().order_by('-product_created_date')[0:4]
        return context



class SearchResultsView(ListView):
    model = Product
    template_name = 'search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(name__icontains=query) | Q(product_description__icontains=query)
        )
        
        return object_list


class Products(ListView):
    
    model = Product
    template_name = 'product-list.html'
    ordering = ['-product_created_date']
    paginate_by = 6
    

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        product_categories = Category.objects.all() 
        context['categories'] = product_categories

        #context['filtered_product']= Product.objects.filter(product_category = product_categories.category_name)   
        
        paginator = Paginator(products, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            product = paginator.page(page)
        except PageNotAnInteger:
            product = paginator.page(1)
        except EmptyPage:
            product = paginator.page(paginator.num_pages)

        context['products'] = product

        return context

    

class Product_Detail(DetailView):
    
    form_class = ReviewForm
    model = Product
    template_name = 'product-detail.html'
    


    def get_context_data(self, *args, **kwargs):
        
        context = super().get_context_data( *args, **kwargs)
        product_details = get_object_or_404(Product,id=self.kwargs['pk'])
        context['product_detail'] = product_details
        context['categories'] = Category.objects.all()  
        context['products'] = Product.objects.all()
        context['related_products'] = Product.objects.filter(product_category = product_details.product_category)
        

        return context



def ReviewProduct(request,pk):
    
    product =get_object_or_404(Product,id= pk)
    name = request.POST['name']
    email = request.POST['email']
    review_body = request.POST['review_body']
    
   
    if request.method == 'POST':
        R = Review(product=product, name=name,email=email, review_body = review_body, date_add=datetime.now())
        R.save()
        messages.success(request,"Sucessfully reviewed the product.") 
        return redirect('product_detail',pk = product.id )



@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    messages.success(request,"Item is added to your cart.")
    return redirect("products")

@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    messages.warning(request,"Item is removed from your cart.")

    return redirect("cart_detail")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    messages.error(request,"All items in your cart has been removed.")
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_detail(request):

    return render(request, 'cart.html')




def contact(request):
    
   
    sender_name = request.POST.get('name')
    sender_email = request.POST.get('email')
    sender_message = request.POST.get('message')
    
   
    if request.method == 'POST':
        contacts = ContactUs(name=sender_name,email=sender_email, message = sender_message, date_sent=datetime.now())
        contacts.save()
        messages.success(request,"Message Sent.") 
        return redirect('contact_us')   
    
    return render(request,"contact.html")


def orders(request):
    
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    orderd_by = User.objects.only('id').get(id=request.user.id)
    mobile_no = request.POST.get('mobile_no')
    adress = request.POST.get('adress')
    city = request.POST.get('city')
    product_name = request.POST.get('product_nam')
    price = request.POST.get('product_price')
    quantity = request.POST.get('prod_quant')
    total_price = request.POST.get('prod_total_pr')
    shipping_cost = float(50.0)
    grand_total = request.POST.get('grand_total')
    sub_total =  request.POST.get('total_price')
    payment_method = request.POST.get('pay_method')
    

    if request.method == 'POST':

        order_item = order(First_name=first_name, Last_name=last_name, 
        Orderd_by = orderd_by, Mobile_no=mobile_no,Adress=adress,City=city,
        Product_name=product_name,Price=price ,Quantity=quantity ,Total_price=total_price,
        Shipping_cost=shipping_cost,Grand_total=grand_total,Sub_total=sub_total,
        Payment_method= payment_method ,Orderd_date=datetime.now())

        order_item.save()
        messages.success(request,"Sucessfully Orderd.") 
        return redirect('cart_clear')    
   
    return render(request,"checkout.html")

