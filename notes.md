# just notes while playing on the cluster.

Install ipython locally:
-----
module load Python
pip install ?user ipython

Install fish locally:
-----
module load Anaconda3
conda install -p $HOME/.local -c conda-forge fish

Vnc headaches:
-----
export DISPLAY=localhost:2  # e.g. vncserver on 5902
xhost +   
# os x open vnc://localhost  kept locking up
mutter &  # gnome 3 WM ?, why isn't the WM starting from xstartup?
