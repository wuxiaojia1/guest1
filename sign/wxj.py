from sign.models import Event

event_list = Event.objects.filter(name='新增测试')
print(event_list)