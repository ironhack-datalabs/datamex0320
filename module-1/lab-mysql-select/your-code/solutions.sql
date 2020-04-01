
# Challenge 1 - Who Have Published What At Where?

select authors.au_id AS 'Author ID', authors.au_lname as 'Last Name', authors.au_fname as 'First Name', titles.title as Title,
publishers.pub_name as Publisher 
from authors
inner join titleauthor
on authors.au_id = titleauthor.au_id
inner join titles
on titleauthor.title_id=titles.title_id
inner join publishers
on titles.pub_id=publishers.pub_id
order by au_lname;


# Challenge 2 - Who Have Published How Many At Where?
# This code doesn't work on my computer but I replicated using other student pc.

CREATE TEMPORARY TABLE challenge1
select authors.au_id, authors.au_lname, authors.au_fname, titles.title as Title,
publishers.pub_name as Publisher 
from authors
inner join titleauthor
on authors.au_id = titleauthor.au_id
inner join titles
on titleauthor.title_id=titles.title_id
inner join publishers
on titles.pub_id=publishers.pub_id
order by au_lname;

select au_id, au_lname as last_name , au_fname as first_name,
pub_name, count(pub_name) as title_count 
from challenge1
group by au_id;

# Challenge 3 - Best Selling Authors
select authors.au_id, authors.au_fname, authors.au_lname, sum(titles.price * ytd_sales) as Total
from authors
left join titleauthor
on authors.au_id = titleauthor.au_id
left join titles
on titleauthor.title_id=titles.title_id
group by titles.ytd_sales
order by authors.au_id
Limit = 

#Challenge 4 - Best Selling Authors Ranking
.


