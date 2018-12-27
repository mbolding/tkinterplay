just some notes while playing on the cluster
=====

Install ipython (or some module) locally:
-----
    module load Python
    pip install --user ipython

Install fish (or some package) locally:
-----
    module load Anaconda3
    conda install -p $HOME/.local -c conda-forge fish

Vnc headaches:
-----
    export DISPLAY=localhost:2  # e.g. vncserver on 5902
    xhost +   
    open vnc://localhost  # on os x, kept locking up
    mutter &

mutter is gnome 3 WM ?, why isn't the WM starting from xstartup?
