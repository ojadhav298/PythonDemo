import requests
def main():
    # Print the welcome message
    print("Welcome to 2022")

    # Get user agent information
    user_agent = get_user_agent()
    print("User Agent:", user_agent)

def get_user_agent():
    try:
        # Send a GET request to a dummy website to retrieve user agent information
        response = requests.get("https://httpbin.org/user-agent")
        if response.status_code == 200:
            # Extract user agent information from the response
            user_agent = response.json()["user-agent"]
            return user_agent
        else:
            return "Failed to retrieve user agent information"
    except Exception as e:
        return "An error occurred while retrieving user agent information: " + str(e)

if __name__ == "__main__":
    main()


