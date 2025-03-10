from django.shortcuts import render, redirect
from shopping.models import UserProfile, UserDetails, Product, Order,Cart
from django.shortcuts import render, get_object_or_404

def home(request):
  return render(request,"./shopping/home.html")

def signup_page(request):
  if request.method == "POST":
    username = request.POST.get("username")
    firstname = request.POST.get("firstname")
    lastname = request.POST.get("lastname")
    email = request.POST.get("email")
    password = request.POST.get("password")
    
    UserProfile.objects.create(
      username = username,
      first_name = firstname,
      last_name = lastname,
      email = email,
      password = password
    )
    
    return redirect("signup")
  return render(request,"./shopping/signup.html")

def login_page(request):
  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")
    
    user = UserProfile.objects.filter(username = username, password = password).first()
    
    if user:
      request.session["username"] = user.username
      request.session["userid"] = user.id
      request.session["firstname"] = user.first_name
      return redirect("productpage")
    else:
      return redirect("login")
  return render(request, "./shopping/login.html")


def products(request):
    if "firstname" not in request.session:
        return redirect("login")
    
    user = request.session.get("firstname")
    user_id = request.session.get("userid")
    
    search_query = request.POST.get("search")

    if search_query:
        products = Product.objects.filter(product_name__istartswith=search_query)
    else:
        products = Product.objects.all()

    user_dp = UserDetails.objects.filter(user_id=user_id).first()
    
    response =  render(request, "./shopping/products.html", {
        "user": user,
        "products": products,
        "profile_pic": user_dp
    })
    response["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response["Pragma"] = "no-cache"
    return response







def product_details(request, product_id):
    if "userid" not in request.session:
        return redirect("login")
    try:
        product = Product.objects.filter(id=product_id).first()
        specifications_list = product.specification.split("\n") 
    except Product.DoesNotExist:
        return redirect('product_not_found') 

    response =  render(request, "./shopping/product_details.html", {"product": product,"spec_list": specifications_list})
    
    response["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response["Pragma"] = "no-cache"




def add_details(request):
    if "userid" not in request.session:
        return redirect("login")
    
    userid = request.session.get("userid")
    
    try:
        user = UserProfile.objects.get(id=userid) 
    except UserProfile.DoesNotExist:
        return redirect("login") 

    if request.method == "POST":
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        pin = request.POST.get("pin")
        city = request.POST.get("city")
        state = request.POST.get("state")
        country = request.POST.get("country")
        dp = request.FILES.get("dp")
        
        UserDetails.objects.create(
            user=user, 
            phone_number=phone,
            address=address,
            pin_code=pin,
            city=city,
            state=state,
            country=country,
            user_dp=dp
        )

        return redirect("productpage") 

    return render(request, "./shopping/add_details.html")

def Add_To_Cart(request, id):
    if "userid" not in request.session:
        return redirect("login")
    userid = request.session.get("userid")
    
    a = UserProfile.objects.get(id = userid)
    b = Product.objects.get(id = id)
    Cart.objects.create(
        user_id = a.id,
        product_id = b.id
    )   
    response =  redirect("productpage")
    response["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response["Pragma"] = "no-cache"
    return response

def Cart_data(request):
    if "userid" not in request.session:
        return redirect("login")
    userid = request.session.get("userid")
    user = UserProfile.objects.filter(id = userid).first()
    
    data = Cart.objects.filter(user_id = user.id)
    a = ""
    for j in data:
        a = j.product.specification.split("\n")
        
    
    response =  render(request,"./shopping/Cart.html",{"data":data,"spec":a})
    response["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response["Pragma"] = "no-cache"
    return response



    
    
def display(request):
    if "firstname" not in request.session: 
        return redirect("login")

    user = request.session.get("firstname")
    
    response = render(request, "shopping/display.html", {"user": user})
    response["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response["Pragma"] = "no-cache"
    
    return response

def logout_page(request):
    request.session.flush()
    return redirect("login")
