# US Medical Insurance Costs Analysis

## Project Overview
This project analyzes a dataset of US medical insurance costs to identify factors that influence insurance charges. Using Python-based data analysis, the program explores how variables such as age, BMI, smoking status, gender, region, and number of children affect insurance pricing.

## Dataset
The project uses the `insurance.csv` dataset, which includes the following features:

- **Age**: Age of the policyholder
- **Sex**: Gender of the policyholder (`male`, `female`)
- **BMI**: Body Mass Index
- **Children**: Number of dependents covered by insurance
- **Smoker**: Smoking status (`yes`, `no`)
- **Region**: Residential region in the US (`northeast`, `southeast`, `southwest`, `northwest`)
- **Charges**: Individual medical insurance charges

## Features
The project provides a comprehensive analysis, including:

- **Basic Statistical Analysis**: Mean, median, standard deviation, min, and max of insurance charges
- **Demographic Analysis**: Effects of age and gender on costs
- **Lifestyle Impact**: Analysis of smoking status and BMI
- **Family Size Analysis**: Correlation between number of children and charges
- **Geographic Analysis**: Cost comparisons across US regions
- **Data Visualisation**: Multiple plots and charts to highlight patterns and trends

## Visualisations
Included visualisations:

- Distribution of insurance charges
- Box plots comparing charges by smoking status
- Bar charts of average charges by region
- Scatter plots (e.g., age vs. charges, BMI vs. charges)
- Bar charts showing average costs by number of children

## Setup and Installation
1. Clone this repository
2. Ensure you have the required packages:
   ```bash
   pip install numpy
   pip install matplotlib

## Usage
Run the main analysis file:
```bash
python US_medical_insurance_costs.py
```

## Project structure
- `insurance.csv`: The dataset file
- `utils.py`: Utility function for loading data
- `data.py`: Data laoding module
- `US_medical_insurance_costs.py`: Main analysis script

## Key Findings
Running this analysis reveals several insights:
- Smoking status has a significant impact on insurance costs
- There is a positive correlation between age and insurance charges
- BMI shows a weak positive relationship with insurance costs
- Regional differences exist in average insurance charges
- The number of dependents (children) affects insurance pricing

## Future Improvements
- Add more advanced statistical analysis
- Implement predictive modeling for insurance cost estimation
- Enhance visualizations with interactive elements

## Author
Mahdi Sattarnia
   
