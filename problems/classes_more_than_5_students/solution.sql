# Write your MySQL query statement below

Select c.class
from(
  select class, count(class) as num_students
  from Courses
  group by class
  having count(class) >= 5
) c