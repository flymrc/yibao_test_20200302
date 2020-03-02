import celery
from .models import EmployeeUser


@celery.task
def user_added(data):
    obj = EmployeeUser.objects.filter(empno=data['empno'])
    if not obj:
        obj = EmployeeUser(empno=data['empno'], name=data['name'])
        obj.save()
    # print(obj)


@celery.task
def test_delay():
    print('test_delay()')
