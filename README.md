
# Image Enhancer

Web application (React + Django) for performing a neural style transfer (NST) that adopts a
style from one image to another while preserving its content.

Based on NST implementation from [Hugging Face](https://huggingface.co/spaces/georgescutelnicu/neural-style-transfer)


## Run Locally

### Prerequisites

This application uses Python 3.9

### How to run

Clone the project

```bash
  git clone https://github.com/Fadion96/image_enhancer
```

Go to the project directory

```bash
  cd image_enhancer/
```

Install backend required libraries

```bash
  pip install -r requirements.txt
```

Install frontend dependencies

```bash
  cd frontend/
  npm install
```

Migrate models to the database and run the server

```bash
  cd backend/
  python manage.py migrate
  python manage.py runserver
```

Run frontend

```bash
  cd frontend/
  npm start
```

## Screenshots

![Login page](/extras/login_page.png)

![Results](/extras/gallery.png)
