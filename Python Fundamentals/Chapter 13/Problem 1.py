# 1. Create two virtual environments, install few packages in the first one. How do you
# create a similar environment in the second one?


#run on cmd

# cd your files where you want to create virtual enviroments

# virtualenv env1

# virtualenv env2

# .\env1\Scripts\activate.ps1      run env1

# pip install pandas==1.5
# pip install pyjokes

# pip freeze > requirements.txt


# deactivate 
# .\env2\Scripts\activate.ps1 

# pip install -r requirements.txt