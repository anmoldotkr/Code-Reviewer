# github_api.py

import requests
import os
from dotenv import load_dotenv


load_dotenv()




def fetch_pull_request_details(owner,repo_name):
    
    github_token = os.getenv('GITHUB_TOKEN')
    

    # GitHub API endpoint for fetching pull request details
    url = f"https://api.github.com/repos/{owner}/{repo_name}/pulls"


     # Make a GET request to the GitHub API with authentication
    response = requests.get(url, headers={"Authorization": f"token {github_token}"})


    # Make a GET request to the GitHub API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        pr_details = response.json()

        # Extract relevant information from the response
        return pr_details 
    else:
        # Print an error message if the request fails
        print(f"Failed to fetch pull request details. Status code: {response.status_code}")
        return None


def fetch_pull_request_number(owner,repo_name,pull_number):

  
    github_token = os.getenv('GITHUB_TOKEN')

    

    # GitHub API endpoint for fetching pull request details

    url = f"https://api.github.com/repos/{owner}/{repo_name}/pulls/{pull_number}"


     # Make a GET request to the GitHub API with authentication
    response = requests.get(url, headers={"Authorization": f"token {github_token}"})


    # Make a GET request to the GitHub API
    response = requests.get(url)
    print("Github Owner: ",owner)
    print("github Repo: ",repo_name)
    print("pull Request number: ",pull_number)

    # Check if the request was successful
    if response.status_code == 200:

        # Parse the JSON response 
        pr_details = response.json()
        print('-----------------')
        # print(pr_details)
        print('------------------')
       
        return pr_details
    else:
        # Print an error message if the request fails
        print(f"Failed to fetch pull request details. Status code: {response.status_code}")
        return None
    
