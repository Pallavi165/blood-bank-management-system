** Blood Bank Management System

**A Blood Bank Management System developed using Python and MySQL to manage donor information, blood inventory, and blood requests efficiently.

** Overview

**This project helps blood banks and healthcare organizations maintain donor records and monitor blood stock availability. It provides a simple command-line interface for performing common operations such as adding donors, searching donor records, updating inventory, and fulfilling blood requests.

** Features
**
* Add donor information
* View all registered donors
* Search donors by blood group
* Manage blood stock inventory
* Process blood requests
* Store and retrieve data using MySQL
* Modular Python code structure

** Tech Stack
**
| Technology             | Purpose                 |
| ---------------------- | ----------------------- |
| Python                 | Application Logic       |
| MySQL                  | Database Management     |
| mysql-connector-python | Database Connectivity   |
| Git                    | Version Control         |
| GitHub                 | Source Code Hosting     |
| VS Code                | Development Environment |

** Project Structure**

```text
blood_bank/
│
├── main.py
├── database.py
├── models.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

** Database Design
**
 **Donors Table**

| Field       | Type         |
| ----------- | ------------ |
| id          | INT          |
| name        | VARCHAR(100) |
| age         | INT          |
| blood_group | VARCHAR(5)   |
| contact     | VARCHAR(15)  |

** Blood Stock Table
**
| Field       | Type       |
| ----------- | ---------- |
| blood_group | VARCHAR(5) |
| units       | INT        |

** Installation
**
```bash
git clone https://github.com/Pallavi165/blood-bank-management-system.git
cd blood-bank-management-system

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
python main.py
```

 **Sample Output**


--- Blood Bank System ---
1. Add Donor
2. View Donors
3. Search Donor
4. Add Blood Stock
5. Request Blood
6. Exit
```

** Future Enhancements
**
* Flask-based web application
* Authentication and authorization
* Blood donation history tracking
* Dashboard and analytics
* Email and SMS notifications
* Report generation

 Author

**Pallavi**

GitHub: https://github.com/Pallavi165


This project is intended for educational and academic purposes.
