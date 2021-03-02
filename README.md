### Tools
1. For Scrapping - Selenium
2. Preprocessing - nltk,stopwords
3. Model Build - tfidfvectorizer, classification(SGD)

## Business Understanding 
This project aims to predict salary for specific fields - data related positions. Therefore, the training and test data is better to be limited within data/analytics related job positions to get more valuable features. When scrapping the data, we make sure one of these keywords exist in the whole job description: 'data analytics','data science','analysis'.

## Data Sources
Indeed.com, 1000+ jobs were scrapped from Indeed.com By using Selenium

### Deployment
To make this tool accessible to non-technical users, I created a flask app and deployed to heroku here: https://job-salary-predict.herokuapp.com. Users can just copy a full job description in data related fields and paste here to get the salary range.

### Project Roadmap
<img src="img/1.png">

### Understand Data
<img src="img/2.png">

### Output
<img src="img/3.PNG">
