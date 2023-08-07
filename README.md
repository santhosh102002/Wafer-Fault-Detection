# WaferFault Detection Project

The **WaferFault Detection** project aims to detect faults in wafer manufacturing using machine learning techniques. The project includes components for data ingestion, data transformation, model training, and prediction pipelines. It utilizes various tools and technologies such as Flask, SMOTE, RobustScaler, Sklearn, Docker, AWS ECR, Git, and GitHub Actions.

## Project Structure

The project is organized with the following structure:

- `src/`: The core of the project, containing components, pipelines, exception handling, and logger files.
  - `components/`: Contains modules for data ingestion, data transformation, and model training.
  - `pipelines/`: Holds training and prediction pipeline files.
- `app.py`: Main application script using Flask.
- `config.yaml`: Configuration file for the project.
- `upload_data_TO_DB.py`: Script to upload data to MongoDB.
- `requirements.txt`: List of Python dependencies.
- `artifacts/`: Contains essential project artifacts.
  - `model.pkl`: Serialized trained machine learning model.
  - `preprocessor.pkl`: Serialized preprocessor including pipeline and transformations.
  - `train.csv`: Training data.
  - `test.csv`: Test data.

## Project Workflow

1. Data Ingestion: Raw data is imported from MongoDB and split into training and test sets.
2. Data Transformation: Using the training pipeline, data is processed and transformed. A preprocessor (`preprocessor.pkl`) is generated, including a pipeline with RobustScaler and SimpleImputer.
3. Model Training: Using the transformed data, the model training pipeline trains multiple classification ML models. The best-performing model is selected and saved as `model.pkl`.
4. Prediction Pipeline: New data can be passed through the prediction pipeline for fault prediction using the trained model.

## Getting Started

1. Clone the repository from GitHub.
2. Set up the necessary environment (virtual environment is recommended).
3. Install project dependencies using `pip install -r requirements.txt`.
4. Ensure MongoDB is running and accessible.
5. Run `upload_data_TO_DB.py` to upload raw data to MongoDB.
6. Start the Flask application with `python app.py`.
7. Access the application through a web browser or API calls.

## Deployment

The project can be deployed using Docker and AWS ECR:

1. Build the Docker image: `docker build -t waferfault-detection .`
2. Tag the image for AWS ECR: `docker tag waferfault-detection:latest <your-aws-account-id>.dkr.ecr.<your-region>.amazonaws.com/waferfault-detection:latest`
3. Push the image to AWS ECR: `docker push <your-aws-account-id>.dkr.ecr.<your-region>.amazonaws.com/waferfault-detection:latest`
4. Deploy the image to AWS ECS or any desired environment.

## Contributing

Contributions to the project are welcome! If you'd like to contribute, please follow the guidelines outlined in the CONTRIBUTING.md file.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
