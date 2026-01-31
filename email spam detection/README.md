                                                     Email Spam Detection

Purpose:

This project is an email spam detection system built using Python and Natural Language Processing (NLP). 
The system analyzes a dataset of emails, extracts important features, and uses a Naive Bayes classifier to predict whether an email is spam or not.


 1. Data Analysis & Preprocessing
    - Data Loading : Load the dataset
    - Data Visualization : Visualize dataset features
    - Data Cleaning : Remove stopwords and duplicates values
    - Data Splitting : Split the dataset into training and testing sets

 2. Model Training
    A Naive Bayes classifier is trained using scikit-learn on the preprocessed data  


 3. Prediction & Evaluation
    - Evaluate the model using accuracy score  
    - Analyze performance with a classification report and confusion matrix 


Dataset:
The dataset contains approximately 5,728 email records with a target column 'spam', indicating whether the email is spam or not.