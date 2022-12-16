## The ultraviolence of virtual environments

### Instead of introduction 
This thread describes my attempt to reproduce Michael's research presented in the article [doi:10.1111/1000-7](https://mangaplus.shueisha.co.jp/titles/100027) by running the script ultraviolence.py. Michael's work is very good, but the lack of a requirements file makes it difficult to take advantage of it, so I have prepared one and hope it will help. Please cite this as well.

This work was performed at on Linux 5.15.0-56-generic x86_64, Ubuntu 22.04.1 LTS, Python 3.11.

### Step 1. Installation of the necessary software. 
For running the script you will need Python ver. 3.11.x, you can download it from [here](https://www.python.org/downloads/release/python-3111/).
Since we will need to install many libraries that may conflict with those already installed, it makes sense to run the script in a virtual environment.
So it is also necessary to install venv with Python 3.11, and you can do this with the following command:

```
sudo apt install python3.11 -venv
```

### Step 2. Creating virtual invironment 
First, create a virtual environment for our project:
```
python3.11 -m venv <project_name>
_example: python3.11 -m venv HW_3_
```
Then activate it:
```
source HW_3/bin/activate
```
With ```cd``` command get into a virtual environment folder. 
cd HW3
git clone https://github.com/Martiansunflower/Python_BI_2022.git -b Homework_3_Ultraviolence.
cd Python_BI_2022/

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

/home/sweetlana/HW_3/lib/python3.11/site-packages/pandas/core/frame.py

# if index is not None and isinstance(index, set):
    # raise ValueError("index cannot be a set")

pip freeze > requirements.txt
pip install -r requirements.txt

python3.11 ultraviolence.py

You're gorgeous!

