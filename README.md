# Market Segmentation Clustering Project

## The Goal
Identify various customer groups for various types of marketing and advertising campaigns from the [Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail) available from UCI. A [presentation of findings](https://docs.google.com/presentation/d/1ISuALqLZ45yDU_TamYawt6bQQjVwkzvrEZoaMLeNt54/) is available.

## The Data
1 year, 500k transactions

### Original Features
* InvoiceNo
* StockCode
* Description
* Quantity
* InvoiceDate
* UnitPrice
* CustomerID
* Country

### Engineered Features for Clustering
The data is itemized purchases, the data was transformed to be on a per customer basis.
* monetary
  * Amount of money spent
* frequency
  * Number of orders
* recency
  * Days since the most recent order
* quantity
  * Number of items purchased

#### Customer Specific Information After Log Transformation:
![mapping revenue, number of purchases, & recency](https://raw.githubusercontent.com/robblatt/unsupervised_learning_market_segmentation_clustering_applied/master/log%20plot.gif)

## Clustering
Using scikit-learn's KMeans and Agglomerative Clustering, using nubmer of clusters and linkage as hyperparameters.

## Selected Clustering
Agglomerative Clustering, using Ward linkage and 6 clusters produced the best results.

Cluster 0: This cluster represents 43.22% of the population and 13.96% of Total Revenue, with a total spend of £1,116,608.17
* Identified as a "middle-bottom" customer

Cluster 1: This cluster represents 26.51% of the population and 29.38% of Total Revenue, with a total spend of £2,350,481.65
* Identified as a "middle-top" customer

Cluster 2: This cluster represents 3.07% of the population and 4.43% of Total Revenue, with a total spend of £354,290.68
* Identified as a "middle-top" customer

Cluster 3: This cluster represents 18.99% of the population and 2.51% of Total Revenue, with a total spend of £200,954.75
* Identified as a "middle-bottom" customer

Cluster 4: This cluster represents 7.04% of the population and 49.89% of Total Revenue, with a total spend of £3,992,169.96
* __Identified as the top-tier customers__

Cluster 5: This cluster represents 1.18% of the population and -0.16% of Total Revenue, with a total spend of £-13,182.79
* Identified as "bottom-tier" customers

### Clusters visualized
![clusters, mapped in a 3d space](https://raw.githubusercontent.com/robblatt/unsupervised_learning_market_segmentation_clustering_applied/master/3d%20clusters.png)

#### Files

* Combined Data.ipynb
  * Final notebook where the complete work and pipelines was done
*  transformation.py
  * function used to perform all data cleaning and feature engineering
* online_retail_data.xlsx
  * The original data, changed to **raw data.csv** in order to speed up the importing process
* raw data.csv
  * see above
*	Rob Discovery.ipynb
  * The notebook used to perform EDA
* One Complete Cycle.ipynb
  * Used as a proof of concept
*  market_segmentation.ipynb
  * EDA and trials of data manipulation
* log_imgs/
  * store png files to create an animated gif of the log transformed data
* non_log_imgs/
  * same as log_imgs/ but for the pre-transformed data
