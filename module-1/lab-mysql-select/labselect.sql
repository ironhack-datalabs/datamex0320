#1
use publications;
select a.au_id as "AUTHOR ID", a.au_lname as "LAST NAME", a.au_fname as "FIRST NAME", t.title as "TITLE", p.pub_name as "PUBLISHER"
from authors as a
inner join titleauthor as tauthor
on a.au_id = tauthor.au_id
inner join titles as t
on tauthor.title_id = t.title_id
inner join publishers as p
on t.pub_id = p.pub_id;

#2 #Error code 1055

select a.au_id as "AUTHOR ID", a.au_lname as "LAST NAME", a.au_fname as "FIRST NAME", p.pub_name as "PUBLISHER", count(t.title) as "TITLE"
from authors as a
inner join titleauthor as titlea
on a.au_id = titlea.au_id
inner join titles as t
on titlea.title_id = t.title_id
inner join publishers as p
on t.pub_id = p.pub_id
GROUP BY a.au_id;

#3

select a.au_id as "AUTHOR ID", a.au_lname as "LAST NAME", a.au_fname as "FIRST NAME",SUM(s.qty) as "TOTAL"
from authors as a
inner join titleauthor as ta
on a.au_id = ta.au_id
inner join titles as t
on ta.title_id = t.title_id
inner join sales as s
on t.title_id = s.title_id
group by a.au_id
order by "TOTAL" desc
limit 3;

#4
select a.au_id as "AUTHOR ID", a.au_lname as "LAST NAME", a.au_fname as "FIRST NAME",SUM(s.qty) as "TOTAL"
from authors as a
left join titleauthor as ta
on a.au_id = ta.au_id
left join titles as t
on ta.title_id = t.title_id
left join sales as s
on t.title_id = s.title_id
group by a.au_id
order by "TOTAL" desc;
