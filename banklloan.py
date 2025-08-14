#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import plotly.express as px


# In[11]:


get_ipython().system('pip install pandas')


# In[12]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import plotly.express as px


# In[13]:


get_ipython().system('pip install matplotlib seaborn plotly')


# In[14]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import plotly.express as px


# In[15]:


df = pd.read_excel("C:/Users/Ankit/Downloads/financial_loan.xlsx")


# In[ ]:


get_ipython().system('pip install xlrd')


# In[ ]:


df = pd.read_excel("C:/Users/Ankit/Downloads/financial_loan.xlsx")


# In[ ]:


get_ipython().system('pip install openpyxl')


# In[ ]:


df = pd.read_excel("C:/Users/Ankit/Downloads/financial_loan.xlsx")


# In[ ]:


df = pd.read_excel("C:/Users/Ankit/Downloads/financial_loan.xlsx")


# # Bank Loan Analysis Report
# 

# In[35]:


import pandas as pd

df = pd.read_excel(
    r"C:\Users\Ankit\Downloads\financial_loan.xlsx",
    engine="openpyxl"
)


# In[ ]:


df.head()


# # Metadata of data
# 

# In[ ]:


print ("No of rows:",df.shape[0])


# In[ ]:


df.dtypes


# 

# In[ ]:


df.describe()


# # Total Loan Application

# In[40]:


total_loan_application = df['id'].count()
print("Total loan Application:" , total_loan_application)


# # MTD Total Loan Application

# In[36]:


latest_issue_date = df['issue_date'].max()
latest_year = latest_issue_date.year
latest_month  = latest_issue_date.month
mtd_data = df[(df['issue_date'].dt.year == latest_year)&(df['issue_date'].dt.month == latest_month)]
mtd_loan_applications = mtd_data['id'].count()
print(f"MTD Loan Applications(for {latest_issue_date.strftime ('%B %Y')}):{mtd_loan_applications}")


# # Total funded amount

# In[37]:


total_funded_amount = df['loan_amount'].sum()
total_funded_amount_millions = total_funded_amount/1000000
print ("Total funded amount:",total_funded_amount_millions)


# # MTD Total Loan Application

# In[38]:


latest_issue_date = df['issue_date'].max()
latest_year = latest_issue_date.year
latest_month  = latest_issue_date.month
mtd_data = df[(df['issue_date'].dt.year == latest_year)&(df['issue_date'].dt.month == latest_month)]
mtd_total_funded_amount = mtd_data['loan_amount'].sum()
mtd_total_funded_amount_millions=mtd_total_funded_amount/1000000
print("MTD Total Funded Amount: ${:.2f}M".format(mtd_total_funded_amount_millions))


# # Total amount received

# In[16]:


total_amount_received = df['total_payment'].sum()
total_amount_received_millions = total_amount_received/1000000
print("Total Amount received: ${:.2f}M".format(total_amount_received_millions))


# # MTD Total amount received

# In[34]:


latest_issue_date = df['issue_date'].max()
latest_year = latest_issue_date.year
latest_month  = latest_issue_date.month
mtd_data = df[(df['issue_date'].dt.year == latest_year)&(df['issue_date'].dt.month == latest_month)]
mtd_total_amount_received = mtd_data['total_payment'].sum()
mtd_total_amount_received_millions=mtd_total_amount_received/1000000
print("MTD total amount received: ${:.2f}M".format(mtd_total_amount_received_millions))


# # Avg interst rate

# In[43]:


avg_int_rate = df['int_rate'].mean()*100
print("Avg int rate:{:.2f}%".format(avg_int_rate ))


# # Avg debt-to-income ratio

# In[42]:


avg_dti = df['dti'].mean()*100
print("Avg DTI:{:.2f}%".format(avg_dti ))


# # Good loan 

# In[47]:


good_loans = df[df['loan_status'].isin(["Fully Paid","Current"])]

total_loan_applications = df['id'].count()

good_loan_applications = good_loans['id'].count()
good_loan_funded_amount = good_loans['loan_amount'].sum()
good_loan_received = good_loans['total_payment'].sum()
good_loan_funded_amount_millions = good_loan_funded_amount / 1000000
good_loan_received_millions = good_loan_received / 1000000

good_loan_percentage = (good_loan_applications / total_loan_applications) * 100

print("Good loan applications:" , good_loan_applications)
print("Good loan funded amount(in millions):${:.2f}M".format(good_loan_funded_amount_millions))
print("Good loan received amount(in millions):${:.2f}M".format(good_loan_received_millions))
print("Good loan percentage:{:.2f}%".format(good_loan_percentage))


# # BAD Loan

# In[50]:


bad_loan = df[df['loan_status'].isin(["Charged Off"])]
total_loan_applications = df['id'].count()
bad_loan_applications = bad_loan['id'].count()
bad_loan_funded_amount = bad_loan['loan_amount'].sum()
bad_loan_received_amount = bad_loan['total_payment'].sum()
bad_loan_funded_amount_millions = bad_loan_funded_amount / 1000000
bad_loan_received_amount_millions = bad_loan_received_amount / 1000000
bad_loan_percentage = (bad_loan_applications / total_loan_applications) * 100

print("Bad loan applications:", bad_loan_applications)
print("Bad loan funded amount (in millions): {:.2f}M".format(bad_loan_funded_amount_millions))
print("Bad loan received amount (in millions): {:.2f}M".format(bad_loan_received_amount_millions))
print("Bad loan percentage: {:.2f}%".format(bad_loan_percentage))


# # Monthly trend by issue date for total funded amount

# # Employee Length by total funded amount
# 

# In[55]:


emp_funding = df.groupby('emp_length')['loan_amount'].sum().sort_values() / 1000

plt.figure(figsize=(10, 6))
bars = plt.barh(emp_funding.index, emp_funding, color='red')
plt.xlabel("Funded amount (in thousands)")
plt.ylabel("Total funded amount by employment length")
plt.tight_layout()
plt.show()

