import streamlit as st
from datetime import datetime

def main():
    st.title("Job Offer Form")
    
    default_dept = ["Finance", "IT", "HR", "Sales", "Marketing", "Other"]

    # Initialize session state to hold the list of departments
    if 'departments' not in st.session_state:
        st.session_state['departments'] = default_dept

    with st.form(key='job_offer_form'):
        # Job Title
        job_title = st.text_input("Job Title", "", help="Enter the job title. Maximum 100 characters.")
        
        # Job Description
        job_description = st.text_area("Job Description", "", help="Provide a detailed job description. Maximum 1000 characters.")

        # Department Name
        department_name = st.selectbox("Department Name", options=st.session_state['departments'], help="Select the department from the dropdown list or add a new one below.")

        new_dept = None
        # Add new department field shows only if 'Other' is selected
        if department_name == "Other":
            new_dept = st.text_input("Other Department", help="Type here to add a new department to the list. Maximum 50 characters.")
            
        # Number of Available Positions
        num_positions = st.number_input("Number of Available Positions", min_value=1, step=1, format="%d", help="Enter the number of positions available. Must be a positive integer.")

        # Salary Range
        salary_from = st.number_input("Salary From ($)", min_value=0.0, step=1000.0, format="%.2f", help="Minimum salary for the position. Must be a positive number.")
        salary_to = st.number_input("Salary To ($)", min_value=0.0, step=1000.0, format="%.2f", help="Maximum salary for the position. Must be greater than or equal to the Salary From.")

        # Start Date
        start_date = st.date_input("Start Date", min_value=datetime.today(), help="Select the start date for the position. Dates in the past are not allowed.")

        # Ability to Attach Promotion Graphic Files
        promotion_graphics = st.file_uploader("Attach Promotion Graphic Files", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'],
                                            help="Attach promotional graphics. Only PNG, JPG, JPEG files are accepted. Recommended size limit per file is 5MB.")

        # Contact Information
        contact_email = st.text_input("Contact Email", "", help="Enter a valid email address.")
        contact_phone = st.text_input("Contact Phone Number", "", help="Enter the phone number. Include country code if applicable.")
        office_hours = st.text_input("Office Working Hours", "", help="Enter office working hours in format '9:00 AM - 5:00 PM'.")

    # Submit Button
        submit_button = st.form_submit_button("Submit Job Offer")

    if submit_button:
        if validate_form(job_title, job_description, department_name, new_dept):
            # Process form data here (e.g., save to database)
            st.success("Job Offer Submitted Successfully!")
        else:
            st.error("Please correct the errors in the form.")

def validate_form(job_title, job_description, department_name, new_dept):
    # Validation logic
    is_valid = True
    errors = []

    # Check required fields
    if not job_title:
        errors.append("Job title is required.")
    if not job_description:
        errors.append("Job description is required.")
    if department_name == "Other" and not new_dept:
        errors.append("New department name is required when 'Other' is selected.")
    if new_dept and (new_dept in st.session_state['departments']):
        errors.append("This department already exists.")
    if new_dept and len(new_dept) > 50:
        errors.append("Department name must be 50 characters or less.")

    # Display errors
    if errors:
        for error in errors:
            st.warning(error)
        is_valid = False

    return is_valid

if __name__ == "__main__":
    main()