
#Here any one can download the .EXE file nad execute it to its local system.

Project Title7:  Digital PC Game Price Comparison Console Application with Secure Login (Using CheapShark API)
Problem Statement: Create a Python-based console application where users can log in and search for the latest prices of digital PC games from multiple stores (such as Steam, GreenManGaming, and Fanatical) using the CheapShark API. The application should include a secure login system, a password recovery option, and a limit on login attempts. After successful login, users can search for the latest deals on a specific game and view pricing data from various stores.

Requirements:
1. Login System:
•	User Credentials:
o	Store user credentials in a CSV file (users.csv) with fields like email, hashed password, and security_question.
o	Use password hashing (e.g., bcrypt) for secure storage and comparison of passwords.
•	Login Process:
o	The user is prompted to enter their registered email and password.
o	The system validates the credentials by comparing them with the data stored in the CSV file.

2. Input Validation:
•	Email Validation:
o	Ensure that the entered email follows a valid format (e.g., user@example.com).
•	Password Validation:
o	The password must meet the following criteria:
	At least 8 characters in length.
	Contains one uppercase letter, one lowercase letter, one number, and one special character.
o	The password input should be hashed for secure comparison with the stored hashed password.

3. Forgot Password:
•	Provide a "forgot password" option on the login screen.
•	Password Reset Process:
o	Prompt the user to enter their registered email.
o	If the email exists in the CSV file, ask the user to answer their security question correctly.
o	Upon answering the security question correctly, allow the user to reset the password (ensuring it meets the validation criteria).
o	Update the CSV file with the new hashed password.

4. Login Attempts:
•	Attempt Limitation:
o	Limit the user to 5 login attempts. After 5 failed attempts, prevent further login attempts until the application is restarted.
•	Security Measures:
o	Notify the user of how many login attempts remain after each failed login.
o	If the limit is exceeded, lock the user out and terminate the application.

5. API Integration (CheapShark API):
•	API Usage:
o	After a successful login, prompt the user to enter the name of a game for which they want to search for price comparisons.
o	Use the CheapShark API to fetch the latest prices and deals from various digital game stores like Steam, GreenManGaming, and Fanatical.
o	Display the following data for the game:
	Game Title: The name of the game.
	Store Name: The store offering the game (e.g., Steam, Fanatical).
	Normal Price: The regular price of the game.
	Sale Price: The discounted price of the game (if available).
	Savings: The percentage of savings compared to the normal price.
	Deal Rating: A score representing how good the deal is.
	Link to Store: URL to the store where the game is available.

![Screenshot 2024-10-03 175846](https://github.com/user-attachments/assets/018c351a-7534-4607-974c-576624822db5)
![Screenshot 2024-10-03 175941](https://github.com/user-attachments/assets/6c667ef5-3a28-40bd-9631-bd1bb416382a)

![Screenshot 2024-10-03 180113](https://github.com/user-attachments/assets/3fb54b59-e34b-4560-b0a5-d59b024447f1)

![Screenshot 2024-10-03 180101](https://github.com/user-attachments/assets/211c7845-37bf-4546-9c2b-8619743ccb0c)
![Screenshot 2024-10-03 180231](https://github.com/user-attachments/assets/70512f8a-65bd-4a08-8a9b-158ebecb849b)
