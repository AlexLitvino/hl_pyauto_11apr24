## git commands
 
git init - initialize local repository  
git clone <url> - clone a remote repository locally  
git add - add files to index  
git commit -m <commit message> - add files to local repository (option -a performs git add *)
git push - add files from a local repository to remote repository  
git branch - work with branches  
git checkout [-b] <branch name> - switch to existing local branch (option -b creates new branch and switches to it)
git fetch - get changes from a remote repository to local repository
git pull (git fetch + git merge) - get changes from a remote repository and merge to local
git merge <branch name> - move changes from specified branch to current (non-linear history)
git rebase <branch name> - move changes from specified branch to current (linear history)
git merge --squash <branch_name_we_want_to_merge> - creating one common commit after merge
git rebase -i HEAD~<N> - combines last N commits into one commit 
git status - check status of local repository  

git tag - work with tags  
git cherry-pick <commit hash> - merge a specific commit from another branch to current branch  
git diff - shows difference between commits or commit and current state  
git log - shows log  
git revert <commit hash> - revert commit with creating new commit
git reset [--soft | --mixed | --hard] <commit hash> - resets repo state to commit with removing/reserving your changes

git config --local user.email <email>
git config --local user.name <username>
git config --list

git config --local credential.helper store