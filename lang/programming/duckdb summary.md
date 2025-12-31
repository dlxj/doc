



```js
SELECT order_id, order_date, json_extract(customer, '$.name') AS cusName,json_extract(customer, '$.city') AS cusCity FROM read_json_auto('orders.json')
```



```
SELECT sum(od.quantity*od.price) amount
FROM read_json_auto('orders.json') AS o,
LATERAL UNNEST(o.order_details) AS t(od),
LATERAL UNNEST([od.product]) AS t(p)
WHERE p.category = 'Electronics'
```



```

SELECT
    o.order_id, 
    LIST_FILTER(o.order_details, x -> x.product.category = 'Electronics') AS order_details
FROM read_json_auto(orders.json') AS o
WHERE 
    ARRAY_LENGTH(LIST_FILTER(o.order_details, x -> x.product.category = 'Electronics')) > 0
    AND SUM(
        LIST_FILTER(o.order_details, x -> x.product.category = 'Electronics') -> 
            (x -> x.price * x.quantity)
    ) > 200;

```

