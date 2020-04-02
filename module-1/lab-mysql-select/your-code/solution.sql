
#Antes de iniciar, para evitar que marque error 
SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));


#CHALLENGE 1 
#Crear un join de acuerdo a los parámetros de título y ID del autor
select a.au_id,au_lname,au_fname,t.au_id,tl.title
	from authors a
	inner join titleauthor t on 
	a.au_id=t.au_id
	inner join titles tl on 
	tl.title_id=t.title_id

#Crear un join de acuerdo a los parámetros de título, ID del autor y ID de publicación

select a.au_id,au_lname,au_fname,t.au_id,tl.title, p.pub_id
	from authors a
	inner join titleauthor t on 
	a.au_id=t.au_id
	inner join titles tl on 
	tl.title_id=t.title_id
	inner join publishers p on 
	p.pub_id=tl.pub_id


#Challenge 2
select authors.au_id as "autor", authors.au_lname as "last name", authors.au_fname as "first name",
       publishers.pub_id as "publishers", count(titles.title) as "title count"
       from authors 
       inner join titleauthor on titleauthor.au_id=authors.au_id
       inner join titles on titles.title_id=titleauthor.title_id
       inner join publishers on publishers.pub_id=titles.pub_id
       
       group by titles.title;


#Challenge 3
select authors.au_id as "author", authors.au_lname as "last name", authors.au_fname as "first name",
       sum(sales.qty) as "total"
       from authors 
       inner join titleauthor on titleauthor.au_id=authors.au_id
       inner join titles on titles.title_id=titleauthor.title_id
       inner join sales on sales.title_id=titles.title_id
	group by authors.au_id
        order by sum(sales.qty) desc
        limit 3;

#Challenge 4
select a.au_id as "author", a.au_lname as "last name",a.au_fname as "first name",
       ifnull(sum(sales.qty),0) as "total"
       from authors a
       left join titleauthor on titleauthor.au_id=a.au_id
       left join titles on titles.title_id=titleauthor.title_id
       left join sales on sales.title_id=titles.title_id
       group by a.au_id
       order by sum(sales.qty) desc
       

