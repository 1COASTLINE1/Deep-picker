# Deep-picker

A deep learning and Gaussian mixture modeling-based framework for analyzing complex NMR spectra of mixed substances.

## 📌 Project Overview

This project addresses the challenge of analyzing NMR spectra from complex mixtures using a combination of **Gaussian Mixture Modeling (GMM)** and **Deep Learning Regression**. It enables precise concentration identification of individual components, especially effective for detecting **low-intensity (small-area) signals**.

---

## 🧠 Models and Structure

### `Class1_model/`
- Compares model performance under varying intensity ratios ranging from **100:1 to 1000:1**.
- Includes visualizations of:
  - **Absolute Error**: `pred - true`
  - **Relative Error**: `(pred - true) / true`
  - Summary statistics: **mean**, **median**, **std**, **max**, **min**

### `Final_model/`
- Uses results from the **600:1 intensity ratio**
- Trained model saved as: `my_model.h5`

### `demonstration.py`
- Demonstrates model predictions using `my_model.h5`
- Visual comparison between:
  - Original spectrum
  - Predicted spectrum
- Outputs predicted **area values**.

---

## 📊 Data Generation

### `Generation/`
- Generates synthetic data by fitting multiple Gaussian peaks
- Outputs formatted Excel files
- Core synthetic generation located in `final_version/Generate_comparision.py`

---

## ⚙️ Environment Setup (Docker + VSCode Remote)

### Build Docker Image
```bash
sudo docker build -t my-jupyter-notebook-gpu .
