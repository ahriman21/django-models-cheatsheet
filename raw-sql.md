## raw sql in django
you can write raw sql qureies in django using django orm. for example :
```
products = Product.objects.raw('SELECT * FROM products WHERE price > 20000')
```
>  django doesnot check wheter your query is correct or not, so you might get unpredictable  errors

* you can pass parameter to your queries. to do that you can put a `%s` in the sql and in second parameter you can pass your data as a list:
```
products = Product.objects.raw('SELECT * FROM products WHERE price > %s', [price])
```


