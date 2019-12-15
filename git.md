
# <h1> GIT Topics






# <h2> What is Git? 

GIT is an opensource distributed version control system and source code management system.



# <h2> What is the difference between Git and Github?
Git is the version control system that tracks changes in the source code.
It aides in co-ordinating work among programmers and can track in any set of files.

Github is repository hosting service. It provides more features like GUI, access control and several collaboration features.


# <h2> What is a repository in Git?
Repository in Git is a place where Git stores all the files. Git can store the files either on the local repository or on the remote repository.


# <h2> How can you create a repository in Git?
“git init”


# <h2> What is ‘bare repository’ in Git?
A “bare” repository in Git contains information about the version control and no working files (no tree) and it doesn’t contain the special .git sub-directory.

 whereas the working directory consists of :
 
A .git subdirectory with all the Git related revision history of your repository.
A working tree, or checked out copies of your project files.



# <h2> What is a ‘conflict’ in git?

Git can handle on its own most merges by using its automatic merging features. There arises a conflict when two separate branches have made edits to the same line in a file, or when a file has been deleted in one branch but edited in the other.



# <h2> In Git how do you revert a commit that has already been pushed and made public?

git revert <name of bad commit>


# <h2> What is the difference between git pull and git fetch?
Git pull = git fetch + git merge 

# <h2> What is ‘staging area’ or ‘index’ in Git?
before completing the commits, it can be formatted and reviewed in an intermediate area known as ‘Staging Area’ or ‘Index’.


# <h2>  What is the difference between the ‘git diff ’and ‘git status’?
 ‘git diff’ is similar to ‘git status’, the only difference is that it shows the differences between various commits and also between the working directory and index. 
 
 
# <h2>  What is git cherry-pick?
 The command git cherry-pick is normally used to introduce particular commits from one branch within a repository onto a different branch.
 git cherry-pick <commit-hash>
 
# <h2>  How do you find a list of files that have changed in a particular commit?
 git diff-tree -r {hash}
 
 
# <h2>  What do you mean by Git fork?
 A Git fork is nothing but a copy of a Git repository. In a Git ecosystem forking down a Repository enables you with liberal experimentation with different changes with little or no Effects on your original project.
 
 
 
# <h2>  What is the HEAD in git?
 HEAD is a reference to the last commit in the currently checked-out branch.
cat .git/HEAD


# <h5> *Learn more about markdown [here](https://guides.github.com/features/mastering-markdown/)*