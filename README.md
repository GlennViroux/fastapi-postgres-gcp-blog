# FastAPI PostgreSQL Blog Post Sample Code

This repository serves as a guide on how to connect a FastAPI application to a PostgreSQL database and deploy the whole application to GCP.

## Introduction

In the blog post, we explore the process of building a RESTful API using FastAPI and PostgreSQL, and deploying it to Google Cloud Platform (GCP) using Cloud Run. The code in this repository serves as a practical example.

## Getting Started

To get started with the code in this repository, follow these steps:

1. Clone the repository
2. Install the required dependencies: `poetry install`
3. Copy the `.env.example` file to `.env` and update the database credentials.
4. Run the database migrations: `poetry run aerich upgrade`
5. Start the FastAPI application: `poetry run uvicorn main:app --reload`

## Contributing

If you'd like to contribute to this project, feel free to open a pull request. We welcome any improvements, bug fixes, or additional features.

Before submitting a pull request, make sure to run the tests: `poetry run pytest`.

## License

The code in this repository is licensed under the [MIT License](license). You are free to use, modify, and distribute it as per the terms of the license.

## Contact

If you have any questions or feedback, you can reach out to the author of the blog post or open an issue in this repository.

Happy coding!
