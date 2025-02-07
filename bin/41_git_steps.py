"""
git: Version Control System
"""

# ---------
# Creating Git repository in our laptop
# ---------
# 1. We need git software
#   https://git-scm.com/downloads
#
# 2. We can use git-UI or terminal/command-prompt
#
# 3. We will make python_training folder as git-repository
#   Steps:
#   step-1 open cmd prompt
#   step-2: cd (change directory) to python_training folder
#   step-3: git init
#   NOW python_training folder is git repository
#
# 4. add all folders/files present in python_training folder
#   to git repository
#   Steps:
#   Step-1: git add bin log programs rest_api Readme.txt
#   Step-2: git status
#   Step-3: git commit -m "Adding all files and folders to git"
#   Step-4: git status
############################

# ---------
# Create New Repository In Github.
# ---------
# 1. Create new account https://github.com/
# 2. Create new repository with the name 'python_training'
############################

# ---------
# Link local repository (laptop-python_training folder)
#   with
#   git-repository 'python_training'
# ---------
# 1. open cmd/command-prompt
# 2. git remote add origin https://github.com/mahadevaprabhug/python_training_7.git
# 3. git push -u origin master
# 4. refresh github reposotory to see the files & folders
############################


# ---------
# Download trainer code from git
# ---------
# 1. Create new directory say 'trainer_code'
#       then cd to trainer_code
#
# 2. Make trainer_code as git repository
#       git init
#
# 3. git remote add origin https://github.com/mahadevaprabhug/python_training_7.git
#
# 4. git pull origin master
#
############################