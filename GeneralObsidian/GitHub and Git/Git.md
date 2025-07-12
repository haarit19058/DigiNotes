It is a free and open source version control system.
It does track changes for developers and coders. Makes checkpoints of the code.
```c
cout<<endl
```




# Some of the important commands

## git config --list
- To see all the details of the user
## Changing the associated email

To change the email address associated with your Git user, you can use the following command:

```bash
git config [--global] user.email "your_new_email@example.com"
```

Replace `"your_new_email@example.com"` with your desired email address.

If you include the `--global` flag, it will change the email address globally for all repositories on your system. If you omit the `--global` flag, it will only change the email address for the current repository.

Here are the commands to change the email address:

1. **Changing globally** (for all repositories):
   ```bash
   git config --global user.email "your_new_email@example.com"
   ```

2. **Changing for the current repository**:
   ```bash
   git config user.email "your_new_email@example.com"
   ```

After running the appropriate command, Git will update the email address associated with your user. You can verify the change by running `git config --get user.email` to confirm that the new email address has been set.




## Add remote repo from bash

token for 30 days
- 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

command i ran to initialize new repo
```shell
$ curl -H "Authorization: token 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" \
     -d '{"name": "repo1", "private": true, "auto_init": true}' \
     https://api.github.com/user/repos
```


curl -H "Authorization: token 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" -d '{"name": "repo1","private": true, "auto_init": true}'  https://api.github.com/user/repos



If you want to create a remote repository directly from the command line (Bash), you can achieve this using the GitHub API or through Git command-line tools like `curl`. Here's how you can create a repository on GitHub via the command line:

1. **Generate a Personal Access Token**:
   To authenticate with GitHub's API, you'll need a personal access token. Go to your GitHub settings, navigate to "Developer settings" -> "Personal access tokens", and generate a new token with the necessary permissions (typically repo).

2. **Create the Repository**:
   Use `curl` to send a POST request to GitHub's API endpoint for creating repositories. Replace `<TOKEN>` with your personal access token and `<REPO_NAME>` with the name of your repository:

```bash
curl -H "Authorization: token <TOKEN>" \
     -d '{"name": "<REPO_NAME>", "private": false, "auto_init": true}' \
     https://api.github.com/user/repos
```

This command will create a new public repository named `<REPO_NAME>` under your GitHub account.

3. **Verify the Repository Creation**:
   Once the command is executed, you should see a JSON response containing information about the newly created repository.

This method allows you to create a remote repository programmatically from the command line without needing to use the GitHub web interface. However, be sure to replace `<TOKEN>` with your personal access token and `<REPO_NAME>` with the desired name of your repository.


## Initialize

The error message you're seeing indicates that Git doesn't know where to push the changes because no remote repository has been configured.

Here's how you can resolve this issue:

1. **Add a remote repository**: If you haven't already added a remote repository, you need to do so. You can add a remote repository using the following command:

    ```bash
    git remote add origin <remote_repository_URL>
    ```

    Replace `<remote_repository_URL>` with the URL of the remote repository where you want to push your changes. You can name the remote "origin" or any other name you prefer.

2. **Push to the remote repository**: After adding the remote repository, you can push your changes to it using the following command:

    ```bash
    git push -u origin <branch_name>
    ```

    Replace `<branch_name>` with the name of the branch you want to push. If you're working on the "main" branch, replace `<branch_name>` with "main". The `-u` option sets the upstream branch for the current branch, so you won't need to specify the remote and branch name next time you push.

If you've already added a remote repository but forgot to specify it in the `git push` command, you can push to it directly:

```bash
git push origin <branch_name>
```

Replace `<branch_name>` with the name of the branch you want to push. If you're working on the "main" branch, replace `<branch_name>` with "main".

## What url should look like

The URL you provide when adding a remote repository depends on where your repository is hosted.

Here are some examples of remote repository URLs for different hosting services:

