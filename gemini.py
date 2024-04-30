

import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
from github_api import fetch_pull_request_number, fetch_pull_request_details


load_dotenv()




def gemeni_call(owner, repo_name, pull_number):


    GOOGLE_API_KEY = os.getenv('GEMINI_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-pro')

    # fetch pull request number
    pr_details = fetch_pull_request_number(owner,repo_name,pull_number)

    latest_pr_details = fetch_pull_request_details(owner,repo_name)

    # convert result into json format
    result_pr_details_json = json.dumps(pr_details)
    result_latest_pr_details_json = json.dumps(latest_pr_details)
    
    response = model.generate_content(f'${pr_details} Review all changes suggest changes and provide feedback')


     # Extract generated text from the response
   
    generated_text = response.candidates[0].content.parts[0].text
    actaul_text= generated_text.strip()
    return actaul_text
 

