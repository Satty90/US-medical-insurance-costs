from data import ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges
import numpy as np
import matplotlib.pyplot as plt


# analyse data here
class PatientDataAnalysis:
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, patients_smoker_status, patients_regions, patients_insurance_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_status = patients_smoker_status
        self.patients_regions = patients_regions
        self.patients_insurance_charges = patients_insurance_charges

    def analyze_ages(self):
        ages_integer = [int(age) for age in self.patients_ages]
        total = 0
        for age_int in ages_integer:
            total += age_int
        mean = round(total / len(ages_integer), 2)
        print(f"Average Patient Age: {mean} years")
        ages_sorted = sorted(ages_integer)
        median = ages_sorted[len(ages_sorted) // 2]
        print(f"Median Pacient Age: {median} years")
        standard_deviation = round(np.std(ages_integer, ddof=1), 2)
        print(f"Standard Deviation: {standard_deviation}")

    def analyze_sexes(self):
        num_of_females = self.patients_sexes.count("female")
        num_of_males = self.patients_sexes.count("male")
        print(f"Number of females: {num_of_females}")
        print(f"Number of males: {num_of_males}")

    def unique_regions(self):
        unique_regions = []
        [unique_regions.append(
            region) for region in self.patients_regions if region not in unique_regions]
        return unique_regions


patient_info = PatientDataAnalysis(
    ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)

patient_info.analyze_ages()
patient_info.analyze_sexes()
patient_info.unique_regions()
