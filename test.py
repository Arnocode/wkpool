import json

# Load the JSON data from the uploaded file
with open('111.json', 'r') as file:
    data = json.load(file)

# Extract users data
users = data.get('users', {})

# Define the required scores fields
required_scores_fields = {"Achtste finales", "Finale", "Halve Finales", "Kwartfinales"}

# Find users without a complete scores object
incomplete_scores_users = [
    user_id for user_id, user_data in users.items()
    if not user_data.get('scores') or not required_scores_fields.issubset(user_data['scores'].keys())
]

# Find emails of users without a complete scores object
emails_of_incomplete_scores_users = [
    user_data['displayName'] for user_id, user_data in users.items()
    if user_id in incomplete_scores_users and 'email' in user_data
]

# Join emails with a semicolon
emails_string = "; ".join(emails_of_incomplete_scores_users)

# Print the count and email addresses
print(f"Number of users without a complete scores object: {len(emails_of_incomplete_scores_users)}")
print(f"Email addresses of users with incomplete scores object: {emails_string}")