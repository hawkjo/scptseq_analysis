# scPT-seq Analysis and Figure Generation

Analysis and figure generation scripts for

### Direct detection of CRISPR mutations and transcriptional responses at single cell resolution in vivo

**John A. Hawkins, Siamak Redhai, Svenja Leible, Mireia Osuna Lopez, Hilal Ozgur, Tianyu Wang, Michaela Holzem, Michael Boutros, Oliver Stegle**

## Analysis notebooks

### Run in the browser
The easiest way to run the notebooks is in the browser with Binder. Simply click on the links below
to launch Binder instances, which will automatically build the appropriate environment and run a
live instance of the notebook in the broswer.

Once the environment is built and the notebook is ready, select from the menubar `Run > Run All`.

#### Mutations and Clones
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/hawkjo/scptseq_analysis/main?labpath=Mutations_and_Clones.ipynb)
Click to launch a live, reproducible environment in your browser.

#### DE and GO Results
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/hawkjo/scptseq_analysis/main?labpath=DE_and_GO.ipynb)
Click to launch a live, reproducible environment in your browser.


### Manual installation
Alternatively, you can install all requirements in your own virtual environment with
```
python -m pip install -r requirements.txt
```
Add the virtual environment to your jupyter setup using
```
python -m ipykernel install --user --name <venv_name> --display-name "<venv_name>"
```
And after opening the notebooks, select the appropriate environment as your kernel and run as
normal.
