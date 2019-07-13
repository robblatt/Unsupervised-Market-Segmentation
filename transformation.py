import pandas as pd
import numpy as np

def transform_df(data):
    df = data
    
    # ==============================
    #  ***   DATA CLEANING      ***
    # ==============================
    
    # removing debt adjustment
    df = df[df.StockCode != 'B']
    
    # limit data to one calendar year
    
    df = df[df['InvoiceDate'] <= '2011-12-01 23:59:59']
    
    # ==============================
    #  *** FEATURE ENGINEERING  ***
    # ==============================
    
    # create a new feature which adds up the total revenue for each line item
    df['TotalRevenue'] = df['Quantity'] * df['UnitPrice']
    
    # these create a series of new dataframes that will be merged to
    # become our important features.
    
    # creates the 'frequency' feature
    invoice_count = df.groupby(['CustomerID'], as_index=False)['InvoiceNo'].count()
    invoice_count.rename(columns={'InvoiceNo': 'frequency'}, inplace=True)
    
    # creates the 'monetary' feature, rounds to two decimal places
    customer_total_revenue = df.groupby(['CustomerID'], as_index=False)['TotalRevenue'].sum()
    customer_total_revenue.rename(columns={'TotalRevenue': 'monetary'}, inplace=True)
    customer_total_revenue.TotalRevenue = round(customer_total_revenue.monetary, 2)
    
    # creates the 'recency' feature, first by converting 'InvoiceDate' to datetime to string,
    # then to an integrer, indicating the total days since purchase
    
    df['InvoiceDate']= pd.to_datetime(df['InvoiceDate'])
    df['DaysSincePurchase'] = df['InvoiceDate'].max() - df['InvoiceDate']
    
    RecentPurchase = customer_since_purchase['DaysSincePurchase']
    RecentPurchaseDays = [None] * len(RecentPurchase)
    for i in range(len(RecentPurchase)):
        RecentPurchaseDays[i] = RecentPurchase[i].days
        
    customer_total_revenue_invoice_count_since_purchase['recency'] = RecentPurchaseDays
    customer_total_revenue_invoice_count_since_purchase.drop('DaysSincePurchase', axis=1, inplace = True)
    customer_total_revenue_invoice_count = customer_total_revenue.merge(invoice_count, on='CustomerID', sort=True)
    
# customer_total_revenue_invoice_count_since_purchase.drop('DaysSincePurchase', axis=1, inplace = True)

customer_total_revenue_invoice_count_since_purchase.head(2)    
    
    # changes the index to the CustomerID to avoid it becoming a feature.
    customer_total_revenue_invoice_count_since_purchase.set_index('CustomerID', inplace = True)
    
    # preparing the features for log transformation
    
    customer_total_revenue_invoice_count_since_purchase['monetary'] = customer_total_revenue_invoice_count_since_purchase['monetary'].apply(lambda x: 0.1 if x <= 0 else x)

    # ==============================
    #  *** DATAFRAME CREATION  ***
    # ==============================

    log_features = pd.DataFrame()
    
    log_features['monetary'] = np.log(customer_total_revenue_invoice_count_since_purchase['monetary'])
    log_features['recency'] = np.log(customer_total_revenue_invoice_count_since_purchase['recency'])
    log_features['frequency'] = np.log(customer_total_revenue_invoice_count_since_purchase['frequency'])
    log_features.set_index(index = customer_total_revenue_invoice_count_since_purchase.reset_index()['CustomerID'])
    
