# Hospitals Management System (HMS)

The Hospitals Management System (HMS) is a software platform designed to manage various aspects of a hospital's operations, including patient information, departments, doctors, and related workflows. The system allows for the creation, management, and reporting of patients and associated data.

## Features
### 1. Patient Management
- **Patient Model**: Contains information about hospital patients, including:
  - First name
  - Last name
  - Birth date
  - History (HTML)
  - CR Ratio (float)
  - Blood type (dropdown)
  - PCR (checkbox)
  - Image (upload image)
  - Address (text)
  - Age (auto-calculated based on birth date)
- **Patient Relationships**: Patients are associated with departments and doctors. Capacity for departments is displayed on the patient view.
- **Patient Log History**: Records are created with each change in patient state, showing the following information:
  - Created by
  - Date
  - Description of change

### 2. Departments
- **Department Model**: Defines various hospital departments with the following attributes:
  - Name
  - Capacity (integer)
  - Is_opened (boolean)
  - Associated patients

### 3. Doctors
- **Doctor Model**: Defines hospital doctors with the following information:
  - First name
  - Last name
  - Image

### 4. Business Rules
- Patients cannot be linked to closed departments.
- The doctors field is `many2many`, and should be read-only until the department is selected.
- First name and last name are mandatory fields.
- If the PCR field is checked, the CR ratio field must be specified.
- The history field is hidden if the age is less than 50.
- The PCR field is automatically checked if the age is under 30, with a warning message.

### 5. Customer Relationship Management (CRM)
- The patient model is linked to the customers model from the CRM module with a new field, `related_patient_id`.
- A constraint prevents linking patients with emails that are already assigned to different customers.
- Prevent users from deleting any customer linked to a patient.
- Show the website field in the list view for customers.
- The Tax ID field is mandatory for CRM customers.

### 6. User Permissions and Roles
- **Manager Group**: Grants the following access rights:
  - Create/read/update/delete all patient records
  - Create/read/update/delete departments
  - Create/read/update/delete doctors
  - View doctor fields in patient forms
  - Access the doctors menu item

### 7. Patient Report
- A custom report template for patients, including:
  - Patient's name
  - Age
  - Department name
  - Associated doctors
  - Birth date
  - PCR
  - Blood type
  - Email
  - Log history

## Additional Considerations
- Patient's age should be auto-calculated based on the birth date.
- Implement data validation for fields like email to ensure uniqueness and correct formatting.
- Integrate error handling for scenarios 
