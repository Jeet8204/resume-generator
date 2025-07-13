# 📝 Resume Generator (Django + PDFKit)

A Django-based web application that allows users to generate professional, printable PDF resumes by filling out a simple form. It supports user authentication, dynamic data handling, and automatic resume delivery via email.

---

## 🚀 Features

- 🔐 **User Authentication** (Login required to generate resumes)
- 📄 **Resume Builder** form with fields for education, work experience, skills, and summary
- 🧠 **Dynamic PDF generation** using HTML templates + `pdfkit` + `wkhtmltopdf`
- 📧 **Email integration** to send the PDF resume to the user automatically
- 📂 **Admin dashboard** to view all resume submissions
- 📋 **PDF Preview in browser**

---

## 📸 Screenshots

> *(Add screenshots here if you'd like. For now, placeholders:)*

- 🖥️ Resume Form: `/accept/`
- 📄 PDF Preview: `/<id>/`
- 🔒 Login: `/accounts/login/`

---

## 🛠 Tech Stack

- **Backend**: Django (Python)
- **PDF Generation**: [`pdfkit`](https://pypi.org/project/pdfkit/) + `wkhtmltopdf`
- **Email**: Django Email backend (SMTP)
- **Authentication**: Django’s built-in auth system
- **Database**: SQLite (default), easy to switch to PostgreSQL
- **Frontend**: Django templates (HTML, Bootstrap optional)

---

## 📦 Installation

### ⚙️ Prerequisites

- Python 3.8+
- pip
- `wkhtmltopdf` installed and accessible in PATH

### 🧪 Clone and set up

```bash
git clone https://github.com/Jeet8204/resume-generator.git
cd resume-generator
python -m venv venv
source venv/bin/activate     # or venv\Scripts\activate on Windows
pip install -r requirements.txt
