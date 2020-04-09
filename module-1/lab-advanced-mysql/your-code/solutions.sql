# Challenge 1 - Most Profiting Authors


# Step 1: Calculate the royalties of each sales for each author
create table sales_royalties
select 
	a.au_id as AUTHOR_ID,
	t.title_id as TITLE_ID,
	ts.price * sales.qty * ts.royalty / 100 * t.royaltyper / 100 as ROYALTIES
from 
    authors a
inner join titleauthor t on
	(a.au_id = t.au_id)
inner join titles ts on 
	(t.title_id = ts.title_id)
inner join sales on
	(sales.title_id = ts.title_id)
;


# Step 2: Aggregate the total royalties for each title for each author

SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
create table total_royalties
select 
	sr.AUTHOR_ID,
	sr.TITLE_ID,
	sum(sr.ROYALTIES) as TOTAL_ROYALTIES	
from 
    sales_royalties sr
group by
	sr.AUTHOR_ID, sr.TITLE_ID
;


# Step 3: Calculate the total profits of each author

select
	tr.AUTHOR_ID,
    ts.advance * t.royaltyper/100 + tr.TOTAL_ROYALTIES as PROFITS
from
	total_royalties tr
inner join titleauthor t on
	tr.TITLE_ID = t.title_id
inner join titles ts on
	ts.title_id = tr.TITLE_ID
order by
	PROFITS
desc limit 3
;



# Challenge 2 - Alternative Solution

select
	au_id as AUTHOR_ID,
    advance + sum(ROYALTIES) as PROFITS
from
(
	select 
	a.au_id,
	t.title_id as TITLE_ID,
	ts.price * sales.qty * ts.royalty / 100 * t.royaltyper / 100 as ROYALTIES,
	ts.advance * t.royaltyper/100 as advance
	from 
	authors a
	inner join titleauthor t on
	(a.au_id = t.au_id)
	inner join titles ts on 
	(t.title_id = ts.title_id)
	inner join sales on
	(sales.title_id = ts.title_id)
    )
as royalties
group by 
	AUTHOR_ID, TITLE_ID, advance
order by
	PROFITS
desc limit 3
;



# Challenge 3
 
create temporary table mos_profiting_authors
select
	au_id as AUTHOR_ID,
    advance + sum(ROYALTIES) as PROFITS
from
(
	select 
	a.au_id,
	t.title_id as TITLE_ID,
	ts.price * sales.qty * ts.royalty / 100 * t.royaltyper / 100 as ROYALTIES,
	ts.advance * t.royaltyper/100 as advance
	from 
	authors a
	inner join titleauthor t on
	(a.au_id = t.au_id)
	inner join titles ts on 
	(t.title_id = ts.title_id)
	inner join sales on
	(sales.title_id = ts.title_id)
    )
as royalties
group by 
	AUTHOR_ID, TITLE_ID, advance
order by
	PROFITS
desc limit 3
;
