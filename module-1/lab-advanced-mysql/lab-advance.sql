#1
select t.title "TITLE",ta.au_id "AUTHOR_ID", (t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100) as "sales_royalty"
from titles as t
left join titleauthor as ta
on t.title_id = ta.title_id
left join sales as s
on t.title_id = s.title_id

#1.2
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

#1.3

