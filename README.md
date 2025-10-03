# SIO – Secure Online Store

## 📌 Description

This project was developed as an academic project at the **University of Aveiro**, for the course **Information and Organisational Security (SIO)**. The goal was to present a web application that would serve as an online shop to sell DETI memorabilia.  

The purpose of this delivery was to improve upon the first version of the project, enhancing the security of the application and adding new features. The **main focus was on security**, so the **front-end is not fully completed**.

## 🔐 Key Issues Addressed

During development, the project addressed various security issues, including:

- **2.1.2**: Authentication and access control  
- **2.1.7**: SQL injection protection  
- **2.1.8**: Input validation and sanitization  
- **2.2.1**: Encryption of sensitive data  
- **2.2.3**: Secure session management  
- **3.2.3 & 3.4.X**: Cross-Site Scripting (XSS) protection  
- **3.3.2**: Cross-Site Request Forgery (CSRF) protection  
- **4.2.2 & 13.2.3**: Secure password and credential management  
- **4.3.1**: Security logging  
- **5.3.6**: Brute-force attack protection  
- **8.3.2**: Content Security Policy (CSP)  
- **11.1.4**: Security monitoring and incident response  
- **14.2.3**: Compliance with data protection regulations (e.g., GDPR)

## 🛠 Features Implemented

From the list of software features given by the teacher, we implemented the following:

- **Password strength evaluation**: requiring at least 12 characters and at most 128 according to v2.1 of the ASVS, with breach verification using the Have I Been Pwned API.  
- **Multi-factor authentication**: implemented with TOTP (Time-based One-Time Password) to authorize access to the application.  
- **Encryption of sensitive data**: including passwords and the key used to generate the TOTP.  

Other functionalities include:

- Product catalog  
- Shopping cart  
- User management (registration, login, account management)  
- Administration panel for products and orders

## RUN

1. Create the virtual environment:
```bash
python3 -m venv venv
```
2. Activate the virtual environment (Every time you open a new terminal you need to do this to make the virtual environment the default Python interpreter of this shell):
```bash
source venv/bin/activate
```
or (Windows):
```bash
.\venv\Scripts\activate.ps1
```

3. Install the requirements:
```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
./run.sh app_sec <PORT>
```

&emsp;&emsp;In Windows use instead:

```bash
.\run.bat app_sec <PORT>
```
5. Access the website:

```bash
http://127.0.0.1:<PORT>
```

6. To generate the database you need to access the following link:

```bash
/generate/all
```
