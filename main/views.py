from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as log
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def register(request):

    if request.method =="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('index')




    return render(request, 'register.html')




def login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            log(request, user)
            return redirect('index')
        else:
            return redirect('login')

    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')



def index(request):
    story = Story.objects.last()
    product = Product.objects.all().order_by('-id')[:4]
    news = News.objects.all()
    ins_img = Inst_img.objects.all()
    context = {
        'story': story,
        'product': product,
        'news': news,
        'ins_img': ins_img
    }
    return render(request, 'index.html', context)

@login_required(login_url='/login/')
def about(request):
    story = Story.objects.last()
    commentary = Comment.objects.all().order_by('-id')[:3]
    team = Team.objects.all().order_by('-id')[:3]

    context = {
        'story': story,
        'team': team,
        'commentary': commentary,

    }

    return render(request, 'about.html', context)

@login_required(login_url='/login/')
def blog(request):
    blog = News.objects.all()
    post = Post.objects.all()
    contex = {
        'blog': blog,
        'post': post,
    }

    return render(request, 'blog.html', contex)

def shop(request):
    product = Product.objects.all()
    latest = Product.objects.filter(category='Latest').order_by('-id')[:3]
    featured = Product.objects.filter(category='FEAUTURED').order_by('-id')[:3]
    popular = Product.objects.filter(category='Popular').order_by('-id')[:3]
    contex = {
        'product': product,
        'latest': latest,
        'featured': featured,
        'popular': popular,
    }

    return render(request, 'shop.html', contex)


@login_required(login_url='/login/')
def shop_cart(request):
    total = 0
    cart = Cart.objects.filter(user=request.user)
    number = Cart.objects.filter(user=request.user).count()
    for i in Cart.objects.filter(user=request.user):
        if i.product.discount_price :
            total += i.product.discount_price
        else:
            total += i.product.price

    contex = {
        'cart': cart,
        'number': number,
        'total': total,
    }

    return render(request, 'shop_cart.html', contex)
@login_required(login_url='/login/')
def shop_checkout(request):
    total = 0
    cart = Cart.objects.filter(user=request.user)
    number = Cart.objects.filter(user=request.user).count()
    for i in Cart.objects.filter(user=request.user):
        if i.product.discount_price:
            total += i.product.discount_price
        else:
            total += i.product.price
    contex = {
            'cart': cart,
            'number': number,
            'total': total,
        }

    user = request.user
    if request.method == 'POST':
        name = request.POST['name']
        last_name = request.POST['last_name']
        country = request.POST['country']
        city = request.POST['city']
        zip_code = request.POST['zip_code']
        phone = request.POST['phone']
        email = request.POST['email']
        note = request.POST['note']
        Shipping.objects.create( name=name,
                                last_name=last_name,
                                country=country,
                                city=city, zip_code=zip_code,
                                phone=phone, email=email,
                                note=note)
        s = Cart.objects.filter(user=request.user)
        for i in s:
            i.delete()
        redirect('shop_checkout')


    return render(request, 'shop_checkout.html', contex)

@login_required(login_url='/login/')
def base(request):
    number = Cart.objects.filter(user=request.user).count()

    contex = {
        'number': number,

    }
    return render(request, 'base.html', contex)


@login_required(login_url='/login/')
def add_cart(request, pk):
    user = request.user
    product = Product.objects.get(id=pk)
    c = Cart.objects.filter(product=product).count()
    if c > 0:
        pass
    else:
        Cart.objects.create(user=user, product=product)
    return redirect('shop')
@login_required(login_url='/login/')
def del_cart(request, pk):
    Cart.objects.get(id=pk).delete()
    return redirect('index')




@login_required(login_url='/login/')
def blog_single(request, pk):
    blog_sin = News.objects.get(id=pk)
    post = Post.objects.all()
    comment = Comment.objects.all().order_by('-id')[:3]
    if request.method == "POST":
        user = request.user
        username = user.username
        email = user.email
        comment = request.POST['comment']
        Comment.objects.create(name=username, email=email, comment=comment)
    contex = {
        'blog': blog_sin,
        'post': post,
        'comment': comment,
    }
    return render(request, 'blog_single.html', contex)




@login_required(login_url='/login/')
def shop_single(request, pk):
    single = Product.objects.get(id=pk)
    product = Product.objects.all().order_by('-id')[:4]

    contex = {
        'single': single,
        'product': product
    }

    return render(request, 'shop_single.html', contex )

@login_required(login_url='/login/')
def shop_list(request):
    return render(request, 'shop_list.html')


@login_required(login_url='/login/')
def contact(request):
    if request.method == 'POST':
        name = request.POST['contact-name']
        phone = request.POST['contact-phone']
        email = request.POST['contact-email']
        subject = request.POST['contact-subject']
        message = request.POST['contact-message']
        Contact.objects.create(name=name, phone=phone, email=email, subject=subject, message=message)
    return render(request, 'contact.html')





