import streamlit as st
import json
from src.equipment_calculator import calculate_cranes, calculate_trucks

# Load input data
with open("data/input_parameters.json") as f:
    params = json.load(f)

st.title("⚓ Container Terminal Equipment Planner")

# Inputs
capacity = st.number_input("Annual Capacity (TEUs)", value=params["annual_capacity"])
productivity = st.number_input("Crane Productivity (containers/hr)", value=params["crane_productivity"])
hours = st.number_input("Annual Operating Hours", value=params["hours_per_year"])
ratio = st.number_input("40’/20’ Ratio", value=params["ratio_40_20"])

cranes_needed = round(calculate_cranes(capacity, productivity, hours, ratio))
st.metric("Required Quay Cranes", cranes_needed)

trucks_needed = round(calculate_trucks(
    params["daily_demand"], params["truck_loading_time"], params["truck_unloading_time"],
    params["truck_distance"], params["truck_speed"], params["truck_availability"],
    params["truck_shifts"], params["shift_hours"]
))
st.metric("Required Trucks", trucks_needed)
