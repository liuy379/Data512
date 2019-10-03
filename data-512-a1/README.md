## Data 512 A1
### Description of the goal of the assignment
This goal of this assignment is to build, analyze, and publish a dataset of monthly traffic on English Wikipedia from January 1 2008 through August 30 2019.

### Data Source
- Legacy Pagecounts API: https://wikimedia.org/api/rest_v1/#/Pagecounts_data_(legacy)/get_metrics_legacy_pagecounts_aggregate_project_access_site_granularity_start_end
- Pageviews API: https://wikimedia.org/api/rest_v1/#/Pageviews_data/get_metrics_pageviews_aggregate_project_access_agent_granularity_start_end
- Wikimedia Foundation REST API: https://en.wikipedia.org/api/rest_v1/

### Description of fields in the output csv file
year: year of the instance
month: month of the instance
pagecount_desktop_views: views count of legacy pagecount through desktop
pagecount_mobile_views: views count of legacy pagecount through mobile
pagecount_all_views: total of pagecount_desk_views and pagecount_mobile_views
pageview_desktop_views: views count of pageview through desktop
pageview_mobile_views: views count of pageview through mobile
pageview_all_views: total of pageview_desktop_views and pageview_mobile_views
