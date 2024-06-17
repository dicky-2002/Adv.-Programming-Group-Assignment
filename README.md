# Adv.-Programming-Group-Assignment
This repository contains all the filles for the group assignment for the advanced programming course for biomedical engineers

# VIRTUAL ENVIRONMENT SETUP:
To create a new environment with conda, where all packages are installed, use the following commands on your terminal:
# to create the env with all the needed packages: (might take several minutes)
conda env create --file groupass.yml    
# to activate the new environment:    
conda activate groupass_group8


-------------------------------

Since this is the first time for everyone callaborating using Git, presumably, I made an attempt to quickly discuss some of the main
points about how to handle code sharing within this repository, should anyone still have some questions about this. Most of the steps 
below are probably unneccesary to mention, but I put them in purely to avoid any confusion. While the use of GitHub Desktop is optional,
 it was my understanding that everyonye is using the desktop version, including me, so the steps below
also reffer to the desktop version.
----------------------------------------------------------------------------------------------------------------------------------------

1. Opening the repository
===============================
If you are reading this, you have already succesfully opened the repository. Hoorayyy:).


2. Making changes to the code
===============================
After opening the repository on your local drive, you can continue to make changes to the code in
VS-Code. Any changes to the code will automaticly be detected in the GIT repository. The repository
will show which files, along with which sections of the code were modified.


3. Commit vs. Push
===============================
When you're done making your adjustments to the code, you can continue to commit your code in the
desktop app. This will create a new branch in the pipeline, containing the newly modified code, while
the previously unmodified version still remains available in the main branch for everyone in case the 
earlier version needs to be re-accesed.

Commit can be easily confused with Push. Git commit puts your changes into your local repository, 
while git push sends your changes to the remote location. git push is used to add commits you have 
done on the local repository to a remote one. Together with git pull, it allows people to collaborate.


4. Pull request
==============================
A pull request is a proposal to merge a set of changes from one branch into another. In a pull request,
collaborators can review and discuss the proposed set of changes before they integrate the changes into
the main codebase. Pull requests display the differences, or diffs, between the content in the source 
branch and the content in the target branch.


5. Merging
===============================
If the newly created branch is accepted by everyone in the group, the branch can be merged with the main branch.
Again, the previously unchanged version still remains, so you don't have to worry about making mistakes and losing
important progress.


6. Merge Conflicts
===============================
Git can often resolve differences between branches and merge them automatically. Usually, the changes are on different
lines, or even in different files, which makes the merge simple for computers to understand. However, sometimes there
are competing changes that Git can't resolve without your help. Often, merge conflicts happen when people make different
changes to the same line of the same file, or when one person edits a file and another person deletes the same file.

You must resolve all merge conflicts before you can merge a pull request on GitHub. If you have a merge conflict between
the compare branch and base branch in your pull request, you can view a list of the files with conflicting changes above
the Merge pull request button. The Merge pull request button is deactivated until you've resolved all conflicts between
the compare branch and base branch.

-------------------------------------------------------------------------------------------------------------------------
Last but not least don't forget that this is might still be the first time for some people collaborating in Git, including me,
so make sure to commicate clearly about anything that might still be a little vague, wheter it is communication within Github
or through Whatsapp.