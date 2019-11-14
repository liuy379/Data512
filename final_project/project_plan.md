## Project Plan
### Introduction

### Data
- Data: [https://data.seattle.gov/Public-Safety/Call-Data/33kz-ixgy]
- License : Public Domain
- Source Link: http://www.seattle.gov/police/

Data is queried from Data Analytics Platformm (DAP) and updated incrementally on a daily basis. A full refresh will occur twice a year and is intented to reconcile minor changes. In order to ensure the analysis is completely reproducible, static instead of updated data will be used in this project. This data represents police response activity. Each row is a record of a Call for Service (CfS) logged with the Seattle Police Department (SPD) Communications Center. Calls originated from the community and range from in progress or active emergencies to requests for problem solving. Additionally, officers will log calls from their observations of the field.

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

This dataset only contains records of police response. If a call is queued in the system but cleared before an officer can respond, it will not be included. 

### Research questions

### Methodology
