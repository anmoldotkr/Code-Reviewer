
---

# AI CODE REVIEWER

## Overview

This project is an AI code reviewer tool designed to streamline the code review process using natural language processing techniques. It integrates with GitHub to fetch pull request details and provides code review suggestions using the Google Generative AI (Gemini) API.

## How It Works

1. **GitHub Integration**:
   - The `github_api.py` module contains functions to interact with the GitHub API.
   - It fetches pull request details and extracts relevant information such as the owner, repository name, and pull number.

2. **Gemini Integration**:
   - The `gemini.py` module utilizes the Google Generative AI (Gemini) API for natural language generation.
   - It generates code review suggestions based on the pull request details obtained from GitHub.

3. **Frontend**:
   - The `frontend.py` script provides a user interface built using Streamlit.
   - It prompts the user to enter a GitHub URL containing a pull request.
   - Upon submission, it parses the URL, fetches pull request details using `github_api.py`, and generates code review suggestions using `gemini.py`.

## Files

- **github_api.py**:
  - Contains functions to interact with the GitHub API.
  - Provides functionality to fetch pull request details based on a given GitHub URL.

- **gemini.py**:
  - Utilizes the Google Generative AI (Gemini) API for natural language generation.
  - Generates code review suggestions based on the provided pull request details.

- **frontend.py**:
  - Implements the user interface using Streamlit.
  - Parses GitHub URLs entered by the user and fetches pull request details.
  - Integrates with `github_api.py` and `gemini.py` to generate code review suggestions.

- **.env**:
  - This file contains environment variables used in the project.
  - It should include the following variables:
    - `GITHUB_TOKEN`: Your GitHub token for authentication.
    - `GEMINI_API_KEY`: Your Gemini API key.

## Authentication

- **GitHub Token**:
  - A GitHub token is required to authenticate requests to the GitHub API. It is stored as an environment variable (`GITHUB_TOKEN`) in the .env file.

- **Gemini API Key**:
  - The Gemini API key is required to authenticate requests to the Google Generative AI API. It is stored as an environment variable (`GEMINI_API_KEY`) in the .env file.

## Usage

1. Install the required dependencies using `pip install -r requirements.txt`.
2. Set up your environment variables in the .env file.
3. Run the `frontend.py` script to launch the Streamlit application.
4. Enter a GitHub URL containing a pull request and click "Parse URL" to generate code review suggestions.

---
