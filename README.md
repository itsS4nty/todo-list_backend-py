# ToDo List - Backend

This guide will walk you through the setup, installation, and running processes to get your backend up and running.

## Prerequisites

Before running the project, make sure you have the following installed:

-   **PostgreSQL**: Ensure [PostgreSQL](https://www.postgresql.org/) is installed and running on your machine.
-   **Python**: This project requires Python3. You can download it from [the official Python website](https://www.python.org/).

## Setup Instructions

### Database Setup

1. Create a PostgreSQL database with a name of your choice. For example, `todo`.

### Project Setup

2. Clone the repository to your local machine.
3. Install the project packages by running:

```bash
pip install -r requirements.txt
```

4. Create a .env file at the root of the project. Follow the structure provided in the [.env.example](.env.example) file.

### Running the Project Locally

To run the project on your local machine:

```bash
uvicorn main:app --reload
```

This command starts the server on the port specified in your `.env` file, or by default on port 3030.

### Using Postman for testing

The project includes a Postman collection for testing the backend without a frontend:

-   Navigate to the postman folder at the root of the project.
-   Import the collection into Postman.
-   Make sure the server is running as described in the [Running the Project Locally](#running-the-project-locally) section.
-   You can now test the backend directly from Postman.
