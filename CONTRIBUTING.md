## Contributing
 
We're thrilled that you'd like to contribute to this project. Your help is essential for keeping it great. Please note we have a [Contributor Code of Conduct](CODE_OF_CONDUCT.md), please follow it in all your interactions with the project.

## Issues and PRs

If you have suggestions for how this project could be improved, or want to report a bug, open an issue! We'd love all and any contributions. If you have questions, too, we'd love to hear them.

We'd also love PRs. If you're thinking of a large PR, we advise opening up an issue first to talk about it, though! Look at the links below if you're not sure how to open a PR.

## Submitting a pull request
Following are the steps to guide you:

* Step 1: Fork the repo and Go to your Git terminal and clone it on your machine.
    ```
    git clone https://github.com/<your_github_username>/MindWave.git
    ```
* Step 2 Navigate to the project directory.
    ```
    cd MindWave
    ```
* Step 3: Add an upstream link to the main branch in your cloned repo
    ```
    git remote add upstream https://github.com/The-Data-Alchemists-Manipal/MindWave.git
    ```
* Step 4. Check the remotes for this repository.
    ```
    git remote -v
    ```
* Step 5: Keep your cloned repo up to date by pulling from upstream (this will also avoid any merge conflicts while committing new changes)
    ```
    git pull upstream main
    ```
* Step 6: Create your feature branch (This is a necessary step, so don't skip it)
    ```
    git checkout -b <branch-name>
    ```
* Step 7: Track and stage your changes.
    ```
     # Track the changes
     git status

     # Add changes to Index
     git add .
     ```
* Step 7: Commit all the changes (Write commit message as "Small Message")
    ```
    git commit -m "Write a meaningful but small commit message"
    ```
* Step 8: Push the changes for review
    ```
    git push -u origin <branch-name>
    ```
* Step 9: Create a PR on Github. (Don't just hit the create a pull request button, you must write a PR message to clarify why and what are you contributing)


## Best Practices for Pull Requests
To increase the likelihood of your pull request being accepted, please follow these best practices:

### Follow the coding style:
Ensure that your changes align with the established coding style used in this project.

### Write and update tests:
 Include tests that cover the functionality you are modifying or adding. If applicable, update existing tests to maintain code coverage.

### Keep changes focused:
 If you have multiple changes that are independent of each other, consider submitting them as separate pull requests. This allows for better review and easier integration.

### Write a good commit message:
 A well-written commit message is important for maintaining clear and concise commit history. Follow the guidelines outlined in this article to create informative commit messages.

### Work in Progress (WIP) pull requests:
 Feel free to submit work-in-progress pull requests to gather early feedback or when you encounter any obstacles. This allows the community to provide assistance and ensures that your contributions align with the project's goals.

We appreciate your contributions and look forward to reviewing your pull requests!
