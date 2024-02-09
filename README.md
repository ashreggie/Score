1. Executive Summary
    
    The objective of studying this dataset is to predict the final score of the students based on several factors.

    Data exploratory is first performed to understand the data and determine useful features to conduct a regression model.

    We build an end-to-end Machine Learning Pipeline to guide the preprocessing stage followed by understanding how the models are chosen and evaluated.

2. Task Summary

    - Use GitHub for CI/CD and version-control   with private repository for project
    - Adding of AISG-AIAP as collaborator
    -  Contains executable shell-bash script (.sh) to run mlp_pipeline.py
    -  Exploratory Data Analysis (EDA) in python notebook (.ipynb)
    - End-to-end Machine Learning Pipeline (MLP) stored in src folder (.py)
    - readme.md to describe walkthrough of project
    -  File Structure
    -  GitHub project repository should not contain dataset (.db)
    - Inclusion of requirements.txt
    -  Complete submission form on google docs

3. Folder Structure
  
    \- .github    
  &nbsp;&nbsp;&nbsp;&nbsp; \- workflows\
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | github-actions.yml\
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; .DS_Store\
  \- .ipynb_checkpoints\
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  eda-checkpoint.ipynb\
  \- images\
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; aiap14_mlp_pipeline_flow.png\
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;aiap14_mlp_pipeline_summary_example.png\
  \- src\
  &nbsp;&nbsp;&nbsp;&nbsp;\- *__pycache*__\
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| preprocessor.cpython-310.pyc\
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; mlp_pipeline.py\
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; preprocessor.py\
  &nbsp;&nbsp;DS_Store\
  &nbsp;&nbsp;.gitignore\
  &nbsp;&nbsp;README.md\
  &nbsp;&nbsp;eda.ipynb\
  &nbsp;&nbsp;requirements.txt\
  &nbsp;&nbsp;run.sh\
  &nbsp;&nbsp;sample_output_log.txt\

4. Instruction


  
    For Linux\
    With Python activated in your environment:

    Clone this project\
    git clone https://github.com/ahjimomo/aiap14-ng-kok-woon-685E.git\

    Run the shell bash script:\
    bash run.sh

    For Windows\
    Open a python shell in your terminal:

    Clone this project\
    git clone https://github.com/ahjimomo/aiap14-ng-kok-woon-685E.git\

    Run the shell bash script:\
    bash run.sh


5. Project Pipeline

    &nbsp;&nbsp;&nbsp;&nbsp;5.1 EDA and key findings
    
    &nbsp;&nbsp;&nbsp;&nbsp;5.2 Feature Engineering
    Feature | Description | Processed
    ---|---|---
    Gender | fzgzg | sggz 
    Color | AFg | SDF

  
    &nbsp;&nbsp;&nbsp;&nbsp;5.3 Choice of Models
    
    &nbsp;&nbsp;&nbsp;&nbsp;5.4 Evaluation of Models