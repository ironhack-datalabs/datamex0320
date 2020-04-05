{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf610
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Challenge 1\
\
\
select authors.au_id as AUTHOR,\
authors.au_lname as LAST_NAME,\
authors.au_fname as FIRST_NAME,\
titles.title as TITLE,\
publishers.pub_id as PUBLISHERS\
from Authors\
inner join titleauthor on titleauthor.au_id = authors.au_id\
inner join titles on titles.title_id = titleauthor.title_id\
inner join publishers on publishers.pub_id = titles.pub_id\
\
\
Challenge 2\
\
select authors.au_id as AUTHOR,\
authors.au_lname as LAST_NAME,\
authors.au_fname as FIRST_NAME,\
publishers.pub_id as PUBLISHERS,\
COUNT(titles.title) as TITLE_COUNT\
from Authors\
inner join titleauthor on titleauthor.au_id = authors.au_id\
inner join titles on titles.title_id = titleauthor.title_id\
inner join publishers on publishers.pub_id = titles.pub_id\
group by titles.title;\
\
\
\
Challenge 3\
\
\
select authors.au_id as AUTHOR,\
authors.au_lname as LAST_NAME,\
authors.au_fname as FIRST_NAME,\
sum(sales.qty) as TOTAL\
from Authors\
inner join titleauthor on titleauthor.au_id = authors.au_id\
inner join titles on titles.title_id = titleauthor.title_id\
inner join sales on sales.title_id = titles.title_id\
group by authors.au_id\
order by sum(sales.qty) desc\
limit 3;\
\
\
Challenge 4\
\
select authors.au_id as AUTHOR,\
authors.au_lname as LAST_NAME,\
authors.au_fname as FIRST_NAME,\
ifnull(SUM(sales.qty),0) as TOTAL\
from authors\
left join titleauthor on titleauthor.au_id = authors.au_id\
left join titles on titles.title_id = titleauthor.title_id\
left join sales on sales.title_id = titles.title_id\
group by authors.au_id\
order by sum(sales.qty) desc;\
\
\
Bonus\
\
\
select authors.au_id as AUTHOR,\
authors.au_lname as LAST_NAME,\
authors.au_fname as FIRST_NAME,\
((ifnull(titles.price,0) * ifnull(sales.qty,0) * ifnull(titles.royalty,0) * ifnull(titleauthor.royaltyper,0)/10000) + ifnull(titles.advance,0)) as PROFIT\
from authors\
left join titleauthor on titleauthor.au_id = authors.au_id\
left join titles on titles.title_id = titleauthor.title_id\
left join sales on sales.title_id = titles.title_id\
ORDER BY PROFIT\
LIMIT 3;\
\
\
\
}