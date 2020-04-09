# Challenge 1 - Who Have Published What At Where?
select 
	a.au_id as AUTHOR_ID,
	a.au_lname as LAST_NAME, 
    a.au_fname as FIRST_NAME,
    s.title as TITLE,
    p.pub_name as PUBLISHER
from 
    authors a
inner join titleauthor t 
on
	(a.au_id = t.au_id)
inner join titles s
on 
	(t.title_id = s.title_id)
inner join publishers p 
on
	(s.pub_id= p.pub_id)
;



#Challenge 2 - Who Have Published How Many At Where?

SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
select 
	a.au_id as AUTHOR_ID,
	a.au_lname as LAST_NAME, 
    a.au_fname as FIRST_NAME,
    s.title as TITLE,
    p.pub_name as PUBLISHER,
	count(s.title) as TITLE_COUNT
from 
    authors a
inner join titleauthor t on
	(a.au_id = t.au_id)
inner join titles s on 
	(t.title_id = s.title_id)
inner join publishers p on
	(s.pub_id= p.pub_id)
group by s.title
order by count(s.title) desc
;



# Challenge 3 - Best Selling Authors

SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
select 
	a.au_id as AUTHOR_ID,
	a.au_lname as LAST_NAME, 
    a.au_fname as FIRST_NAME,
	sum(sales.qty * ts.price) as TOTAL
from 
    authors a
inner join titleauthor t on
	(a.au_id = t.au_id)
inner join titles ts on 
	(t.title_id = ts.title_id)
inner join sales on
	sales.title_id = ts.title_id
group by sales.title_id
order by TOTAL desc
lmimit 3
;


# Challenge 4 - Best Selling Authors Ranking

SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
select 
	a.au_id as AUTHOR_ID,
	a.au_lname as LAST_NAME, 
    a.au_fname as FIRST_NAME,
	coalesce(sum(sales.qty * ts.price), 0.0) as TOTAL
from 
    authors a
left join titleauthor t on
	(a.au_id = t.au_id)
left join titles ts on 
	(t.title_id = ts.title_id)
left join sales on
	sales.title_id = ts.title_id
group by a.au_id
order by TOTAL desc
;


# Bonus Challenge - Most Profiting Authors

SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
select 
	a.au_id as AUTHOR_ID,
	a.au_lname as LAST_NAME, 
    a.au_fname as FIRST_NAME,
	t.royaltyper*(ts.advance + ts.royalty*ts.ytd_sales*ts.price) as PROFIT
from 
    authors a
left join titleauthor t on
	(a.au_id = t.au_id)
left join titles ts on 
	(t.title_id = ts.title_id)
left join sales on
	sales.title_id = ts.title_id
group by a.au_id
order by PROFIT desc
limit 3
;