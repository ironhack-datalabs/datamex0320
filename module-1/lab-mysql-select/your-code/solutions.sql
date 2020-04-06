#Challenge 1
SELECT  a.au_id as "AUTHOR_ID", 
        u.au_fname as "FIRST_NAME", 
        au.au_lname as "LAST_NAME", 
	t.title as "TITLE", 
	pu.pub_id as "PUBLISHER"
	from authors
		INNER JOIN titleauthor on t.au_id=a.au_id
		INNER JOIN authors on t.tittle_id=au.tittle_id
		INNER JOIN publishers on t.pub_id=pu.pub_id;


#Challenge 2
 SELECT a.au_id as "AUTHOR_ID", 
        u.au_fname as "FIRST_NAME", 
        au.au_lname as "LAST_NAME", 
	pu.pub_name as "PUBLISHER",
	COUNT(t.title) as "TITLE COUNT"
	FROM authors 
		INNER JOIN titleauthor on t.au_id=a.au_id
		INNER JOIN tittles on a.tittle_id=t.au_id
		INNER JOIN publishers on t.pub_id=pu.pub_id
		GROUP BY t.tittle;
#Challenge 3

SELECT a.au_id as AUTHOR_ID", 
        u.au_fname as "FIRST_NAME", 
        au.au_lname as "LAST_NAME", 
	SUM(sales.qty) as "TOTAL"
	FROM authord
		INNER JOIN titleauthor ON ta.au_id=a.au_id
		INNER JOIN titles ON t.title_id=ta.totle_id
		INNER JOIN sales ON s.title_id=t.title_id
	ORDER BY SUM(sales.qty) DESC
	LIMIT 3;

#Challenge 4

SELECT  a.au_id as "AUTHOR_ID", 
        u.au_fname as "FIRST_NAME", 
        au.au_lname as "LAST_NAME",       
        IFNULL(SUM(sales.qty),0)as "TOTAL"
        FROM authors
          LEFT JOIN titleauthor on t.au_id = a.au_id
          LEFT JOIN titles on title.title_id = titleauthor.tittle_id
          LEFT JOIN sales on s.titles_id = t.title_id
		GROUP BY a.au_id;


