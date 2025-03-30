# OCT Streamlit App

## Overview

This is an **Optical Coherence Tomography (OCT) Image Analysis Application** built with **Streamlit**. It allows users to upload multiple OCT images for processing and analysis. The application performs various image processing techniques, including grayscale conversion, histogram equalization, Gaussian blurring, edge detection, and adaptive thresholding.

## Features

- Upload multiple **OCT images** (JPEG, PNG, JPG formats)
- Display **image metadata** (size, format, channels, etc.)
- Apply **image processing techniques**:
  - **Grayscale Conversion**
  - **Histogram Equalization**
  - **Gaussian Blurring**
  - **Edge Detection (Canny Algorithm)**
  - **Adaptive Thresholding**
- User-controlled **edge detection thresholds**
- Save and **download processed images**

## Folder Structure

```
OCT_Streamlit_App/
│── app/
│   ├── streamlit_app.py       # Main Streamlit application
│   ├── utils.py               # Helper functions
│── requirements.txt           # Dependencies
│── Dockerfile                 # Docker instructions
│── deployment.yaml            # Kubernetes deployment
│── hpa.yaml                   # Horizontal Pod Autoscaler
│── service.yaml               # Kubernetes service definition
│── .gitignore                 # Ignore unnecessary files
│── README.md                  # Documentation
│── images/                    # Store sample OCT images (optional)
```

## Installation & Setup

### 1️⃣ **Clone the Repository**

```sh
git clone https://github.com/your-username/OCT_Streamlit_App.git
cd OCT_Streamlit_App
```

### 2️⃣ **Install Dependencies**

```sh
pip install -r requirements.txt
```

### 3️⃣ **Run the Application**

```sh
streamlit run app/streamlit_app.py
```

## Docker Setup

### 1️⃣ **Build Docker Image**

```sh
docker build -t oct-streamlit-app .
```

### 2️⃣ **Run Docker Container**

```sh
docker run -p 8501:8501 oct-streamlit-app
```

## Kubernetes Deployment

### 1️⃣ **Apply Deployment & Service**

```sh
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f hpa.yaml
```

### 2️⃣ **Check the Status**

```sh
kubectl get pods
kubectl get svc
```

## CI/CD with GitHub Actions

This application includes a **GitHub Actions CI/CD pipeline** to automate **Docker image building** and **deployment to Azure Kubernetes Service (AKS)**. The pipeline is triggered on every push to the `main` branch.

### 1️⃣ **Set Up GitHub Secrets**

Go to **Settings → Secrets and variables → Actions**, and add the following:

- `ACR_USERNAME`: Your Azure Container Registry username
- `ACR_PASSWORD`: Your Azure Container Registry password
- `AZURE_CREDENTIALS`: Azure service principal credentials

### 2️⃣ **GitHub Actions Workflow**

A sample `.github/workflows/deploy.yml` is included to automate deployment.

## Authors

- **Asad Moinuddin**
- **moinuddinasad@gmail.com**

## License

This project is licensed under the MIT License.
