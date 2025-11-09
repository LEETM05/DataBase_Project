# Medicine-Project

## 📖 Description
This project is a web application that allows users to take pictures of pills and receive information about them. It uses a YOLOv5 model trained on AI Hub's 'Oral Medicine Image Data' to identify the pills.

## ✨ Features
- User authentication (login, logout, signup)
- Take a picture of a pill
- View information about the pill
- View history of pill searches

## 🛠 Technologies Used
- Django
- HTML/CSS
- JavaScript
- YOLOv5

## 🤖 AI Model and Data
- **AI Model**: The project uses the YOLOv5 model for object detection to identify pills from images.
- **Data**: The model was trained on the 'Oral Medicine Image Data' from [AI Hub](https://www.aihub.or.kr/).

## ⚙️ Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Medicine-project.git
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Run database migrations:
   ```bash
   python manage.py migrate
   ```
4. Run the development server:
    ```bash
    python manage.py runserver
    ```

## 🚀 Usage
1. Create an account and log in.
2. Go to the camera page and take a picture of a pill.
3. The application will identify the pill and show you information about it.
4. You can view your search history on the history page.
