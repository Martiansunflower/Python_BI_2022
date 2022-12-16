## The ultraviolence of virtual environments

### Instead of introduction 
This thread describes my attempt to reproduce Michael's research presented in the article [doi:10.1111/1000-7](https://mangaplus.shueisha.co.jp/titles/100027) by running the script ultraviolence.py. Michael's work is very good, but the lack of a requirements file makes it difficult to take advantage of it, so I have prepared one and hope it will help. Please cite this as well.

This work was performed at on Linux 5.15.0-56-generic x86_64, Ubuntu 22.04.1 LTS, Python 3.11.

### Step 1. Installation of the necessary software. 
For running the script you will need Python ver. 3.11.`x`, you can download it from [here](https://www.python.org/downloads/release/python-3111/).
Since we will need to install many libraries that may conflict with already installed ones, it makes sense to run the script in a virtual environment.
So it is also necessary to install venv with Python 3.11, and you can do this with the following command:

```
sudo apt install python3.11 -venv
```

### Step 2. Creating virtual invironment 
First, create a virtual environment for our project:
```
python3.11 -m venv <project_name>
```
Then activate it:
```
source HW_3/bin/activate
```
With ```cd``` command get into a virtual environment folder. 

Now it is necessary to add the ultraviolence.py file to the virtual environment. You can do this in any way: copy the script and create a similar file in any text editor or directly clone this branch from the githab. In the second case, you may need install git first: 
```
sudo apt install git
git clone https://github.com/Martiansunflower/Python_BI_2022.git -b Homework_3
cd Python_BI_2022/
```

### Step 3.

Before going any further, please with ```python -V ``` and ```pip -V``` make sure that the python and pip versions match. 

Then following dependencies will need to be installed for the script to work correctly:
```
pip install --upgrade google-api-python-client
pip install python-math
pip install typing
pip install beautifulsoup4
pip install requests
pip install bio
pip install aiohttp
pip install pandas
pip install opencv-python
pip install lxml
```
Moreover, you will have to edit one library. Please go to the root of virtual environment, then follow `/lib/python3.11/site-packages/pandas/core/` and open _frame.py_ as text file.

example: ``/home/sweetlana/HW_3/lib/python3.11/site-packages/pandas/core/frame.py``

Here you should deactivate following lines:
```
# if index is not None and isinstance(index, set):
# raise ValueError("index cannot be a set")
```
![](https://github.com/Martiansunflower/Python_BI_2022/blob/8d1331911402e4218e7828a92458ea531b9250e5/be_careful.png)

We're at the finish line. To create requirements.txt, return to folder with script and proceed:
```
pip freeze > requirements.txt
pip install -r requirements.txt
```

Now all we have to do is run the script. 

```
python3.11 ultraviolence.py
```
![](https://github.com/Martiansunflower/Python_BI_2022/blob/8d1331911402e4218e7828a92458ea531b9250e5/sucsess.png)

You're gorgeous! \
If something went wrong, please feel free to write me -- let's improve this instruction together.

### Step 4. Instead of an afterword 

Don`t forget to deactivate the virtual environment with the ```deactivate``` command. 
