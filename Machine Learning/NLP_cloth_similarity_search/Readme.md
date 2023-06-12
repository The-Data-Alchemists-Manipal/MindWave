# Clothing Item Similarity

This project aims to find similar clothing items based on their descriptions using machine learning techniques. It collects and preprocesses data, measures similarity, and returns ranked results.

## Problem Statement

The problem is to develop a system that can find similar clothing items based on their descriptions. The system should collect data from multiple e-commerce websites, preprocess the text data, extract useful features, compute similarity between the input text and the database, and return a ranked list of similar item URLs.

## Solution

The solution involves the following steps:

1. **Collect and preprocess data:**
   - Web scrape multiple e-commercelike amazon , flipkart and nykaa fashion websites to gather clothing(Mens : Shirts,T-shirts , jeans  Womens : One Piece , Tops) item descriptions and their corresponding URLs.
   - To keep the datasets balance we have gathered equal amaount of entries from the above stated e-commerce websites.
   - Preprocess the text data by cleaning it, removing special characters, lowercasing, etc., and apply text normalization techniques like stemming or lemmatization.

2. **Measure similarity:**
   - Extracted useful features from the text descriptions using techniques like TF-IDF .
   - Implement a method to compute the similarity between the input text and the texts in the database using cosine similarity.

3. **Return ranked results:**
   - Designed a function that accepts a text string, extracts its features, computes similarities with the items in the database, ranks them based on similarity, and returns the URLs of the top-N most similar items.
   - 
notebook_link :- [Machine Learning/NLP_cloth_similarity_search/similarity_search.ipynb](https://github.com/shashank1623/MindWave/blob/main/Machine%20Learning/NLP_cloth_similarity_search/similarity_search.ipynb)

video_link : https://youtu.be/EUFEDruCOvM

I usally love feebacks and suggestion 
Contact Us:- shashankbhardwaj2030@gmai.com.


Thanks
❤️❤️❤️ shashank Bhardwaj(the_ghost) ❤️❤️❤️❤️
