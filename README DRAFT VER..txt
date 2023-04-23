
1Introduction

This is a Mini-Project for Nanyang Technological University Singapore's course of SC1015, Introduction to Data Science and Artificial Intelligence. 
In the project, it includes our motivation, an in-depth analysis of our data exploration and the algorithms that we have chosen and last, but not least our findings after the project.
Our inspiration, a thorough examination of our data exploration and the methods we have used, and, last but not least, our conclusions are all included in the project.

2Dataset source
-

3Contributors
-Amizzuddin MD Amin (U2222177J)
- Ye Bowen (U2220893C)
- Sun Qing (U2220313A)

4problem definition(maybe you want to add this?)(good course or good rating predict)
-Our motivation for choosing this project comes from being a course instructor, we want to know whether our course is good enough to be on the (uni or institution) and do not want to waste time building something that is not good.

5Exploratory Data Analysis
-To perform a comprehensive Exploratory Data Analysis, we explore several basic statistical features of dataset, including:
Uni-VariateStatistics (IF YOU NEVER USE THEN REMOVE)
Uni-Variate Visualization (IF YOU NEVER USE THEN REMOVE)
Bi-Variate Exploration (IF YOU NEVER USE THEN REMOVE)
Multi-Variate Exploration (IF YOU NEVER USE THEN REMOVE)
Normal Distribution (IF YOU NEVER USE THEN REMOVE)
with our raw dataset we begin by looking at:
-The different types of data present shown.
-How they relevant between our task or problem defination.
-Their respective distributions and whether there might be class imbalances.
-Missing data and other considerations to be had later during cleaning.

6Data Cleaning and Feature Engineering
-After the EDA step, we have generated insights from the data in terms of their distribution and relevance our overall task. The functions in this package we perform the following functions to clean datasets, like e.g. Drop columns which are irrelevant.

7Training and Evaluation
-After the EDA step, we start to the Classification Model on the dataset. We make several attempts to identify a model that can predict if a path is excellent or terrible based on our self-described characteristic. The model is then saved so that it may be used for future testing.
* DecisionTreeClassifier with OneHotEncoding     (inside my ipy if never use then remove)
* DecisionTreeClassifier with Resampling         (inside my ipy if never use then remove)
* RandomForest                                   (inside my ipy if never use then remove)
* RandomForest with fine-tuned hyper-parameters  (inside my ipy if never use then remove)

8New Things that We Learnt during researching
-Feature engineering by selecting, manipulating that can be used to predict if a course is good or not
-Resampling strategies for imbalanced datasets

9References
Dataset: https://www.kaggle.com/datasets/hossaingh/udemy-courses

Price Prediction Case Study: https://towardsdatascience.com/mercari-price-suggestion-97ff15840dbd

Random Forest: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
               https://www.datacamp.com/tutorial/random-forests-classifier-python