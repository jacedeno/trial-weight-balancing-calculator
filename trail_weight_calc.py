import streamlit as st

# Display a title for your app
st.title('Fan Balancing Helper by Jose Cedeno')

# Use Streamlit's input widgets instead of input()
fan_mass = st.number_input("Enter the mass of the fan in kilograms:", min_value=0.0, format='%f')
rotor_radius = st.number_input("Enter the rotor radius in meters:", min_value=0.0, format='%f')
max_speed_rpm = st.number_input("Enter the maximum operating speed in RPM:", min_value=0, format='%d')

# You can add a button to perform the calculation
if st.button('Calculate Suggested Trial Weight'):
    # The calculation logic remains the same
    trial_weight_percentage = 0.1  # Starting with 0.1% of the fan's mass
    trial_weight = (fan_mass * 1000 * trial_weight_percentage / 100) * (rotor_radius * max_speed_rpm / 10000)

    # Use Streamlit's way to display the output instead of print()
    st.write(f"Suggested trial weight is: {trial_weight:.2f} grams")

# Note about the illustrative purposes of the app
st.markdown("""
*Note: This tool is for illustrative purposes and the calculations for suggesting a trial weight
should ideally be based on detailed guidelines from equipment manufacturers or balancing experts.
The percentages and factors used here may need to be adjusted to suit specific cases.*
""")
