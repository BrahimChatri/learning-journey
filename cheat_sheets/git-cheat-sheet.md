
# Git Cheat Sheet

## `git branch`
- `-r`: List remote-tracking branches
  ```sh
  git branch -r
  ```
- `-a`: List all branches
  ```sh
  git branch -a
  ```
- `-d`: Delete a branch
  ```sh
  git branch -d <branch-name>
  ```
- `-D`: Forcefully delete a branch
  ```sh
  git branch -D <branch-name>
  ```
- `-m`: Rename a branch
  ```sh
  git branch -m <old-branch-name> <new-branch-name>
  ```
- `--set-upstream-to`: Set upstream branch
  ```sh
  git branch --set-upstream-to=origin/<branch-name>
  ```

## `git checkout`
- `-b`: Create and switch to a new branch
  ```sh
  git checkout -b <branch-name>
  ```
- `-t`: Track a remote branch
  ```sh
  git checkout -t <remote>/<branch-name>
  ```
- `-f`: Force checkout, discarding local changes
  ```sh
  git checkout -f <branch-name>
  ```
- `-p`: Checkout specific parts of files
  ```sh
  git checkout -p <file>
  ```
- `--orphan`: Create a new branch with no history
  ```sh
  git checkout --orphan <branch-name>
  ```
- `--track`: Track a remote branch
  ```sh
  git checkout --track <remote>/<branch-name>
  ```
- `--no-track`: Do not set tracking information
  ```sh
  git checkout --no-track
  ```

## `git fetch`
- Fetch updates from the remote repository without merging.
  ```sh
  git fetch <remote>
  ```

## `git pull`
- Fetch and merge updates from the remote repository.
  ```sh
  git pull <remote> <branch>
  ```

## `git push`
- Push local commits to the remote repository.
  ```sh
  git push <remote> <branch>
  ```
- `-u`: Set upstream branch for future pushes/pulls.
  ```sh
  git push -u origin <branch>
  ```

## `git reset`
- `--soft`: Reset to a commit but keep changes in staging area.
  ```sh
  git reset --soft <commit>
  ```
- `--mixed`: Reset to a commit and update the staging area.
  ```sh
  git reset --mixed <commit>
  ```
- `--hard`: Reset to a commit and discard all changes in working directory.
  ```sh
  git reset --hard <commit>
  ```

## `git rm`
- Remove a file from the working directory and stage for commit.
  ```sh
  git rm <file>
  ```
- `-r`: Recursively remove a directory and its contents.
  ```sh
  git rm -r <directory>
  ```

## `git remote`
- `-v`: List remote URLs
  ```sh
  git remote -v
  ```
- `add <name> <url>`: Add a new remote repository
  ```sh
  git remote add <name> <url>
  ```
- `remove <name>`: Remove a remote repository
  ```sh
  git remote remove <name>
  ```
- `rename <old-name> <new-name>`: Rename a remote repository
  ```sh
  git remote rename <old-name> <new-name>
  ```
- `set-url <name> <url>`: Change the URL of an existing remote
  ```sh
  git remote set-url <name> <url>
  ```

## Deleting Remote Branches
- Delete a branch from the remote repository
  ```sh
  git push origin --delete <branch-name>
  ```

## SSH Key Management
- Generate a new SSH key:
  ```sh
  ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
  ```
- View the SSH key:
  ```sh
  cat ~/.ssh/id_rsa.pub
  ```


Certainly! Here are some additional Git commands with a summary format, which you can add to your cheat sheet:

# Additional Git Commands

## `git status`
- Display the state of the working directory and the staging area.
  ```sh
  git status
  ```

## `git log`
- Show the commit history for the current branch.
  ```sh
  git log
  ```
- `--oneline`: Display each commit as a single line.
  ```sh
  git log --oneline
  ```
- `--graph`: Show a text-based graphical representation of the branch and merge history.
  ```sh
  git log --graph
  ```
- `--author=<name>`: Filter commits by author.
  ```sh
  git log --author=<name>
  ```

## `git commit`
- Commit staged changes with a message.
  ```sh
  git commit -m "commit message"
  ```
- `-a`: Automatically stage files that have been modified and deleted.
  ```sh
  git commit -a -m "commit message"
  ```
- `--amend`: Amend the previous commit.
  ```sh
  git commit --amend
  ```

## `git merge`
- Merge changes from another branch into the current branch.
  ```sh
  git merge <branch-name>
  ```
- `--no-ff`: Create a merge commit even if the merge resolves as a fast-forward.
  ```sh
  git merge --no-ff <branch-name>
  ```

## `git rebase`
- Reapply commits on top of another base tip.
  ```sh
  git rebase <branch>
  ```
- `-i`: Interactive rebase, allows you to edit commits.
  ```sh
  git rebase -i <commit>
  ```

## `git tag`
- List tags.
  ```sh
  git tag
  ```
- Create a new tag.
  ```sh
  git tag <tag-name>
  ```
- Delete a tag.
  ```sh
  git tag -d <tag-name>
  ```

## `git stash`
- Save your local modifications to a stack.
  ```sh
  git stash
  ```
- Apply the most recently stashed changes.
  ```sh
  git stash apply
  ```
- List all stashed changes.
  ```sh
  git stash list
  ```

## `git diff`
- Show changes between commits, commit and working tree, etc.
  ```sh
  git diff
  ```
- `--cached`: Show changes between the index and the last commit.
  ```sh
  git diff --cached
  ```

## `git clean`
- Remove untracked files from the working directory.
  ```sh
  git clean -f
  ```
- `-d`: Remove untracked directories in addition to untracked files.
  ```sh
  git clean -fd
  ```

## `git config`
- Set a Git configuration value.
  ```sh
  git config <key> <value>
  ```
- `--global`: Apply the configuration globally.
  ```sh
  git config --global <key> <value>
  ```
- `--system`: Apply the configuration system-wide.
  ```sh
  git config --system <key> <value>
  ```

## `git archive`
- Create a tar or zip archive of files from a specific commit.
  ```sh
  git archive --format=tar --output=<archive-file> <branch>
  ```

## `git ls-files`
- Show information about files in the index and the working directory.
  ```sh
  git ls-files
  ```

## `git cherry-pick`
- Apply the changes introduced by some existing commits.
  ```sh
  git cherry-pick <commit>
  ```

## `git revert`
- Revert changes introduced by a commit by creating a new commit.
  ```sh
  git revert <commit>
  ```

