# CheatWall: A Proctoring System for Exams

## Overview

CheatWall is a web-based test evaluation system designed to facilitate virtual proctoring and result management for online exams. It provides teachers with a platform to create virtual classrooms, monitor student proctoring results, and manage access to these results securely.

**Key Features:**

* **Virtual Classroom Creation:** Teachers can create virtual classrooms for their exams.
* **Student Proctoring Result Display:** Proctoring results are displayed in a tabular format for easy review.
* **Access Code Generation:** A unique access code is generated for each virtual classroom, controlling access to student results.
* **Secure Authentication and Communication:** RESTful APIs ensure secure authentication and data exchange.
* **User-Friendly Interface:** Built with HTML, CSS, and JavaScript for an intuitive frontend.
* **Robust Backend:** Powered by Django for efficient data management and server-side logic.

## Technologies Used

* **Frontend:**
    * HTML5
    * CSS3
    * JavaScript
* **Backend:**
    * Django (Python)
* **API:**
    * RESTful APIs

## Installation and Setup

1.  **Clone the Repository:**
    ```bash
    git clone <your_repository_link>
    cd CheatWall
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    ```
    * **Windows:**
        ```bash
        venv\Scripts\activate
        ```
    * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

6.  **Access the Application:**
    Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Sample Screenshots

* **Main Page:**
    * `![Main Page](pictures\Main-page.png)`
* **User Main Page:**
    * `![User Main Page](pictures\User-page.png)`
* **Creating Virtual Class:**
    * `![Create Virtual Class](pictures\Creating-Virtualclass.png)`
* **Access Code:**
    * `![Access Code](pictures\Accesscode.png)`
* **Managing Access Code of Different Virtual Class:**
    * `![Managing Access Codes](pictures\Managing-Virtualclasscode.png)`
* **Managing Student Response Result:**
    * `![Managing Student Responses](pictures\Studentsresponse.png)`


## Usage

1.  **Teacher Login/Registration:** Teachers can create accounts and log in to the system.
2.  **Create a Virtual Classroom:** Teachers can create virtual classrooms for their exams, generating a unique access code.
3.  **Share Access Code:** Teachers share the access code with their students.
4.  **Student Submission:** Students submit their proctoring results using the provided access code.
5.  **View Results:** Teachers can view student proctoring results in a tabular format within the virtual classroom.
6.  **Manage Access:** Teachers can manage and revoke access codes as needed.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bug fixes, feature requests, or improvements.
