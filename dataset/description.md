# Dataset description

## Dataset source
[Dataset](https://www.kaggle.com/datasets/hossaingh/udemy-courses?select=Course_info.csv) source is obtain from the www.kaggle.com

---

## About Dataset
This dataset contains detailed information on all available Udemy courses on Oct 10, 2022. This data was provided in the "Course_info.csv" file. Also, over 9 million comments were collected and provided in the "Comments.csv" file.
The information of over 209k courses was collected by web scraping the Udemy website. Udemy holds 209,734 courses and 73,514 instructors teaching courses in 79 languages in 13 different categories.

The related notebook was uploaded here.
If you are interested in analytical data about online learning platforms, I recommend reading the below article to find attractive insight.
https://lnkd.in/gjCBhP_P 

---

## Dataset Description
| Column label | Description | Data types |
| :--- | :--- | :--- |
| id | Course id | int | 
| title | Course title| string |
| is_paid | Chargeable course | bool |
| price | Course price | float |
| headline | Course headline (sneak peek to what course can offer) | string | 
| num_subscribers | Number of subscribers | int |
| avg_rating | Average course rating | float (0.0 to 5.0) |
| num_reviews | Number of reviews | int |
| num_comments | Number of comments | int |
| num_lectures | Number of lectures | int |
| content_length_min | Course content lenth in minutes | float |
| publish_time | Course publish datetime | UTC (ISO 1806 standard) |
| last_update_date | Course last update | year-month-date (YYYY-MM-DD) |
| category | Course catergory | string (catergory) |
| subcatergory | Course subcatergory | string (catergory) |
| topic | Course topic | string |
| language | Course language | string (catergory) |
| course_url | Course url | string |
| instructor_name | Instructor name | string |

---

