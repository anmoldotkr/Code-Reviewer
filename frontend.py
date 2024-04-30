
import streamlit as st
from gemini import gemeni_call

def parse_github_url(url):
    # Split the URL by '/'
    parts = url.split('/')

    # Extract the owner, repository name, and pull number from the URL
    owner = parts[3]
    repo_name = parts[4]
    pull_number = parts[6]

    return owner, repo_name, pull_number

def display():
    st.title('AI Code Reviewer')

    form = st.form(key='github_url_form')
    # Get the GitHub API URL from the user
    api_url = form.text_input('Enter the GitHub URL:')
    submit_button = form.form_submit_button('Parse URL')

    if submit_button:
        try:
            owner, repo_name, pull_number = parse_github_url(api_url)
            st.success(f"Owner: {owner}, Repository Name: {repo_name}, Pull Number: {pull_number}")


            # Display Gemini call result
            st.markdown(gemeni_call(owner, repo_name, pull_number))

        except IndexError:
            st.error("Invalid GitHub URL. Please enter a valid URL.")



def main():
    display()

if __name__ == "__main__":
    main()