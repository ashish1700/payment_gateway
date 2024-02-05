from django.shortcuts import render
import razorpay

from .models import Coffee
from django.views.decorators.csrf import csrf_exempt  
# Create your views here.



def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = int(request.POST.get("amount")) * 100
        client = razorpay.Client(auth=("rzp_test_W4oqXTwXWe8a70","cZ8ye2LMIWhQygpjPTnzvrrA"))
        
        payment = client.order.create({'amount': amount,'currency': 'INR','payment_capture': '1'})
        print(payment)
        coffee = Coffee(name=name, amount=amount, payment_id=payment['id'])
        
        coffee.save()
        return render(request, "index.html", {'payment': payment})
        
    return render(request, "index.html")

@csrf_exempt
def sucess(request):
    if request.method == "POST":
        a = request.POST  # Fix the typo here
        order_id = ""
        for key, val in a.items():
            if key == "razor_order_id":
                order_id = val
                break
        user = Coffee.objects.filter(payment_id=order_id).first()
        if user:
            user.paid = True
            user.save()
    return render(request, "sucess.html")
