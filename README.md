# Machine Learning Projects

This branch (`ML-project`) of [python-basic-practice](https://github.com/amintnt2000/python-basic-practice) contains the machine learning projects I build while learning ML with Python. Each project lives in its own folder.

## Projects

| Folder | Problem | Type | Dataset topic |
|--------|---------|------|---------------|
| [`canada_income`](./canada_income) | Predict per-capita income by year | Regression | Canada income data |
| [`car_price`](./car_price) | Predict used car prices | Regression | Car sale prices |
| [`hiring`](./hiring) | Predict candidate salary | Regression | Hiring data |
| [`test_score`](./test_score) | Predict test scores | Regression | Student scores |
| [`HR_comma`](./HR_comma) | Predict employee retention | Classification | HR analytics |
| [`titanic`](./titanic) | Predict passenger survival | Classification | Titanic passengers |
| [`iris`](./iris) | Classify iris flower species | Classification | Iris dataset |
| [`digits`](./digits) | Recognize handwritten digits | Classification | Digits dataset |

## Topics Covered

- Data cleaning and preprocessing (missing values, categorical encoding)
- Linear and multiple linear regression
- Classification (logistic regression and other classifiers)
- Model evaluation and cross-validation (K-Fold)
- Data visualization

## Tech Stack

- **Language:** Python 3.x
- **Libraries:** NumPy, pandas, Matplotlib, scikit-learn
- **Tools:** Jupyter Notebook, PyCharm, Git

## Repository Structure

```
.
├── HR_comma/
├── canada_income/
├── car_price/
├── digits/
├── hiring/
├── iris/
├── test_score/
├── titanic/
└── README.md
```

## Getting Started

```bash
# Clone only this branch
git clone -b ML-project https://github.com/amintnt2000/python-basic-practice.git
cd python-basic-practice

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux / macOS

# Install the main libraries
pip install numpy pandas matplotlib scikit-learn jupyter
```

Then open any project folder and run its script or notebook.

## Goal

To document my learning path in ML: starting with the fundamentals (regression and classification on classic datasets) and moving toward more advanced models and real-world projects.

## Author

**Mohammad Amin Nochiyan**
Computer Engineering student, Shahrekord, Iran

- GitHub: [@amintnt2000](https://github.com/amintnt2000)
- LinkedIn: [MohammadAminNochiyan](https://www.linkedin.com/in/MohammadAminNochiyan)

I'm currently looking for an internship, so feedback and opportunities are welcome.
