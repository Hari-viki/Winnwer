from django.shortcuts import render,redirect,get_object_or_404
from .form import newac,sadac
from .models import User,Transaction,SADUser,SADtransaction
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponseBadRequest
from datetime import datetime
from django.contrib import messages

def home(request):
    
    return render(request,'web/home.html')

STATIC_USERNAME = 'thangakumar.@wbpfl.com'
STATIC_PASSWORD = 'thangakumar'
@csrf_exempt
def admin1(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if username == STATIC_USERNAME and password == STATIC_PASSWORD:
            messages.success(request, 'Login successful!')
            return redirect('adminuser')
        else:
            messages.error(request, 'Login failed.')
    
    # return render(request, 'login_app/login.html')
    return render(request,'web/adminpanel.html')

def SADadmin(request):
    transaction_details = {}

    if request.method == 'POST':
        transaction_date = request.POST.get('transaction_date')
        
        if transaction_date:
            target_date = datetime.strptime(transaction_date, '%Y-%m-%d').date()
            
            users = SADUser.objects.all()
            transaction_details = {}
            
            for user in users:
                user_transactions = SADtransaction.objects.filter(usernum=user, date=target_date)
                if user_transactions.exists():
                    transaction_details[user] = user_transactions

    context = {'transaction_details': transaction_details}

    return render(request,'web/adminSAD.html',context)

def adminuser(request):

    transaction_details = {}

    if request.method == 'POST':
        transaction_date = request.POST.get('transaction_date')
        
        if transaction_date:
            target_date = datetime.strptime(transaction_date, '%Y-%m-%d').date()
            
            users = User.objects.all()
            transaction_details = {}
            
            for user in users:
                user_transactions = Transaction.objects.filter(userid=user, date=target_date)
                if user_transactions.exists():
                    transaction_details[user] = user_transactions

    context = {'transaction_details': transaction_details}
    return render(request, 'web/adminuserdetails.html', context)



def DSA(request):
    if request.method=='POST':
        num=request.POST.get('num')
        data=User.objects.filter(num=num)
        print(data)
        transaction = Transaction.objects.filter(userid=num)
        
        return render(request,'web/deposit.html',{'data':data,'transaction':transaction})
    return render(request,'web/deposit.html')

def SAD(request):
    if request.method=='POST':
        num=request.POST.get('num')
        data=SADUser.objects.filter(num=num)
        print(data)
        transaction = SADtransaction.objects.filter(usernum=num)
        
        return render(request,'web/depositSAD.html',{'data':data,'transaction':transaction})
    return render(request,'web/depositSAD.html')


@csrf_exempt
def new(request):
    # print('hello')
    if request.method=='POST':
        newacc=newac(request.POST)
        # print(newacc)
        if newacc.is_valid():
            # print('hello')
            newacc.save()
            print("Save")
            return redirect('home')
    else:
        newacc=newac()
        # return redirect('home')
    return render(request,'web/New.html',{'form':newacc})


@csrf_exempt
def handle_deposit(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        amount = request.POST.get('amount')
        withdraw_amount = request.POST.get('withdraw')
        print(id, amount, withdraw_amount)
        
        user = get_object_or_404(User, id=id)
        
        if user:
            if amount:
                if user.totalamount is None:
                    user.totalamount = int(amount)
                else:
                    user.totalamount += int(amount)
            elif withdraw_amount is not None:  
                if user.totalamount is None:
                    user.totalamount = int(withdraw_amount)
                else:
                    user.totalamount -= int(withdraw_amount)

            user.save()
            
            data = User.objects.filter(num=id)
            total = User.objects.all()
            print('total : ',total)
            if amount:
                Transaction.objects.create(userid=user, deposit=int(amount))
            elif withdraw_amount is not None:  
                Transaction.objects.create(userid=user, withdraw=int(withdraw_amount))

            
            transaction = Transaction.objects.filter(userid=id)
            qs=[q.userid for q in transaction]
            
            for user in qs:
                print("User:", user.name)
                print("Total Amount:", user.totalamount)
                print("--")
            return render(request, 'web/deposit.html', {'data': data, 'transaction': transaction})

    return HttpResponseBadRequest("Invalid request")

@csrf_exempt
def handle_depositSAD(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        amount = request.POST.get('amount')
        withdraw_amount = request.POST.get('withdraw')
        print(id, amount, withdraw_amount)
        
        user = get_object_or_404(SADUser, id=id)
        
        if user:
            if amount:
                if user.totalamount is None:
                    user.totalamount = int(amount)
                else:
                    user.totalamount += int(amount)
            elif withdraw_amount is not None:  
                if user.totalamount is None:
                    user.totalamount = int(withdraw_amount)
                else:
                    user.totalamount -= int(withdraw_amount)

            user.save()
            
            data = SADUser.objects.filter(num=id)
            total = SADUser.objects.all()
            print('total : ',total)
            if amount:
                SADtransaction.objects.create(usernum=user, deposit=int(amount))
            elif withdraw_amount is not None:  
                SADtransaction.objects.create(usernum=user, withdraw=int(withdraw_amount))

            
            transaction = SADtransaction.objects.filter(usernum=id)
            qs=[q.usernum for q in transaction]
            
            for user in qs:
                print("User:", user.name)
                print("Total Amount:", user.totalamount)
                print("--")
            return render(request, 'web/depositSAD.html', {'data': data, 'transaction': transaction})

        return HttpResponseBadRequest("Invalid request")

@csrf_exempt
def SADAcc(request):
    if request.method=='POST':
        sad=sadac(request.POST)
        # print(newacc)
        if sad.is_valid():
            # print('hello')
            sad.save()
            print("Save")
            return redirect('home')
    else:
        sad=sadac()
        # return redirect('home')
    return render(request,'web/SAD.html',{'form':sad})