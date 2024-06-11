import os.path
from django.shortcuts import HttpResponse, render
from shop.models import Product
from shop import ProductSerializer as ps
import simplejson
from django.views.decorators.csrf import csrf_exempt

UPLOAD_DIR = os.path.dirname(__file__) + '/static/images/'
#파일 업로드   현재 실행중 파일 디렉토리

def home(request):
    return render(request, "index.html")

def list(request):
    # 검색기능을 위해
    try:
        product_name = request.GET["product_name"]
    except:
        product_name = ""

    items = Product.objects.filter(product_name__contains=product_name).order_by("-product_name") #필드명 like %키워드%
    serializer = ps.ProductSerializer(items, many=True)
    return HttpResponse(simplejson.dumps(serializer.data))

@csrf_exempt #csrf 면제, 서버에 post 방식 전달
def insert(request):
    if "img" in request.FILES: #첨부파일 리스트
        #<input type='file' ref={img} /> name 맞춰주기
        file = request.FILES["img"]
        file_name = file._name
        fp = open("%s%s" % (UPLOAD_DIR, file_name), "wb")
        #         % 위치(s :스트링)       write binary
        for chunk in file.chunks():
            #             조각들
            fp.write(chunk)
        fp.close() # 파일 닫기, 완성
    else:
        file_name = "-"
    row = Product(product_name=request.POST["product_name"], description=request.POST["description"],
                  price=request.POST["price"], filename=file_name)
    row.save() # 레코드 저장
    #리액트==> insert()
    #           fetch()
def detail(request, product_code):
    row = Product.objects.get(product_code=product_code)
    serializer = ps.ProductSerializer(row)
    #객체==>바이트배열(객체 직렬화)
    return HttpResponse(simplejson.dumps(serializer.data))

@csrf_exempt
def update(request):
    product_code = request.POST['product_code']
    row_src = Product.objects.get(product_code=product_code)

    filename = row_src.filename
    if "img" in request.FILES:
        file = request.FILES["img"]
        filename = file._name

        fp = open("%s%s" % (UPLOAD_DIR, filename), "wb")
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()

    row_new = Product(product_code=product_code,
                      product_name=request.POST["product_name"],
                      description=request.POST["description"],
                      price=request.POST["price"],
                      filename=filename)

    row_new.save()

@csrf_exempt
def delete(request):
    Product.objects.get(product_code=request.GET["product_code"]).delete()

