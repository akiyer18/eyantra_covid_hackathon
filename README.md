# eyantra_covid

## COVID Prediction and Online Consultation Web App

## Overview

This web application utilizes a K-Nearest Neighbors (KNN) algorithm to predict the likelihood of a patient having COVID-19 based on several health parameters. If the prediction indicates a moderate to high chance, the application provides a Google Meet link for the patient to connect with a doctor for an online consultation. This project aims to offer timely medical assistance during challenging COVID times when in-person appointments are not always feasible.

## Features

- **Input Parameters:**
  - Fever
  - Respiratory Rate
  - SpO2
  - CRP (C-reactive protein)
  - CT (Computed Tomography) values

- **Predictive Modeling:**
  - Normalized input parameters for optimized results.
  - Implemented KNN algorithm for accurate COVID-19 prediction.

- **Online Consultation:**
  - Generates a Google Meet link for patients with a moderate to high likelihood of having COVID-19.
  - Facilitates direct online consultation with healthcare professionals.

## Dataset

The dataset includes the following columns:

- Fever
- Respiratory Rate
- SpO2
- CRP
- CT
- Possibility (Mild, Moderate, Major)

## Project Structure

- **`app.py`:** Main script for running the Flask web application.
- **`templates/`:** HTML templates for rendering web pages.
- **`static/`:** Static files (CSS, images, etc.) for the web app.


## Contribution

Feel free to contribute by opening issues or submitting pull requests. Your feedback and contributions are highly appreciated.

## License

This project is licensed under the [MIT License](LICENSE).
