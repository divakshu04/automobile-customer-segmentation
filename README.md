# Automobile Customer Segmentation

Customer segmentation is the practice of dividing a customer base into groups of individuals that are similar in specific ways relevant to marketing, such as age, gender, interests and spending habits.

An automobile company has plans to enter new markets with their existing products (P1, P2, P3, P4 and P5). After intensive market research, they’ve deduced that the behavior of new market is similar to their existing market.

In their existing market, the sales team has classified all customers into 4 segments (A, B, C, D ). Then, they performed segmented outreach and communication for different segment of customers. This strategy has work exceptionally well for them. They plan to use the same strategy on new markets and have identified 2627 new potential customers.


## Project Structure

'segmentation-code.ipynb' - contains detailed code with step by step process from data cleaning to testing the model.

'train.csv' - contains dataset to train model.

'test.csv' - contains dataset to test the model.

'segmentation_module.py' - contains concise python code of making the model and predicting values. The file works as an module.

'predicted_test_data.ipynb' - contains the result of the prediction on 'test.csv' data file.
## Installation

Requirements needed to run this project:

1. Install 'Python' with mentioned modules:
```bash
  pip install pandas
  pip install numpy
  pip install matplotlib
  pip install seaborn
  pip install sklearn
  pip install tensorflow

```
    
## Model Overview
 The model is made to predict a category of a person from A, B, C, D providing dataset with different features. It divides the dataset into four different groups.
## Model Result

After predicting groups, we can analyze different features:

1. Gender vs Prediction
  ![Gender vs Prediction](https://github.com/divakshu04/automobile-customer-segmentation/assets/127183494/4d4d338d-e8ef-4cb5-8259-30ca6823bd79)

2. Ever Married vs Prediction
  ![Ever Married vs Prediction](https://github.com/divakshu04/automobile-customer-segmentation/assets/127183494/57ad52f3-eb24-49cd-a455-1def2afd81f2)

3. Age vs Prediction
  ![Age vs Prediction](https://github.com/divakshu04/automobile-customer-segmentation/assets/127183494/5dc80e4f-ddac-4c28-875c-facd17595c44)

4. Graduated vs Prediction
  ![Graduated vs Prediction](https://github.com/divakshu04/automobile-customer-segmentation/assets/127183494/d7aa2c26-0f8c-45a4-8211-5cffe077b63e)

5. Profession vs Prediction
  ![Profession vs Prediction](https://github.com/divakshu04/automobile-customer-segmentation/assets/127183494/ebac351f-9b62-4b20-90f0-1fb7aab070a2)

6. Work Experience vs Prediction
  ![Work Experience vs Prediction](https://github.com/divakshu04/automobile-customer-segmentation/assets/127183494/25c2a6c4-e5ae-42ea-9388-bfa289f3b1ec)

7. Spending Score vs Prediction
  ![Spending Score vs Prediction](https://github.com/divakshu04/automobile-customer-segmentation/assets/127183494/2233a307-2a75-4c5d-be59-a22ac998d82c)

8. Family Size vs Prediction
  ![Family Size vs Prediction](https://github.com/divakshu04/automobile-customer-segmentation/assets/127183494/b4510b5b-6041-4d9e-af41-42210252d6d4)

9. Var_1 vs Prediction
  ![Var_1 vs Prediction](https://github.com/divakshu04/automobile-customer-segmentation/assets/127183494/94e0c224-b16b-4916-b3dc-638a6c513b4c)

From the above analysis we can define each groups as:

GROUP A:
``` batch
- Females are slightly more than Males.
- Number of customers who are married are slightly more than those who are not married.
- Majority of customers are of younger to some adult customers with age group (20 - 45).
- Number of graduated customers are slightly more than those who are not.
- Majority of customers has profession 'Entertainment' followed by 'Engineers' and 'Artist'.
- Majority of customers has work experience of only one or none.
- Majority of customers has low spending score.
- Majority of customers has family size of two. i.e. they must be married.
- Most of the customers lies in Cat_6.
```
GROUP B:
``` batch
- Females are slightly more than Males.We can say that gender is equally divided.
- Number of customers who are married are more than those who are not married.
- They contain slightly more adult customers than group A with age group (30 - 55).i.e. youngsters are rare in this group.
- Number of graduated customers are more than those who are not.i.e. the group contains educated customers.
- Majority of customers has profession 'Artist' followed by 'Engineers'.
- Majority of customers has work experience of only one or none.
- Majority of customers has low spending score.
- Majority of customers has family size of one. i.e. they must be single or not married or maybe they are living alone.
- Most of the customers lies in Cat_6.
```
GROUP C:
``` batch
- Males are slightly more than Females.
- Almost all customers in this group are married.
- Majority of customers are older customers with age group (35 - 75).
- Number of graduated customers are slightly more than those who are not.
- Majority of customers has profession 'Artist' followed by 'Lawyers'.
- Majority of customers has work experience of only one or none.
- Majority of customers has average spending score.
- Majority of customers has family size of two. i.e. they must be married.
- Most of the customers lies in Cat_6.
```
GROUP D:
``` batch
- Males are more than Females.
- Number of customers who are not married are more than those who are married.
- Majority of customers are of younger customers with age group (18 - 35).
- Number of non-graduated customers are more than those who are not.
- Majority of customers has profession 'Healthcare' followed by 'Executive'.
- Majority of customers has work experience of only one or none.
- Majority of customers has low spending score.
- They contains mixture in family size. i.e. mostly customers have family size of one or four, which means that they are single or living in their parent's house.
- Most of the customers lies in Cat_6.
```
## Conclusion

This concludes that:

GROUP A:-

This group targets to newly customers which have low spending score. Majority of customer has profession of Entertainment which means they are likely to travel more, or maybe they loved to travel more.
Hence, these customers are targeted for COMPACT CARS or BUDGET-FRIENDLY SUVs for better traveling experience.

GROUP B:-

This group targets to newly customers which have low spending score. Mostly they are married and maybe living separately from their families due to work. Majority of customers has profession of Artist. Hence, these customers are targeted for cars like MINIVANS or TRANSPORTATION CARS to get more space for the supplies of their artwork.

GROUP C:-

This group targets to newly customers which have average spending score. Most customers in this group are settled and are old and married.Hence, these customers are targeted for MIDSIZE CARS or MID-RANGED SUVs.

GROUP D:-

This group targets to newly customers which have low spending score. These are middle-class customers with not much education and are younger and working in profession like Healthcare. Mostly they are living alone or with their parents. Hence, these customers are targeted for cars like COMPACT CARS, LOW-END CARS or USED CARS to be affordable for any group.
