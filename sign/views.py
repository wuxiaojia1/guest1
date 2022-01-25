from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from sign.models import Event,Guest
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger



# Create your views here.


def index(request):
    return render(request,'index.html')

#登陆动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username = username,password=password)
        if user is not None:
            #return HttpResponse('login success!')
            auth.login(request,user) #d登陆
            # 将session信息存入到浏览器
            request.session['user'] = username
            response = HttpResponseRedirect('/event_manage/')
            #添加浏览器cookie
            #response.set_cookie('user',username,3600)
            return response
        else:
            return render(request,'index.html',{'error':'username or password error!'})

#发布会管理
@login_required
def  event_manage(request):
    #username = request.COOKIES.get('user', '')  # 读取浏览器cookie
    username = request.session.get('user','')  #读取浏览器session
    event_list = Event.objects.all()
    p = Paginator(event_list,2) #分页器，一页展示2条数据
    page = request.GET.get('page') #根据get请求来的页数，展示第几页
    try:
        contacts = p.page(page)
    except PageNotAnInteger:
        contacts = p.page(1)
    except EmptyPage:
        contacts = p.page(p.num_pages)
    return render(request,'event_manage.html',{"user":username,"events":contacts})


#发布会名称搜索
@login_required
def Event_search_name(request):
    username = request.session.get('user','')
    search_name = request.GET.get('name','')
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request,"event_manage.html",{"user":username,"events":event_list})

#嘉宾名称搜索
@login_required
def Guest_serch_name(request):
    username = request.session.get('user','')
    search_name = request.GET.get('name','')
    guest_list = Guest.objects.filter(realname__contains=search_name)
    return render(request,"guest_manage.html",{"user":username,"guests":guest_list})

@login_required
def guest_manage(request):
    username = request.session.get('user','')
    guest_list = Guest.objects.all()
    p = Paginator(guest_list,2) #分页器，一页2条数据展示
    page = request.GET.get('page')#根据get请求来的页数，展示第几页
    try:
        contacts = p.page(page)
    except PageNotAnInteger:
        # 如果P不是整数，就取第一面数据
        contacts = p.page(2)
    except EmptyPage:
        #如果P不在范围内，就取最后一页
        contacts = p.page(p.num_pages)
    return render(request,"guest_manage.html",{'user':username,'guests':contacts})

#签到会页面
@login_required
def sign_index(request,eid):
    #get_object_or_404 默认调用django的table.object.get()方法，如果查询对象不存在，则会抛出http404异常
   event = get_object_or_404(Event,id=eid)
   event1 = Guest.objects.filter(sign=1).values('sign').count()
   event2 = Guest.objects.all().count()
   return render(request,'sign_index.html',{'event':event,'guests':event1,'guests1':event2})


#签到动作
@login_required
def sign_index_action(request,eid):
    event =get_object_or_404(Event,id=eid)
    event1 = Guest.objects.filter(sign=1).values('sign').count()
    event2 = Guest.objects.all().count()
    phone = request.POST.get('phone','')
    print(phone)
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request,'sign_index.html',{'event':event,'hint':'phone error.','guests':event1,'guests1':event2})

    result = Guest.objects.filter(phone=phone,event_id=eid)
    if not result:
        return render(request,'sign_index.html',{'event':event,'hint':'event id error or phone error','guests':event1,'guests1':event2})

    result = Guest.objects.get(phone=phone,event_id=eid)
    if result.sign:
        return render(request,'sign_index.html',{'event':event,'hint':'user has sgin in','guests':event1,'guests1':event2})
    else:
        Guest.objects.filter(phone=phone,event_id=eid).update(sign='1')
        return render(request,'sign_index.html',{'event':event,'hint':'sign in success','guest':result,'guests':event1,'guests1':event2})







@login_required
def logout(request):
    auth.logout(request) #退出登录
    response = HttpResponseRedirect('/index/')
    return response


def wxj(request):
    event_list = Event.objects.all()
    return HttpResponse(event_list)


if __name__ == "__main__":
    search_name()