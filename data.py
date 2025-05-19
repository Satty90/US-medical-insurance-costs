from utils import load_data_list


ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []


load_data_list(ages, "insurance.csv", "age")
load_data_list(sexes, "insurance.csv", "sex")
load_data_list(bmis, "insurance.csv", "bmi")
load_data_list(num_children, "insurance.csv", "children")
load_data_list(smoker_statuses, "insurance.csv", "smoker")
load_data_list(regions, "insurance.csv", "region")
load_data_list(insurance_charges, "insurance.csv", "charges")
