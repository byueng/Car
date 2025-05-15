# built-in libaray
import time 
from json import loads

# django libaray
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# other python files
from .serializer import *
from .models import *

# complete
@csrf_exempt
def test(request):
    '''
    Use for testing
    '''
    return HttpResponse(f"test successfully, current time: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}")

class RemoveFavoriteView(APIView):
    """
    处理取消收藏车辆的请求
    """
    @csrf_exempt
    def delete(self, request):
        """
        删除用户收藏的车辆
        请求体格式：
        {
            "car_id": "车辆ID",
            "user_id": "用户ID"
        }
        """
        car_id = request.data.get('car_id')
        user_id = request.data.get('user_id')

        if not car_id or not user_id:
            return Response({'message': '缺少 car_id 或 user_id'}, status=400)

        try:
            favorite = FavoriteCar.objects.filter(user_id=user_id, car_id=car_id)
            favorite.delete()
            return Response({'message': '取消收藏成功！'}, status=200)
        except FavoriteCar.DoesNotExist:
            return Response({'message': '收藏记录不存在！'}, status=404)
        except Exception as e:
            return Response({'message': f'取消收藏失败: {str(e)}'}, status=500)

class ProfileView(APIView):
    # permission_classes = [IsAuthenticated]  

    # complete
    @csrf_exempt
    def get(self, request):
        account = request.GET.get('id')
        try:
            if not account:
                return Response({"message": "用户不存在"}, status=404)

            # 获取用户信息
            user = User.objects.get(account=account)
            try:
                profile = Profile.objects.get(user=user)
            except Profile.DoesNotExist:
                return Response({"message": "用户资料不存在"}, status=404)

            # 序列化用户信息
            user_data = {
                "account": user.account,
                "email": profile.email,
                "phone": profile.phone,
                "birthdate": profile.birthdate.strftime('%Y-%m-%d') if profile.birthdate else None
            }
            favorite_cars = FavoriteCar.objects.filter(user=user).distinct()
            car_ids = favorite_cars.values_list('car_id', flat=True)
            cars = CarInfo.objects.filter(id__in=car_ids)
            favorite_cars_data = [
                {
                    "car_id": car.id,
                    "car_brand": car.brand,
                    "car_model": car.model,
                    "car_price": car.price,
                    "car_image": f"http://localhost:8000{car.image.url}"
                }
                for car in cars
            ]
            # 返回数据
            return Response({
                "user": user_data,
                "favorite_cars": favorite_cars_data
            }, status=200)

        except User.DoesNotExist:
            return Response({'message': '用户不存在'}, status=404)
        except Exception as e:
            return Response({'message': '出错了，请重试', 'error': str(e)}, status=500)  


    @csrf_exempt
    def put(self, request):
        '''
        Put Http request, update the user information from front

        ProfileSerializer format:
        {
            "phone": "user_phone"
            "email": "user_email"
            "birthdate": "user_birthdate"
        }

        :param request: Http request object
        :return Respone: Json type respone with status 200 if successfully
        '''
        body = loads(request.body.decode('utf-8')) 
        user = User.objects.get(account=body['account'])
        profile = Profile.objects.get(user=user)
        profile.phone = body['phone']
        profile.email = body['email']
        profile.birthdate = body['birthdate']
        profile.save()
        serializers = ProfileSerializer(profile)
        return Response(serializers.data, status=200)

# complete
@csrf_exempt
def login(request):
    '''
    login API

    Expected body format:
    {
        "account": "user_account",
        "password": "user_password"
    }

    :param request: Http request object
    :return: JsonRespone with status 200 if successful
    '''
    if request.method == 'POST':
        body = loads(request.body.decode('utf-8')) 
        account = body['account']
        password = body['password']
        try:
            user = User.objects.get(account=account)  # 查询数据库
            if password == user.password:
                return JsonResponse({'message': '登录成功，2秒后跳转到主页'}, status=201)
            else:
                return JsonResponse({'message': '密码错误，请重试'}, status=404)        
        except User.DoesNotExist:
            return JsonResponse({'message': '用户不存在'}, status=404)       
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)

# complete
@csrf_exempt
def register(request):
    '''
    register API.

    Expected body format:
    {
        "account": "user_account",
        "password": "user_password",
    }

    :param request: Http request object
    :return: JsonRespone with status 200 if successful
    
    '''
    if request.method == 'POST':
        body = loads(request.body.decode('utf-8'))   
        account = body['account']
        password = body['password']
        flag = User.objects.filter(account=account).exists()        
        if flag:
            return JsonResponse({'message': '创建失败，新建用户名已存在，请重试'}, status=404)
        else:
            user = User(account=account, password=password)
            profile = Profile(user=user)
            user.save()
            profile.save()
            return JsonResponse({'message': '用户创建成功，2秒后自动跳转到登录界面'}, status=201)
    else:
        return JsonResponse({'message': '错误的请求类型'}, status=405)
    
