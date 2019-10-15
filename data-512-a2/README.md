## Data 512 A2

## Data
- page_data.csv is the Wikipedia politician by country dataset ([Source](https://figshare.com/articles/Untitled_Item/5513449))
- WPDS_2018_data.csv is the population by country dataset ([Source](https://www.prb.org/international/indicator/population/table/))
- wp_wpds_politicians_by_country.csv is the joined and cleaned dataset used in the analysis
- wp_wpds_countries-no_match.csv is the data that cannot be merged because of entries found in Wikipedia country but not in population country
- revid_no_prediction.csv contains rev_ids that have "ERROR" in their ORES predictions


## Reflection
#### Data Quality
The quality of the source data used in the analysis is good. There is no missing value in both article and population dataset. In both datasets, the "country" attribute, which is used as key for joining, is clean and can be directly used. I have had experience on cleaning country names before (China vs. People's Republic of China), and it was quite frustrating. So I think authors of these two datasets have done a good job in this part. There is minimal data cleaning involved in the analysis. In the article dataset, pages that are not Wikipedia article have identifiable pattern (page names that start with string "Template"), so those entries were removed from the data. Other data cleaning includes data type manipulation and renaming. When getting the prediction data, I wasn't able to pip install ores for some reason. I ended up using the the ORES REST API, and it was very convenient as well.

#### Analysis
Three data sources are used in the analysis. The article ([Source](https://figshare.com/articles/Untitled_Item/5513449)), the population ([Source](https://www.prb.org/international/indicator/population/table/)) and the ORES prediction (extracted in the notebook). The article dataset contains article names, revision_id (key to join ORES prediction data to get article quality prediction) and country name (key to join population data to get country population in mid 2018). The population dataset contains country names and country population. The ORES prediction dataset contains revision_id and ORES prediction of articles quality. The final cleaned and merged dataset has 44464 unique articles from 180 different countries and 6 different regions. 

By calculating the 10 highest-ranked and the 10 lowest-ranked countries in terms of number of politician articles as a proportion of country population, we easily see how population could act as bias. The highest ranked countries are those with incredibly small population (ex. ~10000), and the lowest ranked countries are obviously those with incredibly large population (ex. India, China). So if we are interested in a metric that measures how "political" Wikipedia articles are in a country, then using population as the denominator is not wise. To address this bias, we can use the predited quality of each article based on ORES and calculate the relative proportion of politician articles that are of FA (featured article) and GA (good article) quality, and use this proportion as the metric we are interested in. In such case, we are following the intuition that larger proportion of high quality politician articles might have higher correlation with the metric we are interested in and we are also completely relying on the ORES prediction in the analysis. After calculating the ratio between number of quality articles and total number of articles, I think the result makes much more sense. Countries like North Korea rank at top and contries like Belgium and Switzerland rank at bottom. Similar situation happens when it comes to evaluating the metric on geographic regions. If we calculate ratio of article counts to population, Oceania ranks as top one, but if we calculate ratio of high quality article counts to article counts, Northern America ranks at top one. 

#### Conclusion
North Korea, Saudi Arbia, and Mauritania are the top 3 countries and Belgium, Tanzania, and Switzerland are the bottom 3 countries in terms of ratio of high quality politician articles to total politician articles. In terms of same ratio, Northern America is the top 1 region. The analysis in this project is not complicated given the scope of the data. However, if more data such as the educated population or the economics is given, I think we can conduct more sophisticated and unbiased analysis. Overall, I believe bias in data is inevitable and correctly identify, undertand, and document bias is crucial. 



## Questions
#### "What biases did you expect to find in the data (before you started working with it), and why?"
The number of Wikipedia politician articles at certain time point is determined by many different factors such as population, economics and political events. So when I saw the focus of this analysis is on some ratio metrics, I expected there to be biases in the result.

#### "What (potential) sources of bias did you discover in the course of your data processing and analysis?"
Population is a large factor causing biases in the analysis. Biases in analysis also occur because of lack of other important attributes. (ex. educated population, GDP)

#### "Can you think of a realistic data science research situation where using these data (to train a model, perform a hypothesis-driven research, or make business decisions) might still be appropriate and useful, despite its inherent limitations and biases?"
Conducting statistical test such as t-test on the difference between countries' raitos of high quality politician articles to total articles can be valid and informative. However, not all countries are suitable to be used in the test as some of the sample sizes (number of total articles) are quite small.

#### "How might a researcher supplement or transform this dataset to potentially correct for the limitations/biases you observed?"
Gathering more data is the first choice. More attributes such as educated population, economics and political events can provide more perspectives about the data so that biases can be better understood and handled.






