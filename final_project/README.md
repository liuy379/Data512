## Data 512 Final Project
### Project Proposal
#### Motivation and Problem Statement
When we are unsure about movie or TV show to watch and there is no any other source of recommendation, reviews are helpful for us to make decisions. However, reviews may inevitably contain spoilers which are not desirable for most people. As a movie lover, even I am fully aware of the risk of spoilers while reading reviews and always being extra careful, I still get spoiled a lot because it is hard to see what’s coming while reading a review. So I am interested in learning about the approaches review websites take to handle potential spoiling comments, the characteristics of spoiling comments (which genre has the highest percentage of spoiling comments, movies in which language or region are more likely to have spoiling comments, and how are spoilers change over time etc), and build a spoiler identifier as I’ve always wanted to practice on NLP techniques. The direct results of this project might be interesting to both owners and users of movie/TV show review website, and the methodology I am planning to use might also be interesting to people who work on text similarity analysis.

#### Data
- Kaggle: https://www.kaggle.com/rmisra/imdb-spoiler-dataset#IMDB_reviews.json
- Author of the Kaggle Dataset: https://rishabhmisra.github.io/publications/
- IMDb: https://www.imdb.com/interfaces/

The Kaggle dataset is collected by Rishabh Misra from IMDb. The dataset consists of two sub datasets (movie_details and reviews) in json format. The movie_details dataset contains metadata such as movie id, plot synopsis, genre, duration, rating, and release date. The reviews dataset includes columns such as movie id, user id, indicator of spoiler, review text, and rating. Rishabh did not include other metadata such as region, language, and crews when he formed the dataset but the information is available on the IMDb website. The Kaggle dataset is licensed as CC so it is in public domain and can be used with citation to Rishabh. License/term of use of the IMDb can be found [here](https://help.imdb.com/article/imdb/general-information/can-i-use-imdb-data-in-my-software/G5JTRESSHJBBHTGX?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3aefe545-f8d3-4562-976a-e5eb47d1bb18&pf_rd_r=MHXRV671VD1X32QASWYC&pf_rd_s=center-1&pf_rd_t=60601&pf_rd_i=interfaces&ref_=fea_mn_lk1#). Potential ethical consideration is that the Kaggle dataset has a column “user_id” which may reveal reviewers’ identities by joining with other data sources. The only thing we can do is removing this column in our analysis.

#### Unknowns and Dependencies
I am planning to use TF-IDF and embeddings as starting point, and then try to leverage some deep learning techniques. The only unknow right now is that I am unsure how fast I can implement these and have a deliverable model that can hopefully do better than just random guessing since I do not have much NLP related experience, but my plan is to start early and quickly finish the first cycle of the analysis (starting with simple approach such as TF-IDF) and adjust following plans based on the results. One dependency is that I plan to leverage pre-trained language model to do transfer learning if I have extra time after completing TF-IDF and embeddings steps.
 
## Project Plan
### Introduction

### Data

### Research questions

### Methodology




