#STEP 1 ROYALTY
select t.title_id 'Title ID',
ta.au_id 'Author ID',
(t.price*sa.qty*t.royalty / 100*ta.royaltyper / 100) 'Royalti'
from publications.titles as t
right join publications.titleauthor as ta
on  t.title_id = ta.title_id
right join publications.sales as sa
on ta.title_id = sa.title_id ;

#STEP 2 PROFITS
select ta2.title_id 'Title ID', 
ta2.au_id 'Author ID', 
sum(royalti) 'Total Royalties'
from 
(select t.title 'Title_ID',
ta.au_id 'Author_ID',
(t.price*sa.qty*t.royalty / 100*ta.royaltyper / 100) 'royalti'
from publications.titles as t
right join publications.titleauthor as ta
on  t.title_id = ta.title_id
right join publications.sales as sa
on ta.title_id = sa.title_id ) as r2
left join publications.titleauthor as ta2
on r2.Author_ID = ta2.au_id
group by ta2.au_id, ta2.title_id ;

#STEP 3 TOTAL PROFITS
select ta3.au_id Author_ID, sum(Total_Royalties) Profits
from 
(select ta2.title_id 'Title ID', 
ta2.au_id Author_ID2, 
sum(royalti) 'Total_Royalties'
from 
(select t.title 'Title_ID',
ta.au_id 'Author_ID',
(t.price*sa.qty*t.royalty / 100*ta.royaltyper / 100) 'royalti'
from publications.titles as t
right join publications.titleauthor as ta
on  t.title_id = ta.title_id
right join publications.sales as sa
on ta.title_id = sa.title_id ) as r2
left join publications.titleauthor as ta2
on r2.Author_ID = ta2.au_id
group by ta2.au_id, ta2.title_id ) as TR 
left join publications.titleauthor as ta3
on TR.Author_ID2 = ta3.au_id
group by ta3.au_id
order by profits desc ;

#CHALLENGE 2 ALTERNATIVE SOLUTION
create temporary table step1_royalty
select t.title_id 'Title ID',
ta.au_id 'Author ID',
(t.price*sa.qty*t.royalty / 100*ta.royaltyper / 100) 'Royalti'
from publications.titles as t
right join publications.titleauthor as ta
on  t.title_id = ta.title_id
right join publications.sales as sa
on ta.title_id = sa.title_id ;

create temporary table step2_profits2
select ta2.title_id 'Title ID', 
ta2.au_id 'Author_ID2', 
sum(royalti) 'Total_Royalties'
from 
(select t.title 'Title_ID',
ta.au_id 'Author_ID',
(t.price*sa.qty*t.royalty / 100*ta.royaltyper / 100) 'royalti'
from publications.titles as t
right join publications.titleauthor as ta
on  t.title_id = ta.title_id
right join publications.sales as sa
on ta.title_id = sa.title_id ) as r2
left join publications.titleauthor as ta2
on r2.Author_ID = ta2.au_id
group by ta2.au_id, ta2.title_id ;

select ta3.au_id Author_ID, 
sum(Total_Royalties) Profits
from step2_profits2 as TR 
left join publications.titleauthor as ta3
on TR.Author_ID2 = ta3.au_id
group by ta3.au_id
order by profits desc ;

#CHALLENGE 3
create table most_profiting_authors
select ta3.au_id au_id, 
sum(Total_Royalties) profits
from step2_profits2 as TR 
left join publications.titleauthor as ta3
on TR.Author_ID2 = ta3.au_id
group by ta3.au_id
order by profits desc;

select * from most_profiting_authors;
