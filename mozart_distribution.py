import streamlit as st
import pandas as pd
import itertools

# Load the dataset
df = pd.read_csv('first_digit.csv')

# Step 2: Generate all possible splits of the first digits into 2 groups
def get_valid_splits_two_groups(df):
    first_digits = df['First Digit'].tolist()
    populations = df['Population'].tolist()
    total_population = sum(populations)
    half_population = total_population / 2
    
    # Generate all combinations of first_digits and split them into two groups
    valid_splits = []
    
    # We only need to check combinations that are half of the total length
    all_combinations = itertools.combinations(range(len(first_digits)), len(first_digits) // 2)
    
    for comb in all_combinations:
        # Calculate the sum of the population for this combination
        comb_population = sum(populations[i] for i in comb)
        
        # Get the other group as the complement of this combination
        treatment_group = set(range(len(first_digits))) - set(comb)
        treatment_population = sum(populations[i] for i in treatment_group)
        
        # Check if both groups have populations within an acceptable margin of each other
        if abs(comb_population - treatment_population) <= 50000:  # Allow for small tolerance of 50,000
            control_group = [first_digits[i] for i in comb]
            treatment_group = [first_digits[i] for i in treatment_group]
            valid_splits.append((control_group, treatment_group, comb_population, treatment_population))
    
    return valid_splits

# Step 3: Generate all possible splits of the first digits into 4 groups
def get_valid_splits_four_groups(df):
    first_digits = df['First Digit'].tolist()
    populations = df['Population'].tolist()
    total_population = sum(populations)
    target_population_per_group = total_population / 4
    
    valid_splits = []
    
    # Generate all possible control group combinations (1 group)
    all_combinations = itertools.combinations(range(len(first_digits)), 2)  # Control group has 2 digits
    
    for comb in all_combinations:
        # Calculate the sum of the population for this control combination
        control_population = sum(populations[i] for i in comb)
        
        # Get the remaining digits for treatment groups
        remaining_digits = set(range(len(first_digits))) - set(comb)
        
        # Split the remaining digits into 3 treatment groups (approx 25% each)
        for treatment_comb in itertools.combinations(remaining_digits, 3):  # First treatment group
            treatment_group_1 = [first_digits[i] for i in treatment_comb]
            treatment_population_1 = sum(populations[i] for i in treatment_comb)
            
            remaining_for_treatment_2_3 = remaining_digits - set(treatment_comb)
            
            for treatment_comb2 in itertools.combinations(remaining_for_treatment_2_3, 2):  # Second treatment group
                treatment_group_2 = [first_digits[i] for i in treatment_comb2]
                treatment_population_2 = sum(populations[i] for i in treatment_comb2)
                
                treatment_group_3 = list(remaining_for_treatment_2_3 - set(treatment_comb2))  # Third treatment group
                treatment_population_3 = sum(populations[i] for i in treatment_group_3)
                
                # Check if the populations are reasonably close to the target population per group
                if abs(control_population - target_population_per_group) <= 1550000 and \
                   abs(treatment_population_1 - target_population_per_group) <= 2400000 and \
                   abs(treatment_population_2 - target_population_per_group) <= 2400000 and \
                   abs(treatment_population_3 - target_population_per_group) <= 2400000:
                    valid_splits.append((
                        [first_digits[i] for i in comb],
                        treatment_group_1,
                        treatment_group_2,
                        treatment_group_3,
                        control_population,
                        treatment_population_1,
                        treatment_population_2,
                        treatment_population_3
                    ))
                # Stop if we've collected 20 valid splits
                    if len(valid_splits) >= 20:
                        return valid_splits

# Step 4: Generate all possible splits of the first digits into 6 groups
def get_valid_splits_six_groups(df):
    first_digits = df['First Digit'].tolist()
    populations = df['Population'].tolist()
    total_population = sum(populations)
    target_population_per_group = total_population / 6
    
    valid_splits = []
    
    # Generate all possible control group combinations (1 group)
    all_combinations = itertools.combinations(range(len(first_digits)), 1)  # Control group has 1 digit
    
    for comb in all_combinations:
        # Calculate the sum of the population for this control combination
        control_population = sum(populations[i] for i in comb)
        
        # Get the remaining digits for treatment groups
        remaining_digits = set(range(len(first_digits))) - set(comb)
        
        # Split the remaining digits into 5 treatment groups (approx 16.6% each)
        for treatment_comb in itertools.combinations(remaining_digits, 2):  # First treatment group
            treatment_group_1 = [first_digits[i] for i in treatment_comb]
            treatment_population_1 = sum(populations[i] for i in treatment_comb)
            
            remaining_for_treatment_2_3_4_5 = remaining_digits - set(treatment_comb)
            
            for treatment_comb2 in itertools.combinations(remaining_for_treatment_2_3_4_5, 2):  # Second treatment group
                treatment_group_2 = [first_digits[i] for i in treatment_comb2]
                treatment_population_2 = sum(populations[i] for i in treatment_comb2)
                
                remaining_for_treatment_3_4_5 = remaining_for_treatment_2_3_4_5 - set(treatment_comb2)
                
                for treatment_comb3 in itertools.combinations(remaining_for_treatment_3_4_5, 2):  # Third treatment group
                    treatment_group_3 = [first_digits[i] for i in treatment_comb3]
                    treatment_population_3 = sum(populations[i] for i in treatment_comb3)
                    
                    remaining_for_treatment_4_5 = remaining_for_treatment_3_4_5 - set(treatment_comb3)
                    
                    for treatment_comb4 in itertools.combinations(remaining_for_treatment_4_5, 2):  # Fourth treatment group
                        treatment_group_4 = [first_digits[i] for i in treatment_comb4]
                        treatment_population_4 = sum(populations[i] for i in treatment_comb4)
                        
                        treatment_group_5 = list(remaining_for_treatment_4_5 - set(treatment_comb4))  # Fifth treatment group
                        treatment_population_5 = sum(populations[i] for i in treatment_group_5)
                        
                        # Check if the populations are reasonably close to the target population per group
                        if abs(control_population - target_population_per_group) <= 4550000 and \
                           abs(treatment_population_1 - target_population_per_group) <= 4550000 and \
                           abs(treatment_population_2 - target_population_per_group) <= 4550000 and \
                           abs(treatment_population_3 - target_population_per_group) <= 4550000 and \
                           abs(treatment_population_4 - target_population_per_group) <= 4550000 and \
                           abs(treatment_population_5 - target_population_per_group) <= 4550000:
                            valid_splits.append((
                                [first_digits[i] for i in comb],
                                treatment_group_1,
                                treatment_group_2,
                                treatment_group_3,
                                treatment_group_4,
                                treatment_group_5,
                                control_population,
                                treatment_population_1,
                                treatment_population_2,
                                treatment_population_3,
                                treatment_population_4,
                                treatment_population_5
                            ))
                            # Stop if we've collected 20 valid splits
                            if len(valid_splits) >= 20:
                                return valid_splits
    
    return valid_splits

# Step 5: Display the valid splits based on the user's input
def display_balanced_splits(num_tests):
    if num_tests == 1:
        valid_splits = get_valid_splits_two_groups(df)
        st.write("### Balanced Splits (2 Groups)")
        for idx, (control_group, treatment_group, control_population, treatment_population) in enumerate(valid_splits, 1):
            st.markdown(f"**{idx}. Split {idx}:**")
            st.markdown(f"**Control Group (First Digit):** {', '.join(map(str, control_group))} (Population: {control_population})")
            st.markdown(f"**Treatment Group (First Digit):** {', '.join(map(str, treatment_group))} (Population: {treatment_population})")
            st.write("\n")
    
    elif num_tests == 2:
        valid_splits = get_valid_splits_four_groups(df)
        st.write("### Balanced Splits (4 Groups)")
        for idx, (control_group, treatment_group_1, treatment_group_2, treatment_group_3, control_population, treatment_population_1, treatment_population_2, treatment_population_3) in enumerate(valid_splits, 1):
            st.markdown(f"**{idx}. Split {idx}:**")
            st.markdown(f"**Control Group (First Digit):** {', '.join(map(str, control_group))} (Population: {control_population})")
            st.markdown(f"**Treatment Group 1 (First Digit):** {', '.join(map(str, treatment_group_1))} (Population: {treatment_population_1})")
            st.markdown(f"**Treatment Group 2 (First Digit):** {', '.join(map(str, treatment_group_2))} (Population: {treatment_population_2})")
            st.markdown(f"**Treatment Group 3 (First Digit):** {', '.join(map(str, treatment_group_3))} (Population: {treatment_population_3})")
            st.write("\n")
    
    elif num_tests == 3:
        valid_splits = get_valid_splits_six_groups(df)
        st.write("### Balanced Splits (6 Groups)")
        for idx, (control_group, treatment_group_1, treatment_group_2, treatment_group_3, treatment_group_4, treatment_group_5, control_population, treatment_population_1, treatment_population_2, treatment_population_3, treatment_population_4, treatment_population_5) in enumerate(valid_splits, 1):
            st.markdown(f"**{idx}. Split {idx}:**")
            st.markdown(f"**Control Group (First Digit):** {', '.join(map(str, control_group))} (Population: {control_population})")
            st.markdown(f"**Treatment Group 1 (First Digit):** {', '.join(map(str, treatment_group_1))} (Population: {treatment_population_1})")
            st.markdown(f"**Treatment Group 2 (First Digit):** {', '.join(map(str, treatment_group_2))} (Population: {treatment_population_2})")
            st.markdown(f"**Treatment Group 3 (First Digit):** {', '.join(map(str, treatment_group_3))} (Population: {treatment_population_3})")
            st.markdown(f"**Treatment Group 4 (First Digit):** {', '.join(map(str, treatment_group_4))} (Population: {treatment_population_4})")
            st.markdown(f"**Treatment Group 5 (First Digit):** {', '.join(map(str, treatment_group_5))} (Population: {treatment_population_5})")
            st.write("\n")
    else:
        st.write("Please select a valid number of tests (1, 2, or 3).")

# Step 6: Input from user to choose the number of tests
st.title("Balanced Splits for Control and Treatment Groups")
num_tests = st.radio("Choose the number of tests:", (1, 2, 3))
display_balanced_splits(num_tests)
