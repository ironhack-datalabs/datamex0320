#Challenge 1 - Who Have Published What At Where?
SELECT authors.au_id, au_lname,
au_fname,titles.title, publishers.pub_name from authors
INNER join titleauthor
on authors.au_id=titleauthor.au_id
INNER join titles
on titleauthor.title_id=titles.title_id
INNER join publishers
on titles.pub_id=publishers.pub_id
order by au_lname;

#Challenge 2 - Who Have Published How Many At Where?
CREATE TEMPORARY TABLE temp
SELECT authors.au_id, au_lname,
au_fname,titles.title, publishers.pub_name from authors
INNER join titleauthor
on authors.au_id=titleauthor.au_id
INNER join titles
on titleauthor.title_id=titles.title_id
INNER join publishers
on titles.pub_id=publishers.pub_id
order by au_lname;

select au_id, au_lname as last_name , au_fname as first_name,
pub_name, count(pub_name) as title_count from temp
group by au_id;

#Challenge 3 - Best Selling Authors

select a.au_id, au_lname, au_fname, ti.title_id, sum(qty) as totalqty 
from authors as a
inner join titleauthor as t
on a.au_id=t.au_id
inner join titles as ti
on t.title_id=ti.title_id
inner join sales as s
on ti.title_id=s.title_id
group by au_id
order by totalqty desc
limit 3;

#Challenge 4 - Best Selling Authors Ranking
select a.au_id, au_lname, au_fname, ti.title_id, sum(qty) as totalqty 
from authors as a
left join titleauthor as t
on a.au_id=t.au_id
left join titles as ti
on t.title_id=ti.title_id
left join sales as s
on ti.title_id=s.title_id
group by au_id
order by totalqty desc;
