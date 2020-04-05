{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf610
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Challenge 1\
\
1.1\
\
select titles.title_id, titles.price,titles.advance, titles.royalty, sales.qty, authors.au_id, authors.au_lname, authors.au_fname, titleauthor.royaltyper, (titles.price * sales.qty * titles.royalty * titleauthor.royaltyper / 10000) as ROYALTIES\
FROM titles\
inner join sales on sales.title_id = titles.title_id\
inner join titleauthor on titleauthor.title_id = sales.title_id\
inner join authors on authors.au_id = titleauthor.au_id\
order by titles.title_id, authors.au_id;\
\
\
\
1.2\
\
\
select title_id, au_id, au_lname, au_fname, advance, sum(royalties) as royalties from(\
	select titles.title_id, titles.price,titles.advance, titles.royalty, sales.qty, authors.au_id, authors.au_lname, authors.au_fname, titleauthor.royaltyper, (titles.price * sales.qty * titles.royalty * titleauthor.royaltyper / 10000) as ROYALTIES\
	FROM titles\
	inner join sales on sales.title_id = titles.title_id\
	inner join titleauthor on titleauthor.title_id = sales.title_id\
	inner join authors on authors.au_id = titleauthor.au_id\
) as temporal\
group by au_id, title_id;\
\
\
\
1.3\
\
\
select au_id as Author_id, au_lname as Last_name, au_fname as First_name, sum(advance + royalties) as Profits from(\
	select title_id, au_id, au_lname, au_fname, advance, sum(royalties) as royalties from(\
		select titles.title_id, titles.price,titles.advance, titles.royalty, sales.qty, authors.au_id, authors.au_lname, authors.au_fname, titleauthor.royaltyper, (titles.price * sales.qty * titles.royalty * titleauthor.royaltyper / 10000) as ROYALTIES\
		FROM titles\
		inner join sales on sales.title_id = titles.title_id\
		inner join titleauthor on titleauthor.title_id = sales.title_id\
		inner join authors on authors.au_id = titleauthor.au_id\
	) as temporal\
	group by au_id, title_id\
) as temporal2\
GROUP BY au_id\
order by profits desc\
limit 3;\
\
\
\
Challenge 2\
\
Step 1\
\
Create TEMPORARY TABLE tmp1\
select titles.title_id, authors.au_id, (titles.price * sales.qty * titles.royalty * titleauthor.royaltyper / 10000) as ventas\
from titles\
inner join sales on sales.title_id = titles.title_id\
inner join titleauthor on titleauthor.title_id = sales.title_id\
inner join authors on authors.au_id = titleauthor.au_id\
order by titles.title_id, authors.au_id;\
\
\
Step 2\
\
Create temporary table tmp2\
select title_id, au_id, sum(ventas) as royalties\
from tmp1\
group by title_id, au_id;\
\
\
Step 3\
\
select tmp2.au_id as Autho_id, authors.au_lname as Last_name, authors.au_fname as First_name, sum(titles.advance + royalties) as PROFITS\
FROM tmp2\
inner join titles on titles.title_id = tmp2.title_id\
inner join authors on authors.au_id = tmp2.au_id\
group by tmp2.au_id\
order by profits desc\
limit 3;\
\
}