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
        print(f"Median Patient Age: {median} years")
        standard_deviation = round(np.std(ages_integer, ddof=1), 2)
        print(f"Standard Deviation: {standard_deviation}")

    def analyze_sexes(self):
        num_of_females = self.patients_sexes.count("female")
        num_of_males = self.patients_sexes.count("male")
        print(f"Number of females: {num_of_females}")
        print(f"Number of males: {num_of_males}")

    def unique_regions(self):
        unique_regions = []
        for region in self.patients_regions:
            if region not in unique_regions:
                unique_regions.append(region)
        return unique_regions

    def analyze_charges(self):
        charges = [float(charge) for charge in self.patients_insurance_charges]

        # basic statistical analysis
        mean = round(sum(charges) / len(charges), 2)
        median = round(sorted(charges)[len(charges) // 2], 2)
        std_dev = round(np.std(charges, ddof=1), 2)
        min_charge = round(min(charges), 2)
        max_charge = round(max(charges), 2)

        print("\n--- INSURANCE CHARGES ANALYSIS ---")
        print(f"Average Insurance Charge: ${mean}")
        print(f"Median Insurance Charge: ${median}")
        print(f"Standard Deviation: ${std_dev}")
        print(f"Maximum Charge: ${max_charge}")
        print(f"Minimum Charge: ${min_charge}")

        # smoking status analysis
        smoker_charges = [float(charges[i]) for i in range(
            len(charges)) if self.patients_smoker_status[i] == "yes"]
        non_smoker_charges = [float(charges[i]) for i in range(
            len(charges)) if self.patients_smoker_status[i] == "no"]

        avg_smoker_charge = round(sum(smoker_charges) / len(smoker_charges), 2)
        avg_non_smoker_charge = round(
            sum(non_smoker_charges) / len(non_smoker_charges), 2)
        smoker_cost_differene = abs(avg_smoker_charge - avg_non_smoker_charge)

        print("\n--- SMOKING STATUS IMPACT ON INSURANCE COST ---")
        print(f"Average Cost for Smokers: ${avg_smoker_charge}")
        print(f"Average Cost for Non-smokers: ${avg_non_smoker_charge}")
        print(f"Saving on Average for Non-smokers: ${smoker_cost_differene}")

        # gender analysis
        male_charges = [float(charges[i]) for i in range(
            len(charges)) if self.patients_sexes[i] == "male"]
        female_charges = [float(charges[i]) for i in range(
            len(charges)) if self.patients_sexes[i] == "female"]

        avg_male_insurance_cost = round(
            sum(male_charges) / len(male_charges), 2)
        avg_female_insurance_cost = round(
            sum(female_charges) / len(female_charges), 2)
        gender_cost_difference = abs(
            avg_male_insurance_cost - avg_female_insurance_cost)

        print("\n--- GENDER ANALYSIS ---")
        print(f"Average Cost for Males: ${avg_male_insurance_cost}")
        print(f"Average cost for Females: ${avg_female_insurance_cost}")
        print(
            f"Cost Difference for Men and Women on Average: ${gender_cost_difference}")

        # regions analysis
        regions = self.unique_regions()
        regional_costs = {}

        for region in regions:
            region_charges = [float(charges[i]) for i in range(
                len(charges)) if self.patients_regions[i] == region]
            regional_costs[region] = round(
                sum(region_charges) / len(region_charges), 2)

        print("\n --- REGIONAL ANALYSIS ---")
        for region, avg_cost in regional_costs.items():
            print(f"Average cost in {region}: ${avg_cost}")

        # BMI analysis
        bmis = [float(bmi) for bmi in self.patients_bmis]
        bmi_correlation = round(np.corrcoef(bmis, charges)[0, 1], 4)

        print("\n--- BMI ANALYSIS ---")
        print(f"Correlation between BMI and charges: {bmi_correlation}")
        print(f"Relationship: {"Strong" if abs(bmi_correlation) > 0.7 else "Moderate" if abs(bmi_correlation) > 0.3 else "Weak"} " +
              f"{"positive" if bmi_correlation > 0 else "negative"} relationship")

        # children analysis
        child_count = {}
        for i in range(len(self.patients_num_children)):
            children = int(self.patients_num_children[i])
            if children not in child_count:
                child_count[children] = {"total": 0, "count": 0}
            child_count[children]["total"] += float(charges[i])
            child_count[children]["count"] += 1

        print("\n--- CHILDREN ANALYSIS ---")
        print("Average Cost by Number of Children::")
        for children, data in sorted(child_count.items()):
            avg_cost = round(data["total"] / data["count"], 2)
            print(f" {children} children: ${avg_cost}")

        # age analysis
        ages = [int(age) for age in self.patients_ages]
        age_correlation = round(np.corrcoef(ages, charges)[0, 1], 4)
        print("\n--- AGE ANALYSIS ---")
        print(f"Correlation between age and cost: {age_correlation}")
        print(f"Relationship: {"Strong" if abs(age_correlation) > 0.7 else "Moderate" if abs(age_correlation) > 0.3 else "Weak"} " +
              f"{"positive" if age_correlation > 0 else "negative"} relationship")

        # visualisations
        plt.figure(figsize=(15, 10))

        # 1. charges
        plt.subplot(2, 3, 1)
        plt.hist(charges, bins=20, color="skyblue", edgecolor="black")
        plt.title("Distribution of Insurance Charges")
        plt.xlabel("Charge ($)")
        plt.ylabel("Frequency")

        # 2. smoker
        plt.subplot(2, 3, 2)
        plt.boxplot([non_smoker_charges, smoker_charges],
                    labels=['Non-smokers', 'Smokers'])
        plt.title('Charges by Smoking Status')
        plt.ylabel('Charge ($)')

        # 3. Regional comparison
        plt.subplot(2, 3, 3)
        regions_list = list(regional_costs.keys())
        costs_list = [regional_costs[region] for region in regions_list]
        plt.bar(regions_list, costs_list, color='lightgreen')
        plt.title('Average Cost by Region')
        plt.ylabel('Average Charge ($)')
        plt.xticks(rotation=45)

        # 4. Age vs. charges scatter plot
        plt.subplot(2, 3, 4)
        plt.scatter(ages, charges, alpha=0.5, color='coral')
        plt.title('Age vs. Insurance Charges')
        plt.xlabel('Age')
        plt.ylabel('Charges ($)')

        # 5. BMI vs. charges scatter plot
        plt.subplot(2, 3, 5)
        plt.scatter(bmis, charges, alpha=0.5, color='purple')
        plt.title('BMI vs. Insurance Charges')
        plt.xlabel('BMI')
        plt.ylabel('Charges ($)')

        # 6. Children count impact
        plt.subplot(2, 3, 6)
        children_count = sorted(child_count.keys())
        children_avgs = [child_count[count]['total'] /
                         child_count[count]['count'] for count in children_count]
        plt.bar([str(c) for c in children_count],
                children_avgs, color='salmon')
        plt.title('Average Cost by Number of Children')
        plt.xlabel('Number of Children')
        plt.ylabel('Average Charge ($)')

        plt.tight_layout()
        plt.show()

    def create_dictionary(self):
        self.patients_dictionary = {}
        self.patients_dictionary["age"] = [
            int(age) for age in self.patients_ages]
        self.patients_dictionary["sex"] = self.patients_sexes
        self.patients_dictionary["bmi"] = self.patients_bmis
        self.patients_dictionary["children"] = self.patients_num_children
        self.patients_dictionary["smoker"] = self.patients_smoker_status
        self.patients_dictionary["regions"] = self.patients_regions
        self.patients_dictionary["charges"] = [
            float(charge) for charge in self.patients_insurance_charges]
        return self.patients_dictionary


patient_info = PatientDataAnalysis(
    ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)

patient_info.analyze_ages()
patient_info.analyze_sexes()
patient_info.unique_regions()
patient_info.analyze_charges()
patient_info.create_dictionary()
