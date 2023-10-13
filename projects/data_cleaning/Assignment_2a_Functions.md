# Assignment 2a: Refactor with Functions and Collaboration via GitHub

## Objective:
In this module, your task is to begin refactoring the script that is in your GitHub repository. You will encapsulate distinct functionalities within functions to enhance the code’s modularity and readability. Additionally, practice collaborative coding by reviewing the code of your peers.

## Steps:

### Part A: Refactor Code

1. **Create Functions for Distinct Tasks:**
    - **Range Cleaning Function:**
        - Should accept a pandas Series, a minimum, and a maximum value.
        - Return a cleaned pandas Series with values outside the range set to np.nan.
    - **Spike Checking Function:**
        - Should accept a pandas Series and a max_jump value.
        - Return a Series with abrupt spikes set to np.nan.
    - **Flat Period Checking Function:**
        - Should accept a pandas Series and a n_flat value.
        - Return a Series with flat periods set to np.nan.
    - **Plotting Function:**
        - Accept two pandas Series: original and cleaned 
        - Should plot values and clearly mark outliers

2. **Comment Your Code:**
    - Ensure each function and logical block of code short and precise comment to explain the purpose and operation of your code.

3. **Test Locally:**
    - Run the refactored script locally to ensure each function is working as expected.

4. **Commit and Push:**
    - Commit your changes with a clear commit message.
    - Push the changes to your GitHub repository.

### Part B: Collaboration and Peer Review

1. **Code Review:**
    - You will be assigned two peers’ repositories to review.
    - Examine their code and provide constructive feedback via GitHub's pull request review features.

2. **Implement Feedback:**
    - Review feedback from your peers on your own code.
    - Make necessary adjustments and improvements to your code based on the feedback.

## Submission:

1. **Pull Request:**
    - Open a pull request if you worked on a different branch.
    - Provide a comprehensive description explaining your code changes, decisions, and any challenges encountered and how you overcame them.

2. **Peer Review:**
    - Complete the review of assigned peers’ pull requests.
    - Provide feedback and suggestions for improvement.

3. **Implement Feedback:**
    - Revise your code according to the feedback received, commit the changes, and update the pull request.

## Evaluation:

- **Code Refactoring (40%):** The refactored code should be modular, with distinct functions performing specific tasks, and be more readable and maintainable.
- **Commenting and Documentation (20%):** The code should be well-commented, explaining complex or unclear code sections. Functionality and usage of each function should be clear.
- **Collaboration and Peer Review (30%):** Timely and constructive feedback should be provided on peers’ pull requests, and feedback received should be well-implemented.
- **Commit and Push Quality (10%):** Commits should be regular with clear, descriptive messages, and the final code should be pushed to GitHub before the deadline.

## Deadline:
- Refactored code should be pushed, and pull requests opened by [specific date and time].
- Peer reviews should be completed, and feedback implemented by [specific follow-up date and time].

Embark on this journey of collaborative learning, enhance your coding, and review skills, and work towards a cleaner, more efficient time series data cleaning script. Happy coding!