# Write your MySQL query statement below

select a.customer_number
from(
  select customer_number, count(customer_number) as order_count
  from Orders
  group by customer_number
  order by order_count desc
  limit 1) a
