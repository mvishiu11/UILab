import streamlit as st
from datetime import datetime, time
import pytz

def main():
    st.title("Job Offer Form")

    with st.form(key='job_offer_form'):
        # Job Title
        job_title = st.text_input("Job Title", "", help="Enter the job title. Maximum 100 characters.")

        # Job Description
        job_description = st.text_area("Job Description", "", help="Provide a detailed job description. Maximum 1000 characters.")

        # Department Name
        department_name = st.selectbox("Department Name", options=["Finance", "IT", "HR", "Sales", "Marketing", "Other"], help="Select the department from the dropdown list.")

        new_dept = None
        if department_name == "Other":
            new_dept = st.text_input("New Department Name", help="Enter the new department name. Maximum 50 characters.")
            st.rerun()
        
        # Number of Available Positions
        num_positions = st.number_input("Number of Available Positions", min_value=1, step=1, format="%d", help="Enter the number of positions available. Must be a positive integer.")

        # Salary Range and Currency
        col1, col2, col3 = st.columns(3)
        with col1:
            salary_from = st.number_input("Salary From", help="Minimum salary for the position.")
        with col2:
            salary_to = st.number_input("Salary To", help="Maximum salary for the position.")
        with col3:
            currency = st.selectbox("Currency", ["USD", "EUR", "GBP"], help="Choose the currency for the salary.")

        # Start Date
        start_date = st.date_input("Start Date", min_value=datetime.today(), help="Select the start date for the position. Dates in the past are not allowed.")

        # Working Hours
        col1, col2, col3 = st.columns([1,1,2])
        with col1:
            opening_hours = st.time_input("Opening Hours", value=time(9, 0), help="Select opening hour.")
        with col2:
            closing_hours = st.time_input("Closing Hours", value=time(17, 0), help="Select closing hour.")
        with col3:
            timezone = st.selectbox("Timezone", pytz.all_timezones, index=pytz.all_timezones.index('UTC'), help="Select the timezone for the working hours.")

        # Contact Information
        contact_email = st.text_input("Contact Email", "", help="Enter a valid email address.")
        
        col5, col4 = st.columns([1,3])
        with col4:
            contact_name = st.text_input("Contact Number", "", help="Enter the phone number in format 111-222-333")
        with col5:
            phone_extension = st.text_input("Phone Extension", "", help="Enter the phone extension if any.")

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