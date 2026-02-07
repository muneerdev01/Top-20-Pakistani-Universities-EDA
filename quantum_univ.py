import pandas as pd
import re
import os

# Paths
# Dataset is in parent directory d:\EDA, script is in d:\EDA\Top-20-Pakistani-Universities
input_path = r"d:\EDA\Top_20_Pakistani_Universities.csv"
output_path = r"d:\EDA\Top-20-Pakistani-Universities\quantum_pak_universities.csv"

def main():
    if not os.path.exists(input_path):
        print(f"Error: Dataset not found at {input_path}")
        return

    print("Loading dataset...")
    df = pd.read_csv(input_path)

    # --- Data Cleaning & Prep ---
    
    # helper for QS Rank
    def parse_rank(val):
        # Extract first number found. e.g. "151-160" -> 151, "92" -> 92
        match = re.search(r'(\d+)', str(val))
        if match:
            return int(match.group(1))
        # If no number, return a low rank (numerically high)
        return 700 
    
    df['QS_Numeric'] = df['QS Ranking (Asia)'].apply(parse_rank)
    
    # Ensure numeric types for calculation
    df['Total Faculty'] = pd.to_numeric(df['Total Faculty'], errors='coerce').fillna(0)
    df['Total Students'] = pd.to_numeric(df['Total Students'], errors='coerce').fillna(1) # prevent div/0
    
    # --- Quantum Metrics Calculation ---

    # 1. Gravity_Resistance = (Faculty / Students) * 100
    df['Gravity_Resistance'] = (df['Total Faculty'] / df['Total Students']) * 100
    
    # 2. Orbital_Stability = Based on QS Ranking (Higher rank/lower numb = Higher stability)
    # Using 700 as base since max ranks go up to ~650
    df['Orbital_Stability'] = 700 - df['QS_Numeric']
    
    # 3. Innovation_Thrust = Based on variety of Programs Offered
    def count_programs(val):
        if pd.isna(val) or val == '':
            return 0
        # Split by comma
        return len(str(val).split(','))
        
    df['Innovation_Thrust'] = df['Programs Offered'].apply(count_programs)

    # --- Output ---
    df.to_csv(output_path, index=False)
    
    print("\n--- Quantum Metrics Calculated ---")
    print(df[['University Name', 'Gravity_Resistance', 'Orbital_Stability', 'Innovation_Thrust']].head().to_string())
    print(f"\nSaved quantum dataset to: {output_path}")

if __name__ == "__main__":
    main()