@csrf_exempt
def forget_password(request):
    """
    forget password api
    Expected body format:
    {
        account: "user who forget password",
        newPassword: "new password",
        confirmPassword: "confirm new password"
    }
    """
    if request.method == 'POST':
        body = loads(request.body.decode('utf-8'))
        account = body['account']
        newPassword = body['newPassword']
        try:
            user = User.objects.get(account=account)
            user.password = newPassword
            user.save()
            return JsonResponse({'message': '密码修改成功, 两秒后跳转到登陆界面'}, status=201)

        except User.DoesNotExist:
            return JsonResponse({'message': '用户不存在'}, status=404)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
    
@csrf_exempt
def reserve(request):
    """
    预约接口
    请求体格式:
    {
        "user_id": "用户ID",
        "car_id": "车辆ID",
        "name": "姓名",
        "phone": "手机号",
        "idcard": "身份证号",
        "date": "预约日期(YYYY-MM-DD)",
        "place": "预约地点"
    }
    """
    if request.method == "POST":
        try:
            body = loads(request.body.decode('utf-8'))
            user_id = body.get('user_id')
            car_id = body.get('car_id')
            name = body.get('name')
            phone = body.get('phone')
            idcard = body.get('idcard')
            date = body.get('date')
            place = body.get('place')

            if not all([user_id, car_id, name, phone, idcard, date, place]):
                return JsonResponse({'message': '缺少必要参数'}, status=400)

            user = User.objects.get(account=user_id)
            car = CarInfo.objects.get(id=car_id)

            reserve = Reserve.objects.create(
                user=user,
                car=car,
                name=name,
                phone=phone,
                idcard=idcard,
                date=date,
                place=place
            )

            return JsonResponse({
                'message': '预约成功',
                'reserve_id': reserve.id,
                'reserve_info': {
                    'user': user.account,
                    'car': f"{car.brand} {car.model}",
                    'name': name,
                    'phone': phone,
                    'idcard': idcard,
                    'date': date,
                    'place': place
                }
            }, status=201)
        except User.DoesNotExist:
            return JsonResponse({'message': '用户不存在'}, status=404)
        except CarInfo.DoesNotExist:
            return JsonResponse({'message': '车辆不存在'}, status=404)
        except Exception as e:
            return JsonResponse({'message': f'预约失败: {str(e)}'}, status=500)
    else:
        return JsonResponse({'message': '错误的请求类型'}, status=405)

@csrf_exempt
def reserveinfo(request):
    """
    查询预约详情接口
    GET 参数:
        userId: 用户ID
        carId: 车辆ID
    返回:
        预约详情或未找到提示
    """
    if request.method == "GET":
        user_id = request.GET.get('userId')
        car_id = request.GET.get('carId')

        if not user_id or not car_id:
            return JsonResponse({'message': '缺少 userId 或 carId'}, status=400)

        try:
            user = User.objects.get(account=user_id)
            car = CarInfo.objects.get(id=car_id)
            reserve = Reserve.objects.filter(user=user, car=car).order_by('-id').first()
            if not reserve:
                return JsonResponse({'message': '未找到预约记录'}, status=404)

            reserve_info = {
                'reserve_id': reserve.id,
                'user': user.account,
                'car': {
                    'id': car.id,
                    'brand': car.brand,
                    'model': car.model,
                    'price': str(car.price),
                    'age': car.age,
                    'image': request.build_absolute_uri(car.image.url) if car.image else None
                },
                'name': reserve.name,
                'phone': reserve.phone,
                'idcard': reserve.idcard,
                'date': str(reserve.date),
                'place': reserve.place,
                'created_at': reserve.created_at.strftime('%Y-%m-%d %H:%M:%S') if hasattr(reserve, 'created_at') else ''
            }
            return JsonResponse({'message': '查询成功', 'reserve_info': reserve_info}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'message': '用户不存在'}, status=404)
        except CarInfo.DoesNotExist:
            return JsonResponse({'message': '车辆不存在'}, status=404)
        except Exception as e:
            return JsonResponse({'message': f'查询失败: {str(e)}'}, status=500)
    else:
        return JsonResponse({'message': '错误的请求类型'}, status=405)

@csrf_exempt
def order(request):
    """
    下单接口
    请求体格式:
    {
        "user_id": "用户ID",
        "car_id": "车辆ID",
        "price": "成交价格",
        "remark": "备注（可选）"
    }
    """
    if request.method == 'get':
        try:
            body = loads(request.body.decode('utf-8'))
            user_id = body.get('user_id')
            car_id = body.get('car_id')
            price = body.get('price')
            remark = body.get('remark', '')

            if not user_id or not car_id or not price:
                return JsonResponse({'message': '缺少必要参数'}, status=400)

            user = User.objects.get(account=user_id)
            car = CarInfo.objects.get(id=car_id)

            # 假设你有一个 Order 模型
            order = Order.objects.create(
                user=user,
                car=car,
                price=price,
                remark=remark
            )

            return JsonResponse({'message': '下单成功', 'order_id': order.id}, status=201)
        except User.DoesNotExist:
            return JsonResponse({'message': '用户不存在'}, status=404)
        except CarInfo.DoesNotExist:
            return JsonResponse({'message': '车辆不存在'}, status=404)
        except Exception as e:
            return JsonResponse({'message': f'下单失败: {str(e)}'}, status=500)
    else:
        return JsonResponse({'message': '错误的请求类型'}, status=405)

