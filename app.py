import streamlit as st
import pandas as pd
import re
import os
import matplotlib.pyplot as plt
import seaborn as sns

# کلاؤڈ پر فائل کا نام
input_path = "Top_20_Pakistani_Universities.csv"

# اسٹریم لٹ پیج کی سیٹنگ
st.set_page_config(page_title="Pak Universities Quantum EDA", layout="wide")

st.title("🇵🇰 Top 20 Pakistani Universities - Quantum Analytics")
st.markdown("Welcome Muneer! Use the sidebar filters to interact with the dashboard.")

if not os.path.exists(input_path):
    st.error(f"Error: Dataset not found at {input_path}.")
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

    # ----------------------------------------------------
    # 🕹️ متحرک فلٹرز (Interactive Sidebar Filters)
    # ----------------------------------------------------
    st.sidebar.header("🎯 Dashboard Control Panel")
    
    # لوکیشن فلٹر (Unique locations list)
    all_locations = ["All Locations"] + list(df['Location'].unique())
    selected_location = st.sidebar.selectbox("Filter by City / Province:", all_locations)
    
    # سٹوڈنٹس کی تعداد کا سلائیڈر (Slider to filter by student count)
    min_students = int(df['Total Students'].min())
    max_students = int(df['Total Students'].max())
    student_range = st.sidebar.slider("Select Minimum Students:", min_students, max_students, min_students)

    # ڈیٹا کو فلٹر کرنا (Filtering the DataFrame based on user inputs)
    filtered_df = df[df['Total Students'] >= student_range]
    if selected_location != "All Locations":
        filtered_df = filtered_df[filtered_df['Location'] == selected_location]

    # ----------------------------------------------------
    # 📊 اپڈیٹڈ ڈسپلے (Filtered Data Display)
    # ----------------------------------------------------
    
    # 1. Dynamic Metrics Cards
    col1, col2, col3 = st.columns(3)
    col1.metric("Filtered Universities", len(filtered_df))
    col2.metric("Avg. Gravity Resistance", f"{filtered_df['Gravity_Resistance'].mean():.2f}%" if len(filtered_df)>0 else "0%")
    col3.metric("Top Innovation Thrust", int(filtered_df['Innovation_Thrust'].max()) if len(filtered_df)>0 else 0)

    st.markdown("---")

    # 2. Data Table (User can sort by clicking column headers)
    st.subheader("📊 Quantum Metrics Dataset (Click column headers to sort!)")
    st.dataframe(filtered_df[['University Name', 'Gravity_Resistance', 'Orbital_Stability', 'Innovation_Thrust', 'Location', 'Total Students']])

    st.markdown("---")

    # 3. Dynamic Charts Section
    st.subheader("📈 Visual Insights")
    
    if len(filtered_df) > 0:
        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            st.write(f"**Innovation Thrust ({selected_location})**")
            fig, ax = plt.subplots()
            # Show top 10 from the filtered list
            sns.barplot(data=filtered_df.head(10), x='Innovation_Thrust', y='University Name', ax=ax, palette="viridis")
            plt.xticks(rotation=0)
            st.pyplot(fig)

        with chart_col2:
            st.write("**Gravity Resistance vs Orbital Stability**")
            fig2, ax2 = plt.subplots()
            sns.scatterplot(data=filtered_df, x='Gravity_Resistance', y='Orbital_Stability', hue='Location', size='Total Students', ax=ax2, sizes=(40, 400))
            st.pyplot(fig2)
    else:
        st.warning("No universities match the selected criteria. Try adjusting the filters in the sidebar!")
