<p align="center"><img src="AmazonLogo.png"></p>

# **Amazon Games Recommender**  
## Description  

A Recommender system based of Video Games from Amazon.com

## Table of Contents
[1. Background & Motivation](#Background&Motivation)<br>
[2. Data Source](#DataSource)<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2a. About The Data](#data)<br>
[3. Exploratory Data Analysis](#EDA)<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3a. Top 10 Popular Platforms](#3a)<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3b. Top 10 Popular Brands](#3b)<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3c. Top 10 Most Popular Product Types](#3c)<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3d. Number of Ratings Posted](#3d)<br>
[4. Recommender](#Recommender)<br>
[6. Future Plans](#FuturePlans)<br>
[7. Dependencies](#Dependencies)<br>
[8. Contact](#Contact)<br>

## <a id="Background&Motivation">Background & Motivation</a>
The video game industry is valued at billions of dollars and is expected to be worth over 90 billion USD within 2020. The world is estimated to have more than 2.5 billion video gamers and is expected to grow even more. With so many types of consoles, videogames, and accessories, there are so many products to choose from. With data of videogames and their reviews from Amazon, I wanted to create a recommender that would help gamers and enthusaists find products that would be similar to their preferences. Developing a recommender in hopes to encourage more sales and enjoyment for both sellers and buyers is my main goal.

---
## <a id="DataSource">DataSource</a>
http://deepyeti.ucsd.edu/jianmo/amazon/index.html

### <a id="data">2a. About the Data</a>
meta_Video_Games.json:  
(84893 Rows, 12 Columns):  
|- category  
|- title         
|- image          
|- brand         
|- rank          
|- main_cat      
|- asin          
|- description   
|- also_buy        
|- also_view       
|- price           
|- feature            

Video_Games.json:  
(2565349 Rows, 12 Columns):
|- overall          
|- verified          
|- reviewTime      
|- reviewerID      
|- asin            
|- reviewerName    
|- reviewText      
|- summary         
|- unixReviewTime   
|- vote            
|- style           
|- image           

---
## <a id="EDA">Exploratory Data Analysis</a>
### <a id="3a">3a. Top 10 Popular Platforms</a>

PC games and accessories are very prominent in Amazon's marketplace. With 23288 items
specifically for PC, and only 3517 items specifically for the Wii. 3567 items we not given a
specific description on which console their item is for.
<p align="center"><img src="Graphs/1. Top 10 Popular Platforms.png"></p>


### <a id="3b">3b. Top 10 Popular Brands</a>

Surprisingly, 4030 video game items did not have a brand included. We can see that Nintendo
is the most well known brand with 3429 items connected to Nintendo. There are 7779 unique brands listed video game items on Amazon.
<p align="center"><img src="Graphs/2. Top 10 Popular Brands.png"></p>


### <a id="3c">3c. Top 10 Most Popular Product Types</a>

Out of all the products, 52633 are video games. 23687 are mounts, and only 532 are video game figures.
<p align="center"><img src="Graphs/3. Top 10 Most Popular Product Types.png"></p>

### <a id="3d">3d. Number of Ratings Posted</a>

A staggering amount of 1487366 reviews gave 5 stars. 311891 reviewers were gave 1 star.
<p align="center"><img src="Graphs/4. Number of Ratings Posted.png"></p>

<!--a id="3e">3e. Number of Ratings Posted -need to fix-</a>
<p align="center"><img src="Graphs/Number of Ratings Posted.png"></p-->

--
## <a id="Recommender">Recommender System</a>
To run project:  
```python Recommender.py```  
This will take a while to run. (estimated 10 mins)
  
  
Following will be prompted once it finishes compiling:
```
Please Enter a Number From the Following: 
1. Recommendations based on asin rating
2. Recommendations based on asin description
3. Enter your own description
(q to quit)
Enter choice of number: 
```  
1 - Will allow you to enter a valid asin number. It will recommend other products that similar users rated and bought. If the asin is not valid, an error message will appear.
  
2 - Will allow you to enter a valid asin number. It will recommend other products similar to the asin's description. If the asin is not valid, an error message will appear.
  
3 - Will allow you to enter your own description and recommend products based on your description.

### Examples
#### Recommendations based on asin Ratings
`Enter choice of number: 1`  
You will then be prompted with the following message:
`Enter an asin (q to quit): `  
Entering q or Q will go back to the main menu. Inputing an invalid asin value will output an wanring message and return back to the main menu. Inputting a valid asin will return top 10 recommended itmes for you.  
`Enter an asin (q to quit): `

  
  
#### Recommendations based on asin Description  
`Enter choice of number: 2`  
You will then be prompted with the following message:  
`Enter an asin (q to quit): `  
Entering q or Q will go back to the main menu. Inputing an invalid asin value will output an wanring message and return back to the main menu. Inputting a valid asin will return top 10 recommended itmes for you.  
`Enter an asin (q to quit): `  
  
  
#### Recommendations based on own description
`Enter choice of number: 3`  
You will then be prompted with the following message:  
`Enter a description: `  
Input a nonempty description and   
`Enter a description: playstation 4 controllers`  
Wait for the program to run, and then you'll get your recommendations!  
  

This recommender has an RMSE of 1.03

Thank you for taking a look at my recommender! If you enjoyed this project or have any questions, feel free to [contact me!](#Contact)


---
## <a id="FuturePlans">Future Plans</a>
1. Find a better way to handle cold starts.
2. Create a flask app to have project on

---
## <a id="Dependencies">Dependencies</a>
Python,
Pandas,
Matplotlib,
scikit-learn,
surprise,
Jupyter Notebook

---
## <a id="Contact">Contact</a>
Feel free to contact me about any questions. I can be reached through these links.  
[LinkedIn](https://www.linkedin.com/in/winrichsy/)  
[Email](winrichsy@gmail.com)  
