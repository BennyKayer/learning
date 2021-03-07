conda commands only work in Anaconda Prompt - Miniconda
List envs
`conda env list`
Create env with packages - doesn't allow name, creates in project
`conda create --prefix ./env pandas numpy matplotlib scikit-learn`
Use name but not able to specify where the env should be
`conda create --name env_name pandas numpy matplotlib scikit-learn`
Install notebook
`conda install jupyter notebook`
