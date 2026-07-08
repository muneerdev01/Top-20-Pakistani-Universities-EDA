import streamlit as st
import pandas as pd
import re
import os

# کلاؤڈ پر فائل کا پاتھ
input_path = "Top_20_Pakistani_Universities.csv"

# 1. پیج کی کنفیگریشن اور ڈارک موڈ فورس کرنا
st.set_page_config(
    page_title="Top-20-Pakistani-Universities-EDA",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. کسٹم CSS انجکشن - ہوبہو سائبر پنک گلو اور بلیک کارڈز کے لیے
st.markdown("""
    <style>
    /* مین بیک گراؤنڈ ڈارک کرنا */
    .stApp {
        background-color: #060913;
        color: #ffffff;
    }
    /* نیون گلو ہیڈنگ */
    .quantum-header {
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
        font-size: 50px;
        font-weight: bold;
        color: #63ffb4;
        text-shadow: 0 0 10px #63ffb4, 0 0 30px #20c997;
        margin-bottom: 5px;
    }
    .quantum-subtitle {
        text-align: center;
        color: #8ab4f8;
        font-size: 16px;
        margin-bottom: 30px;
    }
    /* کسٹم کواڈنٹ کارڈز */
    .university-card {
        background-color: #0b111e;
        border: 1px solid #1e293b;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    .card-title {
        font-size: 16px;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 2px;
    }
    .card-location {
        font-size: 12px;
        color: #a0aec0;
        margin-bottom: 15px;
    }
    /* پروگریس بار لیبلز */
    .metric-label {
        font-size: 11px;
        font-weight: bold;
        letter-spacing: 1px;
        margin-top: 8px;
        margin-bottom: 2px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. مین ہیڈنگز
st.markdown('<div class="quantum-header">Top-20-Pakistani-Universities-EDA</div>', unsafe_allow_html=True)
st.markdown('<div class="Top-20-Pakistani-Universities-EDA">🚀 My First Dataset "University Rankings • Pakistan Sector"</div>', unsafe_allow_html=True)

if not os.path.exists(input_path):
    st.error(f"Error: Dataset not found at {input_path}")
else:
    df = pd.read_csv(input_path)

    # --- ڈیٹا کی صفائی اور کیلکولیشنز ---
    def parse_rank(val):
        match = re.search(r'(\d+)', str(val))
        if match:
            return int(match.group(1))
        return 700 
    
    df['QS_Numeric'] = df['QS Ranking (Asia)'].apply(parse_rank)
    df['Total Faculty'] = pd.to_numeric(df['Total Faculty'], errors='coerce').fillna(0)
    df['Total Students'] = pd.to_numeric(df['Total Students'], errors='coerce').fillna(1)
    
    # فارمولے
    df['Gravity_Resistance'] = (df['Total Faculty'] / df['Total Students']) * 100
    df['Orbital_Stability'] = 700 - df['QS_Numeric']
    
    def count_programs(val):
        if pd.isna(val) or val == '':
            return 0
        return len(str(val).split(','))
    df['Innovation_Thrust'] = df['Programs Offered'].apply(count_programs)

    # --- میپ ڈیٹا میپنگ ---
    coordinates = {
        'Islamabad': [33.6844, 73.0479],
        'Lahore, Punjab': [31.5204, 74.3587],
        'Karachi, Sindh': [24.8607, 67.0011],
        'Topi, Khyber Pakhtunkhwa': [34.0700, 72.6200],
        'Faisalabad, Punjab': [31.4504, 73.1350],
        'Peshawar, Khyber Pakhtunkhwa': [34.0151, 71.5249],
        'Quetta, Balochistan': [30.1798, 66.9750],
        'Jamshoro, Sindh': [25.4300, 68.2600],
        'Islamabad (Multiple Cities)': [33.6844, 73.0479]
    }
    
    df['lat'] = df['Location'].map(lambda x: coordinates.get(x, [33.6844, 73.0479])[0])
    df['lon'] = df['Location'].map(lambda x: coordinates.get(x, [33.6844, 73.0479])[1])

    # ----------------------------------------------------
    # 🌍 نقشہ کا سیکشن
    # ----------------------------------------------------
    st.markdown("### 🗺️ Quantum Matrix Map")
    st.map(df, latitude='lat', longitude='lon', size=20, color='#63ffb4')

    # 🔍 سرچ بار
    search_query = st.text_input("🔍 Search Quantum Coordinates (Name or City)...", "")
    
    if search_query:
        filtered_df = df[df['University Name'].str.contains(search_query, case=False) | df['Location'].str.contains(search_query, case=False)]
    else:
        filtered_df = df

    st.markdown("<br><br>", unsafe_allow_html=True)

    # ----------------------------------------------------
    # 🗂️ گرڈ اور پروگریس کارڈز (فکسڈ سنٹیکس کے ساتھ)
    # ----------------------------------------------------
    st.markdown("### 📊 Quantum Coordinates Grid")
    
    cols = st.columns(3)
    
    for idx, row in filtered_df.reset_index(drop=True).iterrows():
        col_selector = idx % 3
        with cols[col_selector]:
            # کارڈ کا بیرونی ڈھانچہ
            st.markdown(f"""
                <div class="university-card">
                    <div style="float: right; background-color: #1e293b; padding: 2px 6px; border-radius: 4px; font-size: 10px; color: #63ffb4; font-weight: bold;">
                        R- {row["QS_Numeric"]}
                    </div>
                    <div class="card-title">{row["University Name"]}</div>
                    <div class="card-location">📍 {row["Location"]}</div>
                </div>
            """, unsafe_allow_html=True)
            
            # 1. Gravity Resistance (اندر اب ڈبل کوٹس استعمال کیے ہیں تاکہ ایرر نہ آئے)
            grav_text = f'{row["Gravity_Resistance"]:.1f}%'
            st.markdown(f'<div class="metric-label" style="color: #00d2ff;">⚡ GRAVITY RES. <span style="float:right;">{grav_text}</span></div>', unsafe_allow_html=True)
            grav_val = min(float(row["Gravity_Resistance"]) / 20.0, 1.0) 
            st.progress(grav_val)
            
            # 2. Orbital Stability
            orb_text = f'{int(row["Orbital_Stability"])}'
            st.markdown(f'<div class="metric-label" style="color: #63ffb4;">✨ ORB. STABILITY <span style="float:right;">{orb_text}</span></div>', unsafe_allow_html=True)
            orb_val = min(float(row["Orbital_Stability"]) / 700.0, 1.0)
            st.progress(orb_val)
            
            # 3. Innovation Thrust
            thrust_text = f'{int(row["Innovation_Thrust"])}'
            st.markdown(f'<div class="metric-label" style="color: #b76eff;">🚀 THRUST <span style="float:right;">{thrust_text}</span></div>', unsafe_allow_html=True)
            thrust_val = min(float(row["Innovation_Thrust"]) / 10.0, 1.0)
            st.progress(thrust_val)
            
            st.markdown("<br>", unsafe_allow_html=True)
