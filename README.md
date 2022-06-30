# newsfeed_portal

- Python version: 3.8+

- Django version: 3.2.13

- DRF version: 3.13.1

- Database: PostgreSQL, Redis

- Vue version: Vue2

- NodeJS version: 16.13.2

---

## Project Setup

- Clone the project

  ```bash
  git clone https://github.com/adnan-alam/newsfeed_portal
  ```

### Backend

- Create a **.env** file inside the project directory and copy from **env_example** to **.env** and set the environment variables according to the needs.

- Create a virtual environment named **env** with Python's **venv**:

  ```bash
  python3.8 -m venv env
  ```

  - Activate the virtual environment (For Ubuntu):
    ```bash
    source env/bin/activate
    ```

- Install all Python the dependencies

  ```bash
  pip install -r requirements.txt
  ```

- Run database migrations:

  ```bash
  ./manage.py migrate
  ```

- Create Superuser:

  ```bash
  ./manage.py createsuperuser
  ```

  need to provide the username, email and password.

- Run the development server

  ```bash
  ./manage.py runserver
  ```

  and the Django server will be available on `http://127.0.0.1:8000/`.

- Before fetching news, we need to populate the News sources from the `newsapi.org`. To populate the news sources, execute the command:

  ```bash
  ./manage.py populate_news_sources
  ```

- For task scheduling, **huey** Python package is being used. It has dependency of **Redis**, so it must be installed on the system. Run the consumer:

  ```bash
  ./manage.py run_huey
  ```

### Frontend

- Go to **frontend** directory, install packages:

  ```
  npm install
  ```

- Run the development server:
  ```
  npm run dev
  ```
  frontend will be available on `http://127.0.0.1:8080/`.
