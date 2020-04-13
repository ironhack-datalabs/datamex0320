![](arxiv_quant-ph.png)

------

# The most recent 50,000 papers on Quantum Mechanics from ArXiv

This project aims to collect scientific literature store at ArXiv under the category tag quant-ph (Quantum Mechanics). The data base built here will help us to analyze where the field is going and to identify what makes a relevant publication impactful.  

------

# Motivation

This database will allow us to perform an analysis on how publications on quantum mechanics and related fields have evolved, are evolving as well as to identify good and bad practices. Some of questions we would like to address include, but are not limited to:

 1. What makes a publication a relevant or irrelevant one? 

    ​	Here we would like to know the most influential factors that determine whether a publication will be read or not. 

	2. Can we identify where the field is moving to? Which topics were relevant five years ago and are still relevant or which ones went to obscurity?

The analysis is of course devised for publications whose aim is to provide specific insight on a particular topic and not for scientific breakthroughs since such cases are determined by human consensus.   

------

# Contributions

This dataset is inspired by the Kaggle's dataset: 

[Quantum]: https://www.kaggle.com/louise2001/quantum-physics-articles-on-arxiv-2010-to-2020	"Quantum Physics articles on Arxiv 2010 to 2020"

by  **Loulou**. My version of the dataset aims to include more numerical features like:

	1. Number of authors.
 	2. Number of pages.
 	3. Number of figures.
 	4. Number of citations. 
 	5. As well as numerical features derived from Title, Abstract and the text itself. 

This Version 1 of the dataset so it currently includes points from 1 to 3 of the previous list. 

------

# Features

Below is the list of prospectives aspects to be added:

## Code

- [ ] Functions to generate and clean batches of bs4 objects.
- [ ] Functions to clean the data frame.
- [ ] Perform web scraping to retrieve citations for each article.
- [ ] Find an efficient way to retrieve the citation record for each paper.
- [ ] Compact the code in a utils.py file.
- [ ] Transform the code from a function-based to a class-based implementation.

## Dataset Columns

- [x] Title
- [x] Publication Date
- [x] Summary (Abstract)
- [x] Number of Authors
- [x] Categories
- [x] Number of pages
- [x] Number of Figures
- [ ] Citations
- [ ] Citation Record
- [ ] Title Length
- [ ] Abstract Length
