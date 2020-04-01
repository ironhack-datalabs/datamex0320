#Challenge 1 - Most Profiting Authors

#STEP 1
select 
t.title 'TITLE',
ta.au_id 'AUTHOR ID', 
(t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100) as 'sales_royalty'

from titles as t
left join titleauthor as ta
on t.title_id = ta.title_id

left join sales as s
on t.title_id = s.title_id

#STEP 2
SELECT
t2.au_id 'AUTHOR ID',
t2.title_id 'TITLE ID', 
SUM(sales_royalty) as royalties

from 
(select 
t.title 'TITLE',
ta.au_id author_id, 
(t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100) as 'sales_royalty'

from titles as t
left join titleauthor as ta
on t.title_id = ta.title_id

left join sales as s
on t.title_id = s.title_id) AS roya

left join titleauthor as t2
on roya.author_id = t2.au_id

group by t2.au_id, t2.title_id

#STEP 3
select 
ta3.au_id ,
SUM(royalties) as finalprof


from 
(SELECT
t2.au_id author_id5,
t2.title_id 'TITLE ID', 
SUM(sales_royalty) as royalties

from 
(select 
t.title 'TITLE',
ta.au_id author_id, 
(t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100) as 'sales_royalty'

from titles as t
left join titleauthor as ta
on t.title_id = ta.title_id

left join sales as s
on t.title_id = s.title_id) AS roya

left join titleauthor as t2
on roya.author_id = t2.au_id

group by t2.au_id, t2.title_id) as profits

left join titleauthor as ta3
on profits.author_id5 = ta3.au_id

group by ta3.au_id
order by finalprof desc;


#Challenge 2
create temporary table publications.salesroyalty
select 
t.title 'TITLE',
ta.au_id 'AUTHOR ID', 
(t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100) as 'sales_royalty'

from titles as t
left join titleauthor as ta
on t.title_id = ta.title_id

left join sales as s
on t.title_id = s.title_id
;


create temporary table publications.salesprof
SELECT
t2.au_id author_id5,
t2.title_id 'TITLE ID', 
SUM(sales_royalty) as royalties

from 
(select 
t.title 'TITLE',
ta.au_id author_id, 
(t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100) as 'sales_royalty'

from titles as t
left join titleauthor as ta
on t.title_id = ta.title_id

left join sales as s
on t.title_id = s.title_id) AS roya

left join titleauthor as t2
on roya.author_id = t2.au_id

group by t2.au_id, t2.title_id


FINAL QUERY
select 
ta3.au_id ,
SUM(royalties) as finalprof

from 
publications.salesprof

left join titleauthor as ta3
on profits.author_id5 = ta3.au_id

group by ta3.au_id
order by finalprof desc;



#CHALLENGE 3
CREATE TABLE most_profiting_authors AS
select 
ta3.au_id ,
SUM(royalties) as finalprof


from 
(SELECT
t2.au_id author_id5,
t2.title_id 'TITLE ID', 
SUM(sales_royalty) as royalties

from 
(select 
t.title 'TITLE',
ta.au_id author_id, 
(t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100) as 'sales_royalty'

from titles as t
left join titleauthor as ta
on t.title_id = ta.title_id

left join sales as s
on t.title_id = s.title_id) AS roya

left join titleauthor as t2
on roya.author_id = t2.au_id

group by t2.au_id, t2.title_id) as profits

left join titleauthor as ta3
on profits.author_id5 = ta3.au_id

group by ta3.au_id
order by finalprof desc;

