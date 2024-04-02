# Title of the app
st.title('Unbalance weight/radius calculator by Jose Cedeno')

# User inputs for the reference conditions
st.header('Reference Conditions')
reference_radius = st.number_input('Enter the reference radius in inches:', value=10.0, format="%.2f")
reference_weight_grams = st.number_input('Enter the reference weight in grams:', value=28.35, format="%.2f")

# User input for the radius for which the trial weight is to be calculated
st.header('Calculation Parameters')
input_radius = st.number_input('Enter the radius for which you want to calculate the trial weight in inches:', value=10.0, format="%.2f")

# Calculate the trial weight based on the user inputs
if st.button('Calculate Trial Weight'):
    trial_weight_grams = reference_weight_grams * (reference_radius / input_radius)
    st.write(f"Based on the reference conditions ({reference_weight_grams} grams at a radius of {reference_radius} inches),")
    st.write(f"the suggested trial weight for a radius of {input_radius} inches is: {trial_weight_grams:.2f} grams")
