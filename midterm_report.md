# Midterm Report
## Dataset Description
### Data Scope and Pre-processing
Since our project requires features from 2 datasets: flight delay data and corresponding weather data, the temporal scope of the dataset is limited to 2016-2020 (included). After getting rid of unuseful columns and combining corresponding weather data with flights, we decided to keep the following sets of features: 
1. Flight Facts: including start, destination airport, operating airline, time of scheduled departure, flight time, etc. 
2. Weather: If a severe weather event occurs during the scheduled departure time
3. Departure delay: if the flight is delayed when departing

More features can help us predict delay better, but we also want to predict delay earlier, preferably before passengers board the plane. The features can be separated into information that is available before plane takeoff (Long term)and information that is only known when the plane is taking off (Short Term). They will be used in our **2 separate models**. The only feature that is included in Short Term but not in Long Term is the **departure delay**, and we expect it to be very informative on whether a plane will arrive later.

To restrain the scope of the project, We will perform **classification tasks** on whether a flight will be delayed. We classify delayed flights as those that **departed successfully and arrived later than announced**. How we treat canceled and diverted flights are detailed below. 

We further decided to narrow our project to an analysis of all flights taking off from the **top 10 largest airports** in the US. This results in a reduced 2GB dataset with 9M entries.

#### Canceled Flights and Diverted Flights
Cancellations and diverted flights are abnormalities we had to decide how to handle them. As canceled flights are canceled before they take off, we decided to exclude canceled flights altogether. For diverted flights, we will only keep flights that eventually reach their destination (as marked by a non-NULL DivArrDelay time) and treat this delay time as a replacement for the normal delay time.

#### Weather
Our weather data records the start and end times of severe precipitation events recorded by different airports. The reason why we only include severe weather events at scheduled take-off is that it is hard to know the “predicted” landing weather. To avoid future bias and to keep our project manageable, **we decided to only take the weather condition at a given airport at the flight’s expected departure time into consideration**. 

### Exploratory Data Analysis

## Feature engineering and Null-values

## Preliminary Models and Analysis
As discussed before, we build 2 sets of models: with departure delay (‘Short Term” forecast model) and without departure delay (Long Term” forecast model) and will evaluate them separately in the following project.

For each of the 2 feature sets, we tried 2 simple models: Logistic Regression and Decision Tree. The weighted average F-1 score we achieved on the test sample is as follow:

| Model                            | F-1 Score |
| -------------------------------- | --------- |
| Logistic (Without DepDelay)      | 0.57      |
| Logistic (DepDelay)              | 0.82      |
| Decision Tree (Without DepDelay) | 0.56      |
| Decision Tree (DepDelay)         | 0.82      |

Clearly, these simple models do not fit the data very well, but we were able to confirm from the feature importance that **departure delay is very informative**.

### Train, Test, Validation Procedure
Since in our simple models there is no hyperparameter tuning, we split our dataset using **train-test split**. During the construction of a more complex model with hyperparameters, we will utilize a train-test-validation split to make sure our test dataset is always kept hidden from the model training process. Due to the large dataset size, we believe even with such splitting each dataset will contain a sufficient number of rows to achieve sound results.

### Under/Overfitting Concerns
We observe no significant differences between train and test error. We believe due to the complexity of the flight delay problem and the large sample size we have, our main concern is how to train **a more complex, expressive model** to resolve underfitting. We plan to do this by trying polynomial features for logistic regression and also trying out different boosting/bagging techniques for Trees. We will also try Neural Networks, which should have the most expressiveness.
