Esdras
#Challenge 1 - Who Have Published What At Where?
select 
    authors.au_id AS 'Author_ID', 
    authors.au_lname as 'Last_Name', 
    authors.au_fname as 'First_Name', 
    titles.title as Title,
    publishers.pub_name as Publisher 
from authors
	inner join titleauthor on authors.au_id = titleauthor.au_id
	inner join titles on titleauthor.title_id=titles.title_id
	inner join publishers on titles.pub_id=publishers.pub_id
order by au_lname;


#Challenge 2 - Who Have Published How Many At Where?
CREATE TEMPORARY TABLE challenge1
select 
	authors.au_id, 
	authors.au_lname, 
        authors.au_fname, 
        titles.title,
	publishers.pub_name 
from authors
inner join titleauthor on authors.au_id = titleauthor.au_id
inner join titles on titleauthor.title_id=titles.title_id
inner join publishers on titles.pub_id=publishers.pub_id
order by au_lname;


select au_id, au_lname as Last_name , au_fname as First_name,
pub_name as Pub_name, count(pub_name) as Title_count 
from challenge1
group by au_id;

#Challenge 3 - Best Selling Authors
select 
	a.au_id, 
	au_lname, 
        au_fname, 
        ti.title_id, 
        sum(qty) as totalqty 
from authors as a
inner join titleauthor as t on a.au_id=t.au_id
inner join titles as ti on t.title_id=ti.title_id
inner join sales as s on ti.title_id=s.title_id
group by au_id
order by totalqty desc
limit 3;

#Challenge 4 - Best Selling Authors Ranking
select 
    a.au_id, 
    au_lname, 
    au_fname, 
    ti.title_id, 
    sum(qty) as totalqty 
from authors as a
left join titleauthor as t on a.au_id=t.au_id
left join titles as ti on t.title_id=ti.title_id
left join sales as s on ti.title_id=s.title_id
group by au_id
order by totalqty desc;