# Project Plan - Seattle Police Call Response Time Analysis
## Introduction
When we run into emergencies, knowing that polices are typically only a few minutes away and they can reach us in fairly short amount of time is definitely comforting. Clearly, average response times in different cities can vary a lot due to factors such as city population, police funding, and available resources in a given region. Specifically, according to [this article by Matt Halpin](https://www.asecurelife.com/average-police-response-time/), the average police response time in Seattle is 9 minutes, which is quite higher than the response time in other US major cities. When it comes to emergencies, every minute counts. Therefore, I decide to take a look at the police response time in Seattle alone with other interesting/helpful characteristics.

## Research Questions
- How does SPD's response time varies by call priority, call type, event type, and region?
- Can we build a model to predict response time with the given dataset?

Potential answers to the above questions can shed light on some of the characteristics of SPD's response time. For example, plotting response time to emergency calls of different priorities overtime can show the trend of response time. Side by side comparison of crime counts and response time by regions can help SPD to identify regions that have high total crime counts but are not receiving fast enough responses yet, so the SPD can make adjustments based on that.

## Data
- Data: [https://data.seattle.gov/Public-Safety/Call-Data/33kz-ixgy]
- License : Public Domain
- Source Link: http://www.seattle.gov/police/

Data is queried from Data Analytics Platformm (DAP) and updated incrementally on a daily basis. A full refresh will occur twice a year and is intented to reconcile minor changes. In order to ensure the analysis is completely reproducible, static instead of updated data will be used in this project. This data represents police response activity. Each row is a record of a Call for Service (CfS) logged with the Seattle Police Department (SPD) Communications Center. Calls originated from the community and range from in progress or active emergencies to requests for problem solving. Additionally, officers will log calls from their observations of the field. The data has 4154077 rows and 11 columns, and it is around 770 MB.

| Column Name | Description | Datatype |
| --- | --- | --- |
| CAD Event Number | Unique ID | Text |
| Event Clearance Description | How the call was resolved, as reported by the primary officer | Text |
| Call Type | How the call was received by the Communications Center | Text |
| Priority | Priority of the call, as assigned by the CAD system | Text |
| Initial Call Type | How the call was classified, initially by the Communication Center | Text |
| Final Call Type | How the call was classified, finally by the primary officer | Text |
| Original Time Queued | Time queued in the CAD system | Floating Timestamp |
| Arrived Time | Time the first officer arrived on the call | Text |
| Precinct | Precinct where the call originated | Text |
| Sector | Sector where the call originated. All Sectors roll up to one of five Precincts | Text |
| Beat | Beat where the call originated. All Beats roll up to Sectors | Text |

This dataset only contains records of police response. If a call is queued in the system but cleared before an officer can respond, it will not be included. The data itself does not contain any identify or ethical information. However, the CAD Event Number is an unique identifier for each call (or instance), and there might exist external source that happens to have this information as well alone with other detailed information such as name of the caller and specific location of the instance. Currently, I am not able to find any of the external source.


Add crime table here
Add description of crime table here



## Related Work and Intuitions
Most US police departments follow at least three levels of prioritization to ensure emergencies with higher priorities are addressed before those with lower priorities. Typical priority 1 calls are usually dangerous and in-progress crime that requires immediate response. Lower-priority calls usually include instances such as traffic disputes and stolen goods, which are relatively less urgent. [Matt Halpin](https://www.asecurelife.com/average-police-response-time/) has showed the 10 major US cities ranked by average police response time. Generally, police departments in most US cities aim for an average response time of about 5 to 6 minutes, but it actually varies quite a lot. Halpin has raised a good point in his article that it seems like response time is not related to city population but it is kind of related to growth of city population. This is an interesting point and we can actually perform a similar analysis using the our data (response time vs. populations in precinct/sector/beat). If analysis indicates information such as region population is good feature, we can then find more external data sources (education, financial) within precinct/sector/beat and use these features to build a regression model to predict response time.

## Methodology and Tools
`Matplotlib` and `seaborn` are mainly used for visualization purpose. A `Tableau` dashboard is also included in the analysis to compare crime counts and average response time on two identical maps. `t-test` is used to test perform statistical tests in some parts of the analysis, and the code is written in python with the `scipy` package. Finally, `decision tree` is used for modeling response time as all the features in the dataset are binaries and the feature importance provided by tree based model is useful for interpretation.


## Results
### Response Time by Priority
Generally, priority 1 represents events that require immediate actions such as in progress shooting. Priority 2 are events slightly less urgent than priority 1 but also require immediate actions to prevent them developing into priority 1 events. Priority 3 & 4 events are less moderate events such as traffic issues. And finally starting at priority 5, the events are directly handled by the communication center instead of officers. To make the groups more representative and also make the chart more easier on the eye, I regroup the priorities into 1, 2, 3 & 4, and 5+. So in the below chart, we can see that response time to top priority calls is consistent overtime. Response to priority 2 calls becomes slower as time goes. And for certain period (2015 - 2018), response time to priority 3 & 4 is shorter than priority 5 plus.

### Response Time by Call Type
Call type in the datasets indicates the method that the person requests call for service. There are 11 unique call types in total and the chart below shows the top call types sorted by response time. Clearly, SPD response to alarm calls (bank, school, residential, bust, taxi) in shortest time compare to other call types. Perhaps because initiating alarm calls in these locations is easy and well practiced, the response time of this type ranks at the top in the chart. Other than this, it is interesting to observe that response to text messages is slightly faster than 911 calls, but the difference is not statistically significant. While I was working on this part, I wondered if response to 911 calls faster than non 911 calls. And according to the below chart, the answer is yes. Response to 911 calls are generally faster than non 911 calls even for low priority calls such as priority 6 and 7.

### Response Time by Event type
Event type in the dataset indicates is the description of event initially identified by communication center. There are 271 unique event types in total and the chart below shows the top event types sorted by response time. It is comforting to see that calls that request backups or report active shootings receive fastest responses. Additionally, most of the times here are less than 6 minutes, which is the goal SPD is aiming for.

### Response Time by Region
A side by side comparison of crime counts and response time is done in Tableau. The entire Seattle region is divided into beats, which is the most granular unit used by SPD for patrol deployment. Below is a screenshot of the dashboard and the actual interactive dashboard can be found here. Optimally, we want to see regions with dark red on the left chart are also in light green on the right chart. This means regions that have high crime counts are also receiving fast responses. Hovering over any region on the left chart will give you the breakdown of crime counts in categories in that region. Hovering over any region on the right chart will give you the average response time of each priority group for that region. Clicking any region in the left chart will give you the crime counts overtime for that region, and of course clicking any region in the right chart will give you the average response time overtime for that region. This dashboard can be useful to SPD to identify regions that have high crime counts but are not receiving fast enough responses yet (regions in both dark red and dark green) such as K1, and SPD can make adjustments in terms of police force or policies to address the issue.

### Predict Response Time
As mentioned before, decision tree is selected to model response time in this project. I chose to use xgboost, which is the fast version of gradient boosting trees, and the final root mean square error is 13.8. The feature importances are plotted below and we can see that priority is much more crucial than call time in determining response time. This is comforting result for sure, and one future work is to add traffic data into the model and see if that would replace priority features.

## Reflection
### Data Collection
Originally, my project was using the IMDB dataset to build an NLP model to identify spoilers in user reviewers. The dataset was quite tricky. The data was publicly on Kaggle and it was listed as in public domain. However, when I went to the source of the data, which is IMDB, I found that the terms specifically indicate that users of the data cannot republish it in any form. So this was quite shocking to me as the author of the modified version of the data does not mention anything about the license of the original data, and his statement even makes it sound like the license is in his hands (link to the Kaggle page). So I reached out to the IMDB legal team and was informed that the data is not eligible for republishing as expected, which is definitely a lesson for me in terms of tracking the source of any datasets and identifying the license of that source. Therefore, I changed my project topic to the current one, and of course all the data I used in the project are licensed in public domain.

### Coding
Considering the clarity and transparency of the analysis, I use 3 scripts and each focuses only on thing such as data cleaning or modeling. One thing I have ensured in this project is running jupyter notebook from start to end after finishing all the code so that the line numbers cells are in sequence and viewers will not get lost viewing and trying to reproduce the analysis.

### Modeling
First of all, one of the reasons that choosing decision tree in this project is that it is not black box algorithm so it has advantages over other black box algorithms in terms of transparency. Additionally, interpretability of model is definitely crucial for human centered data science, and feature importances provided by tree based models serve this purpose well.





### Sources
- https://data.seattle.gov/Public-Safety/Call-Data/33kz-ixgy]
- http://www.seattle.gov/police/
- https://www.asecurelife.com/average-police-response-time/
