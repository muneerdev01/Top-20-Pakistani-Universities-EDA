import streamlit as st
import pandas as pd
import re
import os
import matplotlib.pyplot as plt
import seaborn as sns

# کلاؤڈ پر فائل کا نام براہ راست ریپوزٹری سے اٹھانے کے لیے
input_path = "Top_20_Pakistani_Universities.csv"

# اسٹریم لٹ پیج کی سیٹنگ
st.set_page_config(page_title="Pak Universities Quantum EDA", layout="wide")

st.title("🇵🇰 Top 20 Pakistani Universities - Quantum Analytics")
st.markdown("Welcome Muneer! This dashboard visualizes Quantum Metrics for top universities.")

if not os.path.exists(input_path):
    st.error(f"Error: Dataset not found at {input_path}. Please ensure the CSV is in the root folder.")
else:
    # Data Loading
    df = pd.read_csv(input_path)

    # --- Data Cleaning & Prep ---
    def parse_rank(val):
        match = re.search(r'(\d+)', str(val))
        if match:
            return int(match.group(1))
        return 700 
    
    df['QS_Numeric'] = df['QS Ranking (Asia)'].apply(parse_rank)
    df['Total Faculty'] = pd.to_numeric(df['Total Faculty'], errors='coerce').fillna(0)
    df['Total Students'] = pd.to_numeric(df['Total Students'], errors='coerce').fillna(1)
    
    # --- Quantum Metrics Calculation ---
    df['Gravity_Resistance'] = (df['Total Faculty'] / df['Total Students']) * 100
    df['Orbital_Stability'] = 700 - df['QS_Numeric']
    
    def count_programs(val):
        if pd.isna(val) or val == '':
            return 0
        return len(str(val).split(','))
        
    df['Innovation_Thrust'] = df['Programs Offered'].apply(count_programs)

    # --- UI Elements / Display ---
    
    # 1. Metrics Cards
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Universities Evaluated", len(df))
    col2.metric("Avg. Gravity Resistance", f"{df['Gravity_Resistance'].mean():.2f}%")
    col3.metric("Top Innovation Thrust Score", int(df['Innovation_Thrust'].max()))

    st.markdown("---")

    # 2. Data Table
    st.subheader("📊 Quantum Metrics Dataset")
    st.dataframe(df[['University Name', 'Gravity_Resistance', 'Orbital_Stability', 'Innovation_Thrust', 'Location']])

    st.markdown("---")

    # 3. Charts Section
    st.subheader("📈 Visual Insights")
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.write("**Innovation Thrust by University**")
        fig, ax = plt.subplots()
        sns.barplot(data=df.head(10), x='Innovation_Thrust', y='University Name', ax=ax, palette="viridis")
        st.pyplot(fig)

    with chart_col2:
        st.write("**Gravity Resistance vs Orbital Stability**")
        fig2, ax2 = plt.subplots()
        sns.scatterplot(data=df, x='Gravity_Resistance', y='Orbital_Stability', hue='Location', size='Total Students', ax=ax2)
        st.pyplot(fig2)
