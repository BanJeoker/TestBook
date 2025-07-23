conda create -n myenv python=3.11 -y
conda activate myenv
conda install --file "C:\Users\YourName\envs\conda-packages.txt" -y
python -m ipykernel install --user --name=myenv --display-name "Python (myenv)"
jupyter notebook
