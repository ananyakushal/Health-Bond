import os
import google.generativeai as genai

genai.configure(api_key = 'AIzaSyDmLQuUp2Rxi0_5U6EtExfERczih72he_c')

model = genai.GenerativeModel('gemini-pro')

def get_keywords(input_text) :
	response = model.generate_content(f"list out all the important keywords from the given text and return them in a comma seperated form : {input_text}")

	list_of_keywords = response.text.split(',')
	return list_of_keywords

# def right_or_wrong(input_text) :
# 	response = model.generate_content(f"check whether the info shared here is an assertive statement and if yes then tell whether it is right or not , answer in yes or no strictly , no other answer is allowed : {input_text}")

# 	print(response.text)
