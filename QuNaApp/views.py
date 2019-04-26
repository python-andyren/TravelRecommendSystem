import json
import os
import pandas as pd
from django.core.paginator import Paginator
from django.http import HttpResponse
from sklearn.externals import joblib
from QuNaApp.helper import create_model
from QuNaApp.models import Spot, LvyouNote


def get_data(request):
    spots = Spot.objects.all()
    lt = []
    for spot in spots:
        data = {
            'spot_name': spot.spot_name,
            'price': spot.price,
            'hot_rate': spot.hot_rate,
            'address': spot.address,
            'month_sold': spot.month_sold,
            'intro': spot.intro,
            'province': spot.province,
            'spot_type': spot.spot_type,
            'diary_num': spot.diary_num
        }
        lt.append(data)
    jsondata = json.dumps(lt, ensure_ascii=False)
    return HttpResponse(jsondata)


def get_LvyouNote(request, page_num):
    lvyouNotes = LvyouNote.objects.all()
    paginator = Paginator(lvyouNotes, 4)
    page = paginator.page(page_num)
    lt = []
    for message in page.object_list:
        data = {
            'img_url': message.img_url,
            'like': message.like,
            'look_num': message.look_num,
            'title': message.title,
            'note_url': message.note_url,
            'intro': message.intro
        }
        lt.append(data)
    result = {
        'code': '200',
        'msg': 'Success',
        'data': lt
    }
    jsondata = json.dumps(result, ensure_ascii=False)
    return HttpResponse(jsondata)


def do_predict(request):
    print(request)
    if request.method != 'POST':
        data = {
            'code': 403,
            'msg': 'Not Allowed.'
        }
        jsondata = json.dumps(data, ensure_ascii=False)
        return HttpResponse(jsondata)
    if not os.path.exists('../lr.pkl'):
        lr = create_model()
    else:
        lr = joblib.load('../lr.pkl')

    a = request.POST.get('a')
    b = request.POST.get('b')
    c = request.POST.get('c')
    d = request.POST.get('d')

    province = request.POST.get('e')
    province_list = ['河北', '山西', '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东',
                     '海南', '四川',
                     '贵州', '云南', '陕西', '甘肃', '青海', '台湾', '北京', '天津', '上海', '重庆', '广西', '内蒙古', '西藏', '宁夏', '新疆',
                     '香港', '澳门']
    if province not in province_list:
        data = {
            'code': 400,
            'msg': 'There is no city'
        }
        jsondata = json.dumps(data, ensure_ascii=False)
        return HttpResponse(jsondata)

    value = [[a, b, c, d]]
    y = pd.DataFrame(data=value, columns=['price', 'hot_rate', 'month_sold', 'diary_num'])
    result = lr.predict(y)
    spots = Spot.objects.filter(spot_type=result, province=province)
    lt = []

    if len(spots) <= 5:
        for message in spots:
            data = {
                'spot_name': message.spot_name,
                'address': message.address,
                'intro': message.intro,
            }
            lt.append(data)
        result = {
            'code': '200',
            'msg': 'Success',
            'data': lt
        }
        jsondata = json.dumps(result, ensure_ascii=False)
        return HttpResponse(jsondata)
    elif len(spots) == 0:
        data = {
            'code': 400,
            'msg': 'No content.',
            'data': ''
        }
        jsondata = json.dumps(data, ensure_ascii=False)
        return HttpResponse(jsondata)
    else:
        for i in range(5):
            data = {
                'spot_name': spots[i].spot_name,
                'address': spots[i].address,
                'intro': spots[i].intro,
            }
            lt.append(data)
        result = {
            'code': '200',
            'msg': 'Success',
            'data': lt
        }
        jsondata = json.dumps(result, ensure_ascii=False)
        return HttpResponse(jsondata)
