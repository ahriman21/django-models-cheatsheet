1-
# see SQL of your query
>>> queryset = Event.objects.all()
>>> str(queryset.query)

2-
# OR query
## first way:
>>> queryset = User.objects.filter(name='ali') | User.objects.filter(family='alavi')
## second way :
>>> queryset = User.objects.filter( Q(name='ali') | Q(family='alavi') )

3-
# AND query
## first way: 
>>>> queryset_1 = User.objects.filter(
first_name__startswith='R',
last_name__startswith='D'
)
## second way :
>>>> queryset_2 = User.objects.filter(first_name__startswith='R') 
                  &
                  User.objects.filter(last_name__startswith='D')
## third way :
>>>> queryset_3 = User.objects.filter(
                  Q(first_name__startswith='R') 
                  &
                  Q(last_name__startswith='D')
)
               
4-
# NOT query
## first way: (exclude)
>>>> queryset = User.objects.exclude(email__contains='admin')
## second way: (~Q)
>>>> queryset = User.objects.filter( ~Q(email__contains='admin') )

5-
# UNION query ( combine two querysets )
>>> q1 = User.objects.filter(email__contains='admin')
>>> q2 = User.objects.filter(email__contains='b')
>>> union = q1.union(q2)
### NOTICE : each UNION query must have the same number of columns ###

6-
# How to select some fields
## first way :
>>>> queryset = User.objects.filter(first_name__startswith='R').values('first_name', 'last_name')
## second way:
>>>> queryset = User.objects.filter(first_name__startswith='R').only("first_name", "last_name")
### The only difference between only and values is only also fetches the id. ###

7-
# finding records that their FileField is empty or null :
>>>> no_files_objects = MyModel.objects.filter( Q(file='') | Q(file=None) )

8-
# We can find Nth records from the query by using slice operator.
## example :How to find second largest record using Django ORM?
>>> user = User.objects.order_by('-last_login')[1] # //Second Highest record w.r.t orderby 'last_login'
>>> user.first_name
'Raghu'
>>> user = User.objects.order_by('-last_login')[2] # // Third Highest record w.r.t orderby 'last_login'
>>> user.first_name
'Sohan'

9-
#  Find rows which have duplicate field values
## example : find records that hava same firstnames or sth
>>>> duplicates = User.objects.values('first_name').annotate(name_count=Count('first_name')).filter(name_count__gt=1)
>>>> print(duplicates)
## ---output---> <QuerySet [{'first_name': 'John', 'name_count': 3}]>

10-
# How to find distinct field values from queryset
## you want to find users whose names have not been repeated. You can do this like this
distinct = User.objects.values(
'first_name'
).annotate(
name_count=Count('first_name')
).filter(name_count=1)
records = User.objects.filter(first_name__in=[item['first_name'] for item in
˓→distinct])

11-
# get a random record from a table :

def get_random():
return Category.objects.order_by("?").first()


12-
# how to create multiple objects in one shot?

>>> Category.objects.bulk_create(
[Category(name="God"),
Category(name="Demi God"),
Category(name="Mortal")]






