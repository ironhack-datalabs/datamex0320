Challenge 1 - Most Profiting Authors
Step 1: Calculate the royalties of each sales for each author

select t.title "TITLE",ta.au_id "AUTHOR_ID", (t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100) as "sales_royalty"
from titles as t
left join titleauthor as ta
on t.title_id = ta.title_id
left join sales as s
on t.title_id = s.title_id

Step 2: Aggregate the total royalties for each title for each author
select tauthor.au_id "AUTHOR ID",tauthor.title_id "TITLE ID", SUM(sales_royalty) as ROYALTIES

from (select t.title 'TITLE',ta.au_id author_id, (t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100) as 'sales_royalty'
from titles as t
left join titleauthor as ta
on t.title_id = ta.title_id
left join sales as s
on t.title_id = s.title_id) AS r
left join titleauthor as tauthor
on r.author_id = tauthor.au_id
group by tauthor.au_id, tauthor.title_id;

Step 3: Calculate the total profits of each author
select ta3.au_id ,SUM(royalties) as PROFIT
from 
(select t2.au_id author_id5,t2.title_id "TITTLE ID", SUM(sales_royalty) as royalties
from 
(select t.title "TITLE",ta.au_id author_id, (t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100) as "sales_royalty"
from titles as t
left join titleauthor as ta
on t.title_id = ta.title_id
left join sales as s
on t.title_id = s.title_id) as royal
left join titleauthor as t2
on royal.author_id = t2.au_id
group by t2.au_id, t2.title_id) as profits
left join titleauthor as ta3
on profits.author_id5 = ta3.au_id
group by ta3.au_id
order by PROFIT desc;

Challenge 2 - Alternative Solution
create temporary table publications.salesroyalty
select t.title ,ta.au_id "AUTHOR ID", (t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100) as "sales_royalty"
from titles as t
left join titleauthor as ta
on t.title_id = ta.title_id
left join sales as s
on t.title_id = s.title_id;

create temporary table publications.salesprofit
SELECT t2.au_id author_id5,t2.title_id "TITLE ID", SUM(sales_royalty) as royalties
from 
(select t.title "TITLE ID",
ta.au_id author_id, 
(t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100) as "sales_royalty"
from titles as t
left join titleauthor as ta
on t.title_id = ta.title_id
left join sales as s
on t.title_id = s.title_id) AS roya
left join titleauthor as t2
on roya.author_id = t2.au_id
group by t2.au_id, t2.title_id

Challenge 3
create table most_profiting_authors 
select ta3.au_id ,SUM(royalties) as finalprofit
from 
(select t2.au_id author_id5,t2.title_id "TITLE ID", SUM(sales_royalty) as royalties
from 
(select t.title "TITLE",ta.au_id author_id, (t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100) as "sales_royalty"
from titles as t
left join titleauthor as ta
on t.title_id = ta.title_id
left join sales as s
on t.title_id = s.title_id) as royal
left join titleauthor as t2
on royal.author_id = t2.au_id
group by t2.au_id, t2.title_id) as profit
left join titleauthor as ta3
on profit.author_id5 = ta3.au_id
group by ta3.au_id
order by finalprofit desc;
