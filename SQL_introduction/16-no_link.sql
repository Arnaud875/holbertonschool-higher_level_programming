-- 16. lists all records of the table

select score, name
from second_table
where name != ""
order by score desc;
