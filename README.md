# 🏭 AI-Powered Smart Factory Control Room

### Industrial Digital Twin & Machine Failure Diagnosis System using Machine Learning

An AI-powered predictive maintenance system designed to monitor industrial machine parameters, predict possible machine failures, assess machine health, and provide maintenance recommendations through an interactive control-room dashboard.

---

## 📌 Project Overview

This project implements a **Machine Failure Prediction and Monitoring System** for industrial machines using Machine Learning.

The system takes important machine operating parameters as input and uses a trained machine learning model to predict whether the machine is likely to experience a failure.

The project provides an interactive **Streamlit-based Smart Factory Control Room** where users can enter machine parameters and observe the predicted machine condition.

### Features

- ✅ Machine Health Condition
- ✅ Failure Probability
- ✅ Machine Health Score
- ✅ Risk Assessment
- ✅ Maintenance Recommendation
- ✅ Graphical Analysis of Machine Parameters

The project is developed using the **AI4I 2020 Predictive Maintenance Dataset**.

---

## 🎯 Objectives

- Predict possible machine failures before they occur.
- Monitor important industrial machine parameters.
- Calculate an estimated machine health score.
- Determine the probability of machine failure.
- Identify different levels of machine risk.
- Provide suitable maintenance recommendations.
- Develop an interactive industrial monitoring dashboard.
- Demonstrate the application of Machine Learning in Predictive Maintenance.

---

## ⚙️ Machine Parameters

| Parameter | Unit | Description |
|------------|------|-------------|
| Air Temperature | K | Temperature of surrounding air |
| Process Temperature | K | Machine process temperature |
| Rotational Speed | RPM | Rotational speed of machine |
| Torque | Nm | Torque applied to machine |
| Tool Wear | min | Operating wear of machine tool |

These parameters are used as inputs to the trained Machine Learning model.

---

## 🤖 Machine Learning Prediction

The trained Machine Learning model analyzes machine parameters and predicts the machine condition.

### Prediction Output

- 🟢 Machine Healthy
- 🔴 Machine Failure Predicted

The dashboard also displays:

- Machine Health Score
- Failure Risk
- Risk Level
- Maintenance Recommendation

---

## 🏥 Machine Health Score

The system calculates a machine health score based on the predicted probability of the machine being healthy.

### Risk Assessment

| Health Score | Risk Level |
|-------------|------------|
| Above 80% | 🟢 LOW RISK |
| 51% - 80% | 🟡 MEDIUM RISK |
| 50% or Below | 🔴 HIGH RISK |

This provides a simple way for users to understand the current machine condition.

---

## 🚨 Maintenance Recommendation

The system provides maintenance recommendations based on abnormal machine operating conditions.

Examples:

- 🌡️ High Air Temperature → Inspect Cooling System
- 🔧 High Tool Wear → Replace or Inspect the Tool
- ⚙️ High Torque → Inspect Motor Load Condition
- ✅ Normal Conditions → No Immediate Maintenance Required

These recommendations help users identify maintenance requirements at an early stage.

---

## 📊 Interactive Dashboard

The project uses **Streamlit** to create an interactive Smart Factory Control Room.

### Control Room

- 🎯 Model Accuracy
- 🏭 Number of Machines
- ⚠️ Failure Types
- 🟢 System Status

### Machine Parameters

Users can enter:

- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear

### Prediction Section

After clicking the **Predict** button, the dashboard displays:

- Machine Condition
- Machine Health Score
- Failure Risk
- Risk Assessment
- Maintenance Recommendation

### Dataset Analysis

The dashboard also provides graphical analysis of machine operating parameters to better understand dataset trends and machine conditions.

---

## 🔄 System Workflow

```text
                Machine Parameters
                       │
                       ▼
                  Data Input
                       │
                       ▼
              Data Preprocessing
                       │
                       ▼
             Machine Learning Model
                       │
                       ▼
              Failure Prediction
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
      Machine Healthy      Failure Predicted
             │                   │
             └─────────┬─────────┘
                       ▼
              Health Score &
               Failure Risk
                       │
                       ▼
               Risk Assessment
                       │
                       ▼
          Maintenance Recommendation
```

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Libraries and Frameworks

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

### Machine Learning

- Supervised Machine Learning
- Classification
- Predictive Maintenance

### Development Tools

- Visual Studio Code
- Git
- GitHub

---

## 📁 Project Structure

```text
AI-Powered-Smart-Factory-Control-Room
│
├── Dataset
│   └── ai4i2020.csv
│
├── Images
│   ├── failure1 (1).png
│   ├── failure1 (2).png
│   ├── failure1 (3).png
│   ├── failure1 (4).png
│   ├── failure1 (5).png
│   ├── healthy prediction.png
│   ├── healthy prediction1.png
│   ├── healthy prediction2.png
│   └── healthy prediction3.png
│
├── models
│   └── model.pkl
│
├── analysis.py
├── app.py
├── check_data.py
├── missing_values.py
├── save_model.py
├── train_model.py
└── README.md
```

---

## 📌 Conclusion

The AI-Powered Smart Factory Control Room demonstrates how Machine Learning can be applied to predictive maintenance and industrial machine monitoring.

By analyzing machine parameters such as temperature, rotational speed, torque, and tool wear, the system predicts the possibility of machine failure and provides a simple health and risk assessment.

The interactive Streamlit dashboard makes the system easy to use and provides a foundation for developing a more advanced Industrial Digital Twin and Smart Factory Monitoring System.

---

## 👨‍💻 Developed By

**Kshipra Kshitij Joshi**

---

## 🚀 Project Title

**AI-Powered Smart Factory Control Room**

Industrial Digital Twin & Machine Failure Diagnosis System using Machine Learning
