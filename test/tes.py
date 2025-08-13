import sys, site, pathlib
print("Interpreter:", sys.executable)                 # should be ...\myenv\Scripts\python.exe
print("User-site :", site.getusersitepackages())      # typically ...\AppData\Roaming\Python\Python311\site-packages
print("User-site on sys.path?:", site.getusersitepackages() in sys.path)

# Is your venv isolated?
print("pyvenv.cfg exists:", pathlib.Path(sys.prefix, "pyvenv.cfg").exists())
print("include-system-site-packages =", any("include-system-site-packages" in l 
      for l in pathlib.Path(sys.prefix, "pyvenv.cfg").read_text().splitlines()))



conda create -n myenv python=3.11 -y
conda activate myenv
conda install --file "C:\Users\YourName\envs\conda-packages.txt" -y
python -m ipykernel install --user --name=myenv --display-name "Python (myenv)"
jupyter notebook
