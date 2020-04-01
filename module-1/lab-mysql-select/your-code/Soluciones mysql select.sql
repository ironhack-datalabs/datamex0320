#publications 

#Challenge 1 - Who Have Published What At Where?

use publications;

select a.au_id 'AUTHOR ID', a.au_lname 'LAST NAME', a.au_fname 'FIRST NAME', t.title 'TITLE', p.pub_name 'PUBLISHER'

from authors as a
Inner join titleauthor as ta
on a.au_id = ta.au_id

inner join titles as t
on ta.title_id = t.title_id

inner join publishers as p
on t.pub_id = p.pub_id

#Challenge 2 - Who Have Published How Many At Where?
select
a.au_id 'AUTHOR ID', 
a.au_lname 'LAST NAME', 
a.au_fname 'FIRST NAME', 
p.pub_name 'PUBLISHER', 
COUNT(t.title) 'TITLE'

FROM authors as a
Inner join titleauthor as ta
on a.au_id = ta.au_id

inner join titles as t
on ta.title_id = t.title_id

inner join publishers as p
on t.pub_id = p.pub_id

GROUP BY a.au_id
order by TITLE desc;


#Challenge 3 - Best Selling Authors
select 
a.au_id AS 'AUTHOR ID', 
a.au_lname AS 'LAST NAME', 
a.au_fname AS 'FIRST NAME',
SUM(s.qty) AS 'TITLES SOLD'



FROM authors as a
Inner join titleauthor as ta
on a.au_id = ta.au_id

inner join titles as t
on ta.title_id = t.title_id

inner join sales as s
on t.title_id = s.title_id

group by a.au_id
order by 'TITLES SOLD' desc
limit 3;


#Challenge 4 - Best Selling Authors Ranking
select 
a.au_id AS 'AUTHOR ID', 
a.au_lname AS 'LAST NAME', 
a.au_fname AS 'FIRST NAME',
SUM(s.qty) AS 'TITLES SOLD'



FROM authors as a
left join titleauthor as ta
on a.au_id = ta.au_id

left join titles as t
on ta.title_id = t.title_id

left join sales as s
on t.title_id = s.title_id

group by a.au_id
order by 'TITLES SOLD' desc; 