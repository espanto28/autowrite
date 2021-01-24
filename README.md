# autowrite
This program will write articles for you. 

## Set up

The first step is to pip install the requirements.txt file

## Step 1: Scraper

The way it will work is that it will first scrape the internet and pull down articles.

You need to create a folder called "articles" and then create a text file with extentsion .txt.

The text file should contain a list of websites you want to scrape. Each website should separated by a newline. Add the full website URL.

The scraper is the scraper.py file. It will collect it from a list of websites you wish to download articles and store them in the "articles" folder. 


## Step 2: Train and generate

There are two main approaches I suggest. 

1.) Approach 1 - manually place all articles into 1 articles after extracting the text. 
2.) Approach 2 - read each text file and merge into 1 file. I find this approach tricky. 

Once you select a approach then I found best to predict every 20 words. Then predict the next 20 words. The solution loops where it takes the next 20 words and outputs another 20. 


Then pass them to a TF model for text generation.
