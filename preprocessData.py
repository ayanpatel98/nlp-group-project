# This file is for preprocessing the youtube transcripts.

import pickle
import re
import pandas as pd


maximum_subtitle_len_threshold = 700
minimum_subtitle_len_threshold = 100


def preprocess(subtitle, dict):
    processed_subtitle = re.sub(r"\[.*?\]", "", subtitle)
    processed_subtitle = processed_subtitle.replace("THIS IS A TEST", "")
    processed_subtitle = processed_subtitle.replace("THIS IS A CAPTIONS TEST", "")
    processed_subtitle = re.sub(r'\W+', ' ', processed_subtitle).strip()
    subtitle_words = processed_subtitle.split()
    processed_subtitle_words = []
    for word in subtitle_words:
        if word.lower() in dict:
            processed_subtitle_words.append(word)
    
    return " ".join(processed_subtitle_words)


# create dictionary from glove file
file = open("glove.6B.100d.txt", 'r',errors='ignore')
Lines = file.readlines()
file.close()
gloveDict = set()
for line in Lines:
    values = line.split()
    word = values[0]
    gloveDict.add(word)

processed_dataset = []

with open('YoutubeData_668.pkl', 'rb') as file:
    data = pickle.load(file)
    for i in range(len(data["Subtitles"])):
        new_subtitle = preprocess(data["Subtitles"][i], gloveDict)
        if len(new_subtitle.split()) <= maximum_subtitle_len_threshold and len(new_subtitle.split()) >= minimum_subtitle_len_threshold:
            processed_dataset.append([data["Video_ID"][i], new_subtitle])


processed_data = pd.DataFrame(processed_dataset,columns=['Video_ID','Subtitles'])

with open("preprocessed_YoutubeData_668.pkl", "wb") as f:
    pickle.dump(processed_data, f)

    


