## Dataset Description
### Data Scope and Pre-processing
Our project utilizes features from 2 datasets: flight delay data and corresponding weather data. The temporal scope of the dataset is limited to 2016-2020 (included). After getting rid of unuseful columns and combining corresponding weather data with flights, we decided to keep the following sets of features: 
1. Flight Facts: including start, destination airport, operating airline, time of scheduled departure, flight time, etc. 
2. Weather: If a severe weather event occurs during the scheduled departure time
3. Departure delay: if the flight is delayed when departing

To restrain the scope of the project, We will perform **classification tasks** on whether a flight will be delayed. We classify delayed flights as those that **departed successfully and arrived later than announced**. How we treat canceled and diverted flights are detailed below. 

More features can help us predict delay better, but we also want to predict delay before passengers board the plane. Our features can be separated into information that is available before the plane actually depart (Long term) and information that is only known when the plane is taking off (Short Term). They will be used in our **2 separate models**. The featurs that are included in Short Term but not in Long Term is the **departure delay** , and we expect it to be very informative on whether a plane will arrive later.

We further decided to narrow our project to an analysis of all flights taking off from the **top 10 largest airports** in the US. This results in a reduced 2GB dataset with 9M entries.

#### Canceled Flights and Diverted Flights
 As canceled flights are canceled before they take off, we decided to exclude canceled flights altogether. For diverted flights, we will only keep flights that eventually reach their destination and classify whether they delay like normal flights.

#### Weather
Our weather data records the start and end times of severe precipitation events recorded by different airports. To avoid future bias and to keep our project manageable, we decided to only consider the **weather condition at origination of a flight during its expected departure time** into consideration since it is hard to know the “predicted” destination weather. We do plan to explore how to include more weather information of the destination in the full report.

### Exploratory Data Analysis

### Null-values
We listed most relevant missing value features and their percentageas below.
| Feature  | description                | # NA  | Percentage in 9142933 data |
| -------- | -------------------------- | ----- | -------------------------- |
| DepDelay | Departure delay in minutes | 721   | 0.00789%                   |
| ArrTime  | arrival time               | 3504  | 0.0383%                    |
| ArrDelay | Arrival delay in minutes   | 21404 | 0.2341%                    |

For *DepDelay*, missing values are due to take off on time so we fill them with 0. For *ArrDelay* null values, if the flight is diverted, the delay information is recorded in *DivArrDelay*, otherwise, it's due to arrive on time; therefore we fill with 0 and values from *DivArrDelay* correspondingly. We removed rows without *ArrTime* as they are corrupted data that can’t be used for training.

### Feature engineering
We listed several most important feature engineering steps as below:

1. **Weather related**: 
For condition severity, each weather condition (rain, fog, etc.) has 5 possible values: “NA” (no), “Light”, “Moderate”, “Heavy” and “Severe” to represent how serious the condition is. Thus, we used real encoding from 0 (NA) to 4 (Severe) for indication.
2. **Time related**:
For *DepTime*, if we turn each take off time into a category by one-hot , the number of features will be too large and leads to overfitting. Therefore, we matched each *DepTime* into midnight (0-6), morning(6-12), afternoon (12-18) and night (18-24) and then did one-hot encoding on these 4 categories instead. For flight date, we pick *Quarter* and *DayofWeek* as categorical data and encode with one-hot.
3. **Airline related**:
We condier airline company to be more representative than flight number in prediction. Thus, we encoded *Reporting_Airline* by one-hot and dropped *Flight_Number_Reporting_Airline*. 
4. **Location related**:
We first encoded *Origin* (origin airpot) by one-hot. Then for arrival airport, there are too many values which may possibly lead to overfitting. Thus, we decided to try two versions of one-hot encoding, one for *DestState* (arrival state) as destination category and one for *Dest* (arrival airport) as destination category.

To sum up, after dealing with null values and feature engineering, we have **8988665 rows of data**. For version 1(*DestState*), we have **112 features** and for version 2(*Dest*), we have **382 features**.

## Preliminary Models and Analysis
As discussed before, we build 2 sets of models: with departure delay and weather ("Short Term" forecast model) and without them ("Long Term" forecast model). We use all features to build these preliminary models.

For each of the 2 feature sets, we tried 2 simple models: Logistic Regression and Decision Tree. The weighted average F-1 score we achieved on the test sample is as follow:
<table>
  <tr>
    <th>Model</th>
    <td>Logistic (LT)</td>
    <td>Logistic (ST)</td>
    <td>Decision Tree (LT)</td>
    <td>Decision Tree (ST)</td>
    <td>Dummy (Majority)</td>
  </tr>
  <tr>
    <th>Weighted F-1 Score</th>
    <td>0.57</td>
    <td>0.82</td>
    <td>0.56</td>
    <td>0.82</td>
    <td>0.49</td>
  </tr>
</table>


Clearly, these simple models do not fit the data very well, but they are all better than simply guessing the majority class. We were also able to confirm from the feature importance of decision tree that **departure delay is very informative**. We also observed that one-hot encoding of destination states is not very informative, which makes us decide to try Lat-Lon representation instead in the following project.

### Train, Test, Validation Procedure
We split our dataset using **train-test split**. For hyperparameter tuning, we will utilize a **train-test-validation split** . Due to the large dataset size, we believe even with such splitting each dataset will contain a sufficient number of rows to achieve sound results.

### Under/Overfitting Concerns
We observe **no significant differences** between train and test error. Due to the complexity of the flight delay problem and the large sample size we have, we will focus on how to train **a more complex, expressive model** to resolve **underfitting**. We plan to do this by trying polynomial features for logistic regression and also trying out different boosting/bagging techniques for Trees. We will also try Neural Networks, which should have the most expressiveness.

### Further Improvement
We will continue to work on the following area to improve the model:
1. Better metrics, weight false positive and false negatives differently.
2. Explore the effect of balancing dataset before training
3. Introduce more complex models, like boosting, bagging, neural networks, etc.
4. Re-visit the origin/destination features and see if any alternative encoding (latitude/longitude, etc.) can improve the model.
5. Re-visit the weather data and see if we can add more destination weather features to the model.
6. Run Feature Selection or PCA before training to reduce data size and increase result interpretability.

We will also compare the result of our two models and see if we can shorten the gap in accuracy between predictions using short-term and long-term information. Our desired goal is to have a model that can predict delay using only long-term features and is as good as the one using departure delay.
