import streamlit as st
import pandas as pd
import joblib

# 🧠 Step 1: Load the trained model
model = joblib.load("random_forest_model.joblib")

# 🏷 Step 2: Page title
st.title("Kraljic Matrix Category Predictor")
st.write("Predict the Kraljic Category of a product based on supplier and risk parameters.")

# 📝 Step 3: User input form
with st.form(key='kraljic_form'):
    st.subheader("Enter Product Details:")

    product_name = st.selectbox("Product Name", [
        'Semiconductors', 'Pharma APIs', 'Lithium Batteries', 'AI Chips',
        'Customized Valves', 'Rare Earth Metals', 'Specialty Gases',
        'Catalysts', 'Standard Bolts', 'PVC Pipes', 'Packaging Material',
        'Steel Beams', 'Cleaning Supplies', 'Uniforms', 'Printer Ink',
        'Office Stationery'
    ])

    supplier_region = st.selectbox("Supplier Region", [
        'South America', 'Asia', 'Africa', 'Europe', 'North America', 'Global'
    ])

    lead_time_days = st.number_input("Lead Time (Days)", min_value=0, step=1)
    order_volume_units = st.number_input("Order Volume (Units)", min_value=0, step=1)
    cost_per_unit = st.number_input("Cost per Unit", min_value=0.0, step=0.01)
    
    supply_risk_score = st.slider("Supply Risk Score (1-5)", 1, 5, 3)
    profit_impact_score = st.slider("Profit Impact Score (1-5)", 1, 5, 3)
    environmental_impact = st.slider("Environmental Impact Score (1-5)", 1, 5, 3)
    single_source_risk = st.selectbox("Single Source Risk", ["Yes", "No"])

    submit_button = st.form_submit_button(label="Predict Kraljic Category")

# 🧩 Step 4: Prediction
if submit_button:
    # Prepare input for the model
    input_df = pd.DataFrame([{
        'Product_Name': product_name,
        'Supplier_Region': supplier_region,
        'Lead_Time_Days': lead_time_days,
        'Order_Volume_Units': order_volume_units,
        'Cost_per_Unit': cost_per_unit,
        'Supply_Risk_Score': supply_risk_score,
        'Profit_Impact_Score': profit_impact_score,
        'Environmental_Impact': environmental_impact,
        'Single_Source_Risk': single_source_risk
    }])

    # Predict
    prediction = model.predict(input_df)[0]

    st.success(f"Predicted Kraljic Category: *{prediction}*")