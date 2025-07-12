# Using git

1) Command Line 
2) IDE/code editors like vscode
3) gui browser



- git -- version to see the version of the git
- git     see sll the commands of git


# Configuring git

- git config --global user.name "My name"
- git config --global user.email "someone@gmail.com"

there are many options
1) --local
2) --system
3) --global


git config --list     to see the config details



# init
- init is  used to create a new git repo

- git remote add origin <-link->
- git remote -v   to verify origin
- git branch     to check the branch
- git branch -M main   to rename the branch
- git push origin main




# Creating a new repo and using it


- generate a new token from the website>settings>devops  and then use the following command

token for 30 days
- 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

command i ran to initialize new repo
```shell
$ curl -H "Authorization: token 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" \
     -d '{"name": "repo1", "private": false, "auto_init": true}' \
     https://api.github.com/user/repos
```


note the error of parsing the json file is due to use of single quote and double quotes so keep the single quote outside and double quotes inside 

init is  used to create a new git repo

- git remote add origin <-link->
- git remote -v   to verify origin
- git branch     to check the branch
- git branch -M main   to rename the branch
- git push origin main



## some error 

Haarit@LAPTOP-3S72LHSI MINGW64 /d/Obsidian (main)
$ git push origin main
To https://github.com/haarit19058/Obsidian
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'https://github.com/haarit19058/Obsidian'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. If you want to integrate the remote changes,
hint: use 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

Haarit@LAPTOP-3S72LHSI MINGW64 /d/Obsidian (main)
$ git pull origin main --allow-unrelated-histories
From https://github.com/haarit19058/Obsidian
 * branch            main       -> FETCH_HEAD
Merge made by the 'ort' strategy.
 README.md | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
## Origin in git

No, the term "origin" in Git does not represent a folder on your local machine. Instead, "origin" is just a conventionally used name for a remote repository. 

When you run the command `git remote add origin <repository_url>`, you are telling Git to associate the provided URL with the name "origin" in your local repository's configuration. This allows you to refer to the remote repository by the name "origin" in your Git commands.

The remote repository itself is not stored on your local machine as a folder. It exists on a remote server, such as GitHub, GitLab, or a private server. The "origin" name serves as a convenient label for you to interact with that remote repository from your local machine.











token for 23110077

```python
	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
```
