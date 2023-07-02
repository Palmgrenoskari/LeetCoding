# Write your MySQL query statement below
select sub.name, sub.balance
from (
  select u.name as name, sum(t.amount) as balance
  from Users u join Transactions t ON u.account = t.account
  group by t.account
) as sub
where balance > 10000