from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import json
from redis import Redis
from .models import Player
# Create your views here.
from django.views import View

class Get_makr(View):
    def get(self,request,pk,start=None,end=None):
        pk = str(pk)
        user = Player.objects.filter(player__contains=pk).first()
        redis = Redis(host="127.0.0.1", port=6379, db=1)
        res = redis.zrevrange("set",0,-1)
        user_rank = redis.zrevrank('set',user.id)
        if start!=None and end !=None:
            low = int(start)
            high = int(end)
            if low > len(res) or high> len(res):
                return HttpResponse("超出了玩家排名范围")
            res = res[low-1:high]  # [列表中都是id]
        id_lst = [int(i) for i in res ] # [按照分数从高到低的玩家id]
        data = []
        for id in id_lst:
            obj =Player.objects.get(id=id)
            rank = redis.zrevrank("set",obj.id)
            data.append(
                {
                    "rank":rank+1,
                    "player":obj.player,
                    "makr":obj.makr
                }
            )
        data.append({"rank":user_rank+1,"player":user.player,"makr":user.makr})
        return render(request,"result.html",{"data":data})
class Create_makr(View):
    def post(self,request):
        encode_data = request.body
        data = encode_data.decode()
        data = json.loads(data)
        player = data.get('player')
        makr = data.get('makr')  ####记得修改类名大写
        if makr < 1 or makr > 10000000 or type(makr)!=int:
            return HttpResponse("输入的分数不在范围内")
        check = Player.objects.filter(player=player).first()
        if check:
            check.makr = makr
            check.save()
            id = check.id
            redis = Redis(host="127.0.0.1",port=6379,db=1)
            res = redis.zadd("set",{id:makr})

        else:
            a = Player.objects.create(
                player = player,
                makr = makr
            )
            id = a.id
            makr = a.makr
            redis = Redis(host="127.0.0.1",port=6379,db=1)
            res = redis.zadd("set",{id:makr})
            print(res)
        return JsonResponse('分数上传成功',safe=False)