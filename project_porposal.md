## Project Description
### Why important
We have all experienced the pain and anxiety when our flights were delayed for an unknown duration and all we can do is wait. In fact, flight delays have caused severe troubles for the economy. According to [Rebollo’s research](https://www.sciencedirect.com/science/article/abs/pii/S0968090X14001041?via%3Dihub), in 2007 alone, the U.S. economy had endured 31–40 billion dollars loss due to flight delays. If we can predict which flight will have delays, consumers, airlines, and air traffic controllers can all benefit from this. Passengers can now feel less troubled and plan their trips accordingly by knowing how long their planes are expected to delay; airlines can use this predicted delay information to optimize connecting flights and notify passengers when they are likely to miss their next flights; air traffic controllers can route planes more efficiently by prioritizing flights that are expected to delay the most and permit them to fly in faster airspace. Although we cannot avoid flight delays entirely, having an accurate prediction ahead of time would mitigate the economic losses from flight delays.

### Problem Formulation
With this problem in mind, we decided to develop a model to predict the expected delay time for U.S. air traffic. To better simulate the actual problem, we decided to provide different models in different scenarios based on information available at:
1. Days before the flight starts, when only airline name, depart, destination information is available (to simulate predicting when consumers are buying tickets)
2. Just before the plane takes off, where local weather conditions, delay conditions for other flights taking off at the same airport are also available. (to simulate air traffic controller/ firms optimizing workflows)

By comparing these models, we can evaluate the possibility of building long-term predictions on flight delays that can better help customers and airlines to prepare for the future.

### Dataset chosen
We believe that flight delays can be due to various factors like the airport’s traffic volume, different airline policies, and changing weather conditions. To make accurate predictions, we rely on the combination of two major datasets:
1. Airline reporting carrier on-time performance dataset ([https://developer.ibm.com/exchanges/data/all/airline/#get-this-dataset](https://developer.ibm.com/exchanges/data/all/airline/#get-this-dataset)), which contains flight information like start/destinations, airline code, etc.
2. US Weather Events (https://www.kaggle.com/sobhanmoosavi/us-weather-events), which contains weather warnings issued by weather stations in different airports.

In the first dataset, we can investigate delay trends that differ by airport/ dates/ time in day/ airline, and in the second dataset, we expect to see how severe weather warnings at start and destination airports affect delay times.
