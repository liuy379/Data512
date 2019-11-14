## Project Plan
### Introduction

### Data
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

This dataset only contains records of police response. If a call is queued in the system but cleared before an officer can respond, it will not be included. The data ifself does not contain any identify or ethical information. However, the CAD Event Number is an unique identifier for each call (or instance), and there might exist external source that happens to have this information as well alone with other detailed information such as name of the caller and specific location of the instance. Currently, I am not able to find any of the external source. 

### Research questions
- How do call trends differ by precinct/sector/beat?
- How do priorities of calls look like over time?
- Is the response time to high priority calls significantly shorter than that to low priority calls?
- Are proportions of call types significantly different?
- Do final call types (identified by officers) match initial call types (identified by communication center) well?

Most of the attributes in the dataset are categorical. The Original_Time_Queued ranges between April 2010 to April 2019, so it can be used alone with other aggregated statistics to analyze how those statistics increase and decrease over time. The difference between Original_Time_Queued and Arrive_Time gives us the response time, which will be the only numeric feature in the dataset. 


### Methodology and Tools
As we are comparing differences between groups, `t-test` for difference between groups and proportions and `chi-square test` are two of the major parts in this project. Also, since we have some geographic information, visualizations are also crucial. So I decide to to use `R` in this project since it is language made for statistical tests, and use R's `ggplot2` packages for visualization to maintain consistency. I also plan to build interactive dashboard using `Bokeh` if I have time.












