# Dublin-Regional-Economic-Outlook
## Project Title 
Dublin Regional Economic Outlook 
## Description
Dublin Region Economic Indicators help monitor economic development in the Dublin City Region. This project aims at analyzing datasets of those indicators provided by Dublin City Council (DCC) available [here](https://data.smartdublin.ie/dataset/dublin-economic-monitor). 

Datasets include: 
1. National and Dublin Unemployment
2. Sectoral Employment
3. Dublin and National ex Dublin Residential Property Price Indexes
4. Dublin, GDA and Outside GDA Residential Rents Indexes
5. Dublin housing completions and commencements
6. Dublin Public Transport Usage
7. Dublin Airport passenger arrivals
8. Dublin Port Tonnage
9. Dublin current conditions
10. Dublin expectations
11. Dublin sentiment overall


## How to View the Project
### 1. Quick way
You can view the HTML without setting up Python or Jupyter.

### 2. To Run the Project Locally
#### a. Clone the Repository
Start by cloning the project to your local machine.
```
git clone https://github.com/your-username/Dublin-Regional-Economic-Outlook
cd Dublin-Regional-Economic-Outlook
```
#### b. Set Up the Virtual Environment
Option 1: Using pip and venv
```
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
```
Option 2: Using Conda
```
conda env create -f environment.yml
conda activate dublin_data_env
```
#### c. Launch Jupyter Notebook
For venv users:
```
deactivate

```

#### d. Deactivate the Environment (when done)
For conda users:
```
conda deactivate

```
