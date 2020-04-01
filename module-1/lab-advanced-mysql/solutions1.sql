#Step 1: Calculate the royalties of each sales for each author
select titles.title_id, titleauthor.au_id, (titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100) as sales_royalty
from titles
left join titleauthor
on titles.title_id = titleauthor.title_id
left join sales
on titles.title_id = sales.title_id;

#Step 2: Aggregate the total royalties for each title for each author
create temporary table aggregated_royalties
select title_id, au_id, sum(sales_royalty)
from aggregated_royalties
group by title_id;

select title_id, au_id, sum(sales_royalty)
from aggregated_royalties
group by au_id;

#Step 3: Calculate the total profits of each author
select aggregated_royalties.title_id, aggregated_royalties.au_id, advance 
from aggregated_royalties
inner join titles
on aggregated_royalties.title_id=titles.title_id;

create table royalties_advance
select aggregated_royalties.title_id, aggregated_royalties.au_id, sales_royalty, advance 
from aggregated_royalties
inner join titles
on aggregated_royalties.title_id=titles.title_id;

select au_id, sum(sales_royalty+advance) as total_profit
from royalties_advance
group by au_id
order by au_id desc
limit 3;

#Challenge 2 - Alternative Solution
#Challenge 3
CREATE TABLE most_profiting_authors
select au_id, sum(sales_royalty+advance) as total_profit
from royalties_advance
group by au_id;