1. **GitHub**:
   If your repository is hosted on GitHub, the URL should look like:
   ```
   https://github.com/username/repository.git
   ```

   Replace `username` with your GitHub username and `repository` with the name of your repository.

2. **GitLab**:
   For repositories hosted on GitLab, the URL format is similar to GitHub:
   ```
   https://gitlab.com/username/repository.git
   ```

   Replace `username` with your GitLab username and `repository` with the name of your repository.

3. **Bitbucket**:
   Bitbucket repositories have URLs like:
   ```
   https://bitbucket.org/username/repository.git
   ```

   Replace `username` with your Bitbucket username and `repository` with the name of your repository.

4. **Self-hosted or other Git hosting services**:
   If you're using a self-hosted Git server or a different Git hosting service, the URL format may vary. You'll typically use either HTTPS or SSH URLs. For example:

   - HTTPS:
     ```
     https://example.com/username/repository.git
     ```

   - SSH:
     ```
     git@example.com:username/repository.git
     ```

   Replace `example.com` with the domain of your Git server, `username` with your username, and `repository` with the name of your repository.

Make sure to use the correct URL for your specific hosting service and repository location. If you're unsure about the URL, you can usually find it on the webpage of your repository on the hosting service's website.



# Notes continued


Git commands
 1) clone --> bring a repository that is hosted on github into a folder on local machine.
 2) add-->Track your files and changes in Git
 3) commit-->Save your files in git
 4) push-->Upload git commits to a remote repo, like github
 5) pull--> Download changes from remote repo to your local machine, the opposite of push
 
6) status-->shows all the files that are updated deleted or created.
7)  .git in the directory records all the changes.


Untracked files and tracked files.
use of period


git add .  --> to add all the files under tracking
git status/show  gives all the info regarding the files.

git commit -m "a" -m "arg2" filename   -m des //first -m gives the message to commit ; second -m  is used to give the description

git push --> to upload on remote github



git ssh keys
git works on Openssl

git clone "repo link"

TO work on a repository we have to move to the repo folder and then you can make change, commit etc.



for ssh to work properly we need to make user keys with email id.

works like keys are needed to transfer the data. 
testkey and testkey.pub

On github we can see the keys that we have uploaded. Or automatically configured.

Remember that while working with linux we need to upload the ssh keys on github to work it properly. Explore that part whenever necessary.




 git push origin main/(master)
 origin is an option that sets the location of a git repo
 master/main is the name of the branch we want to work on


starting a repo locally.
make a folder and move into it.

git push origin main  //This is necessary because if we dont set it the  an error will occur becuz git won't know where to push the file.   

git init  //to initialize a repository 
git add file
git commit -m "created readme" -m "nothing special"

git remote -v  // gives all the remote repositories that is connected to the repo

Shortcut :
git push -u origin main // set upstream so that we dont have to type it every time.

Note that by commiting the changes git automatically adds it.



Git Branching
git branch //to see all the branches
git checkout  -b "new branch" // to make a new branch 
git checkout  branchname // to switch between branches.
hit tab to autocomplete

Write your code in a readable way.

git merge main// to merge the codes of different branches

while working in the another branch use
use merge master //to merge with main branch.

git diff nameofthebranch // merge and compare what changes are being done like + or -

PULL request
when we want to merge our branch to the main branch.
we can add comment to our pull request and even on any particular branch.

git pull // to get the pull request edits.
git branch -d nameofthebranch //to delete the branch.


git commit -am "adds and commits simultaneously" //only works on the master file.



Undoing something on git.

git reset // gives the file of unstaged files
git reset filename // to redo the changes
git reset HEAD~1 // head refers to the last commit and tilde refers to the number of stages i want to go back to.

git log // see the log of all commits 

copy the unique hash and use to go back to that particular commit

git reset <hash of the commit] //moning bak to a particular commit.

git reset <hash of  the commit] --hard // to completely remove the changes.


Forking in git

get the complete code to your own repo





