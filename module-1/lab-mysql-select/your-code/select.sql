#CHALLENGE 1
select  a.au_id as AUTHOR_ID, au.au_fname as FIRST_NAME, au.au_lname as LAST_NAME, t.title as TITLE, t.title_id as TITLE_ID, pu.pub_name as PUBLISHER
from titles as t
RIGHT join titleauthor as a
on t.title_id=a.title_id
INNER join authors as au
on a.au_id=au.au_id
left join publishers as pu
on t.pub_id=pu.pub_id;
#CHALLENGE 2
select  a.au_id as AUTHOR_ID, au.au_fname as FIRST_NAME, 
au.au_lname as LAST_NAME, t.title as TITLE, t.title_id as TITLE_ID, 
pu.pub_name as PUBLISHER,
count(pu.pub_name) as TITLE_COUNT  
from titles as t
left join titleauthor as a
on t.title_id=a.title_id
left join authors as au
on a.au_id=au.au_id
left join publishers as pu
on t.pub_id=pu.pub_id
GROUP BY a.au_id;
#CHALLENGE 3
select a.au_id as AUTHOR_ID, au.au_fname as FIRST_NAME, au.au_lname 
as LAST_NAME, sum(sa.qty) as CANTIDAD
from titles as t
INNER join titleauthor as a
on t.title_id=a.title_id
INNER join authors as au
on a.au_id=au.au_id
INNER join sales as sa
on a.title_id = sa.title_id
group by AUTHOR_ID
order by CANTIDAD desc limit 3;
#CHALLENGE 4
select a.au_id as AUTHOR_ID, au.au_fname as FIRST_NAME, au.au_lname 
as LAST_NAME, sum(sa.qty) as CANTIDAD
from titles as t
INNER join titleauthor as a
on t.title_id=a.title_id
INNER join authors as au
on a.au_id=au.au_id
INNER join sales as sa
on a.title_id = sa.title_id
group by AUTHOR_ID
order by CANTIDAD desc;