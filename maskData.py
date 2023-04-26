import pickle
import pandas as pd

def maskSubtitle(subtitle):
    subtitle_length = len(subtitle.split())
    num_words_to_mask = subtitle_length // 4
    masked_subtitle_1_arr = []
    masked_subtitle_2_arr = []
    masked_subtitle_3_arr = []

    subtitle_arr = subtitle.split()
    i = 0
    for word in subtitle_arr:

        if i < num_words_to_mask:
            masked_subtitle_1_arr.append("<mask>")
            i+=1
        else:
            masked_subtitle_1_arr.append(word)
    
    i = 0
    for j in range(len(subtitle_arr), -1, -1):
        if i < num_words_to_mask:
            masked_subtitle_2_arr = ["<mask>"] + masked_subtitle_2_arr
            i += 1
        else:
            masked_subtitle_2_arr = [subtitle_arr[j]] + masked_subtitle_2_arr

    i = 0
    mask_round = True
    for word in subtitle_arr:
        if i < num_words_to_mask:
            if mask_round:
                masked_subtitle_3_arr.append("<mask>")
                mask_round = False
            else:
                masked_subtitle_3_arr.append(word)
                mask_round = True
        else:
            masked_subtitle_3_arr.append(word)
   
    
    return " ".join(masked_subtitle_1_arr), " ".join(masked_subtitle_2_arr), " ".join(masked_subtitle_3_arr)

masked_dataset = []

with open('preprocessed_YoutubeData_668.pkl', 'rb') as file:
    data = pickle.load(file)
    for i in range(len(data["Subtitles"])):
        masked_subtitle_1, masked_subtitle_2, masked_subtitle_3 = maskSubtitle(data["Subtitles"][i])
        masked_dataset.append([data["Video_ID"][i], [masked_subtitle_1,masked_subtitle_2,masked_subtitle_3],data["Subtitles"][i] ])

masked_data = pd.DataFrame(masked_dataset,columns=['Video_ID','Masked_Subtitles','Subtitles'])

with open("masked_YoutubeData_668.pkl", "wb") as f:
    pickle.dump(masked_data, f)
