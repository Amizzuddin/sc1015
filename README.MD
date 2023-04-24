# SC1015 Mini Project

## Dataset source
Dataset is taken from kaggle. Click [here](dataset/description.md) for more information on dataset

## Contributors
- Amizzuddin MD Amin (U2222177J)
- Bowen
- Sun Qing

Click [here](contributions/CONTRIBUTORS_INSTRUCTIONS.md) for contributors instructions.

## problem definition
Our motivation for the study to find out if content creator has influence over the quality, price and quantity of the course provided in udemy (an online platform) 

## Exploratory Data Analysis
- To perform a comprehensive Exploratory Data Analysis, we explore several basic statistical features of dataset, including:
    - Multi-Variate Exploration
    - Normal Distribution (valid for numerical types)
    - Correlation ratio (valid for both categorical and numerical types)
- with our raw dataset we begin by looking at:
    - The different types of data present shown.
    - How they relevant between our task or problem defination.
    - Their respective distributions and whether there might be class imbalances.
    - Missing data and other considerations to be had later during cleaning.
- Detailed EDA can be could at the following:
    - [EDA done by Amizzuddin](contributions/amizzuddin/amizzuddin.ipynb)
    - [EDA done by SunQing](contributions/sunqing/SunQingMainWorking.ipynb)
    - [EDA done by Bowen](contributions/bowen/update%20from%20SQ.ipynb)

## Use of YAML (yet another markup language)
YAML file is use to configure of the following:
- features to inclue into the dataframe
- clean up parameters
- category feature for count visualizartion
- numerical versus categorical features for EDA visualization
- kprotoypes parameters
- decision tree classfier parameters

## Data Cleaning and Feature Engineering
After the EDA step, we have generated insights from the data in terms of their distribution and relevance our overall task. The functions in this package we perform the following functions to clean datasets, like e.g. Drop columns which are irrelevant.

## Training and Evaluation
- After the EDA step, we start to the Classification Model on the dataset. We make several attempts to identify a model that can predict if a path is excellent or terrible based on our self-described characteristic. The step taken for training our model are as follows:
    - Kprototypes to create clusters which will be added into dataset
    -  DecisionTreeClassifier to verify the clusters created by Kprototypes

## New Things that We Learnt during researching
- Feature engineering by selecting, manipulating that can be used to predict if a course is good or not
- Resampling strategies for imbalanced datasets

## References
- [Price Prediction Case Study](https://towardsdatascience.com/mercari-price-suggestion-97ff15840dbd)
- [Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
- [Random Forest Tutorial](https://www.datacamp.com/tutorial/random-forests-classifier-python)
- [K-Prototypes](https://antonsruberts.github.io/kproto-audience/)
- Course Content Xtra Module : (under Data-Driven Identification: MX topic 4) The idea of kprototype is the same as K-Means.