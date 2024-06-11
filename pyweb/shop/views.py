from django.shortcuts import render, redirect
from shop.models import Product, Cart

UPLOAD_DIR = "c:/work/pyweb/shop/static/images/"

def product_list(request):
    productList = Product.objects.order_by("product_name")
    return render(request,"shop/product_list.html",{"productList":productList,"count":len(productList)})

def product_write(request):
    if request.session.get("userid",False): #로그인상태
        return render(request,"shop/product_write.html")
    else: #로그아웃 상태면 로그인창 뜸
        return redirect("/mymember/login")

def product_insert(request):
    if "file1" in request.FILES:
        file = request.FILES["file1"] #첨부파일이름
        file_name = file._name
        fp = open("%s%s" % (UPLOAD_DIR, file_name), "wb") # %:위치
        #         "c:/work/pyweb/shop/static/images/%s
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
    else:
        file_name = "-"

    row = Product(product_name=request.POST["product_name"], description=request.POST["description"],price=request.POST["price"], picture_url=file_name)
    row.save()
    return redirect("/shop/product_list")

def product_detail(request):
    pid = request.GET["product_id"]
    row = Product.objects.get(product_id=pid)
    return render(request, "shop/product_detail.html", {"row": row, "range": range(1, 21)}) #range 생성

def product_edit(request):
    if request.session.get("userid", False):
        pid = request.GET["product_id"]
        row = Product.objects.get(product_id=pid)
        return render(request, "shop/product_edit.html", {"row": row})
    else:
        return redirect("/mymember/login")

def product_update(request):
    id = request.POST['product_id']
    row_src = Product.objects.get(product_id=id)
    p_url = row_src.picture_url
    if "file1" in request.FILES:
        file = request.FILES["file1"]
        p_url = file._name
        fp = open("%s%s" % (UPLOAD_DIR, p_url), "wb")
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
    row_new = Product(product_id=id, product_name=request.POST["product_name"],description=request.POST["description"], price=request.POST["price"], picture_url=p_url)
    row_new.save()
    return redirect("/shop/product_list")

def product_delete(request):
    Product.objects.get(product_id=request.POST["product_id"]).delete()
    return redirect("/shop/product_list")

def cart_insert(request):
    uid = request.session.get("userid", "")
    if uid != "": #로그인상태
        row = Cart(userid=uid, product_id=request.POST["product_id"], amount=request.POST["amount"])
        row.save()
        return redirect("/shop/cart_list")
    else:
        return redirect("/mymember/login")

def cart_list(request):
    uid = request.session.get("userid","")
    if uid !="": #로그인상태
        #raw : sql 직접작성
        cartList = Cart.objects.raw("""
        select cart_id, userid, amount, c.product_id, product_name, amount*price money
        from shop_cart c, shop_product p
        where c.product_id = p.product_id and userid ='{0}'
        """.format(uid))
        sumMoney = 0 #총금액(배송료 제외)
        fee = 0 #배송료
        total = 0 #총금액(배송료 포함)
        cartCount = len(cartList)
        if cartCount > 0:
            #장바구니 금액 합계(raw 쿼리에는 반드시 PK가 포함되어야 함)
            sumRow = Cart.objects.raw("""
            select sum(amount*price) cart_id
            from shop_cart c, shop_product p
            where c.product_id = p.product_id and userid='{0}'
            """.format(uid))
            sumMoney = sumRow[0].cart_id
            #배송료
            if sumMoney != None and sumMoney >= 50000:
                fee = 0
            else:
                fee = 2500

            if sumMoney != None:
                total = sumMoney + fee
            else:
                sumMoney = 0
                total = 0
            return render(request, \
                          "shop/cart_list.html",
                          {"cartList": cartList, "cartCount": len(cartList), "sumMoney": sumMoney, "fee": fee,
                           "total": total})
        else:
            return redirect("/mymember/login")

def cart_update(request):
    uid = request.session.get("userid", "")
    if uid != "":
        amt = request.POST.getlist('amount')
        cid = request.POST.getlist('cart_id')
        pid = request.POST.getlist('product_id')
        for idx in range(len(cid)):
            row = Cart(cart_id=cid[idx], userid=uid, product_id=pid[idx], amount=amt[idx])
            row.save()
        return redirect("/shop/cart_list")
    else:
        return redirect("/mymember/login")

def cart_del(request):
    Cart.objects.get(cart_id=request.GET["cart_id"]).delete()
    return redirect("/shop/cart_list")

def cart_del_all(request):
    uid = request.session.get("userid", "")
    if uid != "":
        Cart.objects.filter(userid=uid).delete() #여러레코드
        return redirect("/shop/cart_list")
    else:
        return redirect("/mymember/login")