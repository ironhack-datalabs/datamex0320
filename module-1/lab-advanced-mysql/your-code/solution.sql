#Challenge 1

SELECT t.title_id, t.price., t.advance, t.royalty, s.qty, a.au_id, a.au_lname, a.au_fname, ta.rolatyper, (t.price*s.qty*t.royalty)
FROM titles t
INNER JOIN sales s on s.title_id=t.title_id
INNER JOIN titleauthor ta on ta.title_id=s.title_id
INNER JOIN authors a on a.au_id=ta.au_id
ORDER BY t.title_id, a.au_id;

SELECT title_id, au_id, au_lname, au_fname, advace, sum(ROYALTIES) a ROYALTIES from( 
	SELECT t.title_ide, t.price, t.advance, t.royalty, s.qty, a.au_id, a.au_lname, a.au_fname, ta.rolatyper, (t.price*s.qty*t.royalty)
	FROM titles t
	INNER JOIN sales s on s.title_id=t.title_id
	INNER JOIN titleauthor ta on ta.title_id=s.title_id
) as tmp
GROUP BY au_id, title_id;


SELECT au_id as "AUTHOR ID", au_lname as "LNAME", au_fname as "FNAME", sum(advance + ROYALTIES) as PROFITS FROM (SELECT title_id, au_id, au_lname, au_fname, sum(ROYALTIES) as ROYALTIES from (
	SELECT t.title_id, t.price, t.advance, t.royalty,s.qty, a.au_id, au_lname, au_fname, ta.rolatyper, (t.price*s.qty*t.royalty)
	FROM title t
	INNER JOIN sales s on s.title_id = t.title_id
	INNER JOIN titleauthor ta on ta-title_id = s.title_id
	INNER JOIN authors a on a.au_id=ta.au_id
) as tmp2
GROUP BY au_id
ORDER BY PROFITS;


#Challenge 2

CREATE temporary TABLE tmp1
SELECT t.title_id, a.au_id, (t.price * s.qty * t.royalty * ta.royaltype / 10000) as scale_royalty
FROM titles t
INNER JOIN sales s on s.title_id=t.title_id
INNER JOIN titleauthor ta on ta.title_id = s.title_id
INNER JPIN authors a on a.au_id = ta.au_id
ORDER BY t.title_id, a.au_id;

CREATE temporary TABLE tmp2
SELEC title_id, au_id, sum(sale_royalty) as ROYALTIES
FROM tmp1
GROUP BY title_id, au_id;

SELECT tmp2.au_id as "AUTHOR ID", a.au_lname as "LNAME", a.au_fname as "FNAME", sum(t.advance + ROYALTIES) as PROFITS
FROM tmp2
INNER JOIN titles t on t.title_id = tmp2.title_id
INNER JOIN authors a on a.au_id = tmp2.au_id
GROUP BY tmp2.au_id
LIMIT 3; 
