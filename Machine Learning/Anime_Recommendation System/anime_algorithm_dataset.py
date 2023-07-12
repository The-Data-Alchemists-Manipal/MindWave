
import numpy as np
import pandas as pd 
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#DATA COLLECTION & PRE-PROCESSING

anime_data=pd.read_csv(r'D:\Users\User\Downloads\mal_top2000_anime.csv') #load the dataset 
anime_data.head()

#Data Cleaning 
anime_data=anime_data.rename(columns={'Unnamed: 0':'Index'})
print(anime_data)
anime_data.shape

#selecting preferred features 
anime_data['Score'] = anime_data['Score'].astype(str)
selected_features = ['Score','Genres','Demographic','Theme(s)']
print(selected_features)
for feature in selected_features:
    anime_data[feature] = anime_data[feature].fillna('')
    
combined_feature = anime_data['Score']+' '+anime_data['Genres']+' '+anime_data['Demographic']+' '+anime_data['Theme(s)']
print(combined_feature)

#converting text data to feature vectors 
#creation of an instance 
vectorizer= TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_feature)
print(feature_vectors)

#COSINE SIMILARITY

#getting similarity scores using cosine similarity
similarity = cosine_similarity(feature_vectors)
print(similarity)
print(similarity.shape)

#testing user input for the system 
#USER INPUT FOR ANIME
anime_name = input('Enter your favorite Anime:')

#creating a list with all anime names from the dataset 
list_anime_titles = anime_data['Name'].tolist()

# find the closest match for the anime provided by the user 
find_cl_match = difflib.get_close_matches(anime_name,list_anime_titles)
print(find_cl_match)

close_match = find_cl_match[0]
print(close_match)

#finding the index of anime with the title 
index_of_anime = anime_data[anime_data.Name == close_match]['Index'].values[0]
print(index_of_anime)

#getting a list of similar anime 
similarity_score = list(enumerate(similarity[index_of_anime]))
print(similarity_score)

len(similarity_score)
#sorting anime based on their similarity score
sorted_similar_anime = sorted(similarity_score , key =lambda x:x[1], reverse= True)
print(sorted_similar_anime)

#Creation of Anime Recommendation System 
anime_name = input('Enter your favorite Anime:')
list_anime_titles = anime_data['Name'].tolist()
find_cl_match = difflib.get_close_matches(anime_name,list_anime_titles)
close_match = find_cl_match[0]
index_of_anime = anime_data[anime_data.Name == close_match]['Index'].values[0]
similarity_score = list(enumerate(similarity[index_of_anime]))
sorted_similar_anime = sorted(similarity_score , key =lambda x:x[1], reverse= True)
print('Anime Suggested for you :) \n')

i=1
for anime in sorted_similar_anime:
    Index=anime[0]
    title_from_index = anime_data[anime_data.Index==Index]['Name'].values[0]    # fOR loop to find the recommended anime which will display the name and demographic of the anime to the user 
    demog_from_index = anime_data[anime_data.Index==Index]['Demographic'].values[0]
    if(i<20):           #i<20 will give 20 anime recommendations 
        print(i,'.',title_from_index, ([demog_from_index]))
        i+=1

#GUI CREATION FOR ANIME RECOMMENDATION SYSTEM # 

#to give the user a better experience 
import tkinter as tk
from tkinter import messagebox
import difflib
from PIL import ImageTk, Image


#create Tkinter GUI 
root=tk.Tk()
root.title("Anime Recommendation System")
root.configure(bg="#222222")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1,weight=1)






#define styling
title_font=("Arial",16,"bold")
root.option_add("*Font",title_font)

#define styling for labels
label_font=("Arial",12,"bold")
entry_font=("Arial",12)
button_font=("Arial",12,"bold")
button_bg="#3366CC"
button_fg="#FFFFFF"
button_active_bg="#25476D"
button_active_fg="#FFFFFF"

#create a canvas widget and set the bg image
try:
    bg_image=Image.open(r"D:\Users\User\Downloads\ani.gif")
    bg_image=bg_image.resize((1300,600),Image.ANTIALIAS)
    root.background=ImageTk.PhotoImage(bg_image)
    
    #create a canvas widget and place the bg on it
    canvas=tk.Canvas(root, width=900, height=400)
    canvas.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")
    canvas.create_image(0,0,anchor=tk.NW,image=root.background)
except IOError:
    messagebox.showerror("Error","failed to load background image.")
    
    
#Create GUI elements - label for anime name input 
name_label=tk.Label(root,text="Enter Anime Name:")
name_label.grid(row=0, column=0,padx=10,pady=10,sticky="w")




#create the entry field
entry = tk.Entry(root, font=entry_font)
entry.grid(row=0, column=1, padx=10, pady=10 , sticky="ew")



def get_recommendations():
    anime_name=entry.get()
    

#find closest match in the anime dataset
    list_anime_titles = anime_data['Name'].tolist()
    find_cl_match = difflib.get_close_matches(anime_name, list_anime_titles)
    if find_cl_match:
        close_match = find_cl_match[0]
        index_of_anime = anime_data[anime_data.Name == close_match]['Index'].values[0]

        # Compute similarity scores
        similarity_score = list(enumerate(similarity[index_of_anime]))
        sorted_similar_anime = sorted(similarity_score , key=lambda x: x[1], reverse=True)

        # Generate recommendations
        recommendations = []
        for i, anime in enumerate(sorted_similar_anime):
            if i < 20:
                Index = anime[0]
                title_from_index = anime_data[anime_data.Index == Index]['Name'].values[0]
                demog_from_index = anime_data[anime_data.Index == Index]['Demographic'].values[0]
                recommendations.append(f"{i+1}. {title_from_index} {demog_from_index}")
      
        messagebox.showinfo("Anime Recommendations For You :)","\n".join(recommendations))
    
    else:
        messagebox.showinfo("Anime Recommendations For You","No match found :(")

button = tk.Button(root, text="Get Recommendations",font=button_font, bg=button_bg, fg=button_fg,activebackground=button_active_bg, activeforeground=button_active_fg, command=get_recommendations)
button.grid(row=1, column=0 , padx=10 ,pady=10, sticky="ew")




#start the event loop
root.mainloop()

    
    

