# Ben Developer Server

This is a Django project for managing a portfolio website.

## Project Structure

- `ben_developer_server/urls.py`: URL configuration for the project.
- `templates/portfolio/index.html`: HTML template for the portfolio index page.
- `programs/views.py`: Views for the programs app.

## Requirements

- Python 3.x
- Django 3.x

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ben_developer_server.git
    cd ben_developer_server
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Server

1. Apply migrations:
    ```sh
    python manage.py migrate
    ```

2. Run the development server:
    ```sh
    python manage.py runserver
    ```

3. Open your browser and go to `http://127.0.0.1:8000/` to see the portfolio website.

## Project URLs

- `/`: Portfolio index page.
- `/admin/`: Admin site.

## License

This project is licensed under the MIT License.