# this file is for combining all of the RACE dataset files into one JSON file

import numpy as np
import os
import json

with open("RACE_GPT2.json", "w") as outfile:
    for file in os.listdir('/Users/veyond-metaverse/cs544/project/RACE/train/high'):
        with open(f"/Users/veyond-metaverse/cs544/project/RACE/train/high/{file}", "r") as file:
            text = file.read()

        data = json.loads(text)
        len_of_question = len(data["questions"])

        completion_text = ""

        for i in range(len_of_question):
            text = f"""{data['questions'][i]} 
A. {data['options'][i][0]}
B. {data['options'][i][1]}
C. {data['options'][i][2]}
D. {data['options'][i][3]}
Answer = {data['answers'][i]}

"""
            completion_text += text


        data_point = {
                    "prompt" : data["article"],
                    "completion" : completion_text
                }
        print("completition_text:",completion_text)

        json.dump(data_point, outfile)