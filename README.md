# **Insurance All** - health insurance company
## **Car insurance interest cross sell**   
![Insurance](https://github.com/Soturno95/Car-Insurance-Interest/assets/95311171/8916c717-9370-40fe-9f74-921e54d3bc87)


# **1. Business problem**
Insurance all is a company that primarily offers health insurance; now the company wants to expand the business offering car insurance to it's clients.   
The company did a survey with 381,109 clients asking about the interest in acquiring a car insurance and now the product team selected 38,111 new customers to participate in a campaign, in which they will be offered the new car insurance product.    
The offer will be made by the sales team through telephone calls; however, the sales team has the capacity to make 10,000 calls within the campaign period.
The goals are:   

- Find important insights about the most relevant attributes of customers interested in purchasing auto insurance.

- Find the percentage of customers that will be interested in purchasing the car insurance with 10,000 calls and 20,000 in case the capacity of the sales team increases.     
- Find how many calls the sales team need to make contact with 80% of customers interested in purchasing auto insurance.  

- Develop an API capable of returning a "propensity score" of each client to purchase the insurance, along with a manual on how to use it.    

# **2. Business assumptions**
The assumptions about the business problem are as follows:       
- Days with stores closed and/or zero sales were not taken into account.       
- Stores without close competitors had the distance fixed at 200000, which is a lot higher than other distances, as a way of preserving the rows, instead of deleting them.   



# **3. Solution strategy**
**Step 01. Data description:** My goal is to use statistics metrics to identify data outside the scope of business.   

**Step 02. Feature engineering:** Derive new attributes based on the original variables to better describe the phenomenon that will be modeled.    

**Step 03. Data filtering:** Filter rows and select columns that do not contain information for modeling or that do not match the scope of the business.   

# **4. Top 3 data insights**   

People between 32 to 54 years old are more propense to buy the car insurance.    

![download](https://github.com/Soturno95/Car-Insurance-Interest/assets/95311171/4a0ea4bf-ce45-40ca-9f73-f84557dcaca8)

Car owner's whose age are between 1 and 2 years are more likely to buy the insurance.   

![download (1)](https://github.com/Soturno95/Car-Insurance-Interest/assets/95311171/c2eb07b8-332c-46ea-93e6-d4693f0c047a)

Car owner's without a history of damage to their vehicles won't buy the insurance.       

![download (3)](https://github.com/Soturno95/Car-Insurance-Interest/assets/95311171/916b97cb-ee91-4d9f-ad20-f0f4b0c39a05)

# **5. Machine learning model applied**   
Tests were made using 6 different algorithms with a 5 fold cross validation; the main metrics used to compare models were the Cumulative Gains Curve, Lift Curve and Precision at k.    

![download](https://github.com/Soturno95/Car-Insurance-Interest/assets/95311171/3264d9fd-f107-4fc3-9b25-9efb80eff749)   
![download (1)](https://github.com/Soturno95/Car-Insurance-Interest/assets/95311171/907f7b70-46b5-4e98-b786-640d6f4f67b6)   

|Models| Precision at 20%:| Models| Precision at 50%:|
|---------|---------------------|--------------|--------|
|LGBM    |0.3472|  XGB | 0.2413 |
|XGB     |0.3455|  LGBM | 0.2412 |
|RF      |0.3140|  LR| 0.2405 |
|ET      |0.3082|  RF| 0.2392 |
|KNN     |0.2920|  ET | 0.2372| 
|LR      |0.2894|  KNN| 0.2019|

# **6. Machine learning model performance**   

The chosen algorithm was LGBM. Below is the hiper parameter fine tuning result with a 5 fold cross validation:   

![download (2)](https://github.com/Soturno95/Car-Insurance-Interest/assets/95311171/364aabb9-be1e-4d52-acf0-f49d33d2ea0a)   

**Precision at 20%: 0.3677**    
**Precision at 50%: 0.2492**    

The result below emulates the production environment; the tuned model was trained with the train and validation data, then used on the test(unseen) dataset.

![download (3)](https://github.com/Soturno95/Car-Insurance-Interest/assets/95311171/e16d527a-fe7b-4850-8216-a0948c3fdf32)

**Precision at 20%: 0.3566**       
**Precision at 50%: 0.2443**       

# **7. Business results**   

The revenue was estimated on $500,00 per car insurance bought, the cost $50,00 per call, and profit the former minus the latter.    

![download](https://github.com/Soturno95/Car-Insurance-Interest/assets/95311171/e2dc98e4-7e0f-4319-9b7f-f9000520f6c4)   

## **7.1 Business questions**   

### 1 - What percentage of customers interested in purchasing car insurance will the sales team reach by making 10,000 calls?

*70.95% of interested clients after 10000 calls (26.24 % of the base)*  

### 2 - If the sales team's capacity increases to 20,000 calls, what percentage of customers interested in purchasing auto insurance will the sales team be able to reach?  

*99.28% of interested clients after 20000 calls (52.48 % of the base)*   

### 3 - How many calls does the sales team need to make to contact 80% of customers interested in purchasing auto insurance?   

*11,904 calls to reach 80% of interested customers (31.24% of the base)*

# **8. Conclusions**

The project successfully answered the business questions and automated part of the sales team effort when reaching the clients.   

# **9. Lessons learned**   

- The metrics used on ranking to learn problems
- Using google sheets to build an responsive and easy to access API

# **10. Next steps to improve**   

- Improving the usability of the google sheet's solution
- Improving the model results with a more throughout hyperparameter fine tuning
