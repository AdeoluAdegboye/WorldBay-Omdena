# WorldBay-Omdena
**Credit scoring application for food subscription company serving underbanked Nigerians **

World Bay  offers a food subscription where users pay for food parcels and receive their food packages only after they have paid the full amount due. 
The users can pay their subscription over a certain number of days (27 days). World Bay offers different tiered plans, and users can upgrade to better plans. 

The majority of  users are unbanked and have no financial footprint. World Bay requested for a way to equip these users by using their paying patterns with World Bay, and other factors  to build credit scores for them. 

This alternative credit-scoring system  will eventually allow them to offer micro-pensions, micro-loans, micro-insurance and other micro-financial services on top of the grocery package subscription that they offer currently. 

Methods & Tools 
<img width="486" height="518" alt="Screenshot 2026-03-03 at 07 39 22" src="https://github.com/user-attachments/assets/9924d7fa-500c-461b-9d44-9f1edd0e0bf2" />

Modeling- ML Algorithms
- Random Forest

SHAP analysis 
SHAP analysis was used to gain more insight into the predictions made by the ML model. SHAP analysis was introduced by (Lundberg and Lee, 2017). This analysis enables computing how much each feature in the model has contributed to the prediction. Using coalitional game theory, shapley values are computed that help to distribute the final prediction among different features of the model. 


Results & Insights 
A total of 49 engineered features were created: 43 were determinants of customer transaction behaviour, 2 were predictors of repayment behaviour, 2 were for demographics, and 4 were DateTime features. These 49 engineered features had gone through a process of feature selection, and the top five best predictors of customer CLV were: (1) prob_of_predicted_purchases_30d, (2) monetary_value, (3) prob_is_active_30d, (4) 4.91 - 180 days, and (5) cond_expected_avg_profit. 

More than 10 engineered features were added to the final model, which drastically increased the accuracy from 50% to 85%. Some features such as gender and implied marital status, were found to have a high percentage of nulls hence the features were dropped. Aside from these, it was found in the CLV modeling that around 7, 927 customers were repeating customers that have at least two transactions. 

With these results, it is suggested that other factors be included as features in the model such as the income level of a customer, marital status, job, gender, and education level among others. 
