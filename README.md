# Wine Quality Dataset Analysis

## Overview

This project explores the Red Wine Quality dataset from the UCI Machine Learning Repository. The primary goal was to define and justify variable selections for three distinct business problems related to predicting and understanding wine quality based on physicochemical properties. An initial data exploration script (`Exploration.py`) is included.

## Author

- **Data Scientist:** Connor Hill

## Dataset

*   **Source:** UCI Machine Learning Repository
*   **Dataset Name:** Wine Quality (Using the Red Wine subset: `winequality-red.csv`)
*   **Details:**
    *   Contains 1599 observations (rows).
    *   Includes 12 attributes (columns): 11 physicochemical inputs and 1 quality output.
    *   Link: [https://archive.ics.uci.edu/ml/datasets/wine+quality](https://archive.ics.uci.edu/ml/datasets/wine+quality)

## Business Problems Explored

### Problem 1: Predicting Wine Quality Score
*   **Question:** How accurately can we predict the sensory quality score (0-10) of a red wine using its measured physicochemical properties?
*   **Dependent Variable (DV):** `quality`
    *   **Rationale:** The objective is to predict the wine's quality score directly. This column represents the sensory score assigned by experts, serving as the specific target outcome.
*   **Independent Variables (IVs):** `volatile acidity`, `citric acid`, `chlorides`, `sulphates`, `alcohol`, `pH`
    *   **Rationale:** This selection provides a comprehensive set of factors known to influence taste, aroma, and perception, aiming for a robust prediction. Key aspects covered include potential spoilage (`volatile acidity`), freshness (`citric acid`), taste elements (`chlorides`), preservation/stability (`sulphates`, `pH`), and body (`alcohol`).

### Problem 2: Identifying Key Quality Influencers
*   **Question:** Which specific physicochemical factors have the most significant positive or negative influence on the perceived quality rating of red wine, and can we quantify this impact?
*   **Dependent Variable (DV):** `quality`
    *   **Rationale:** To assess the influence of various factors *on* the quality score, the `quality` column is the outcome variable whose variation we seek to explain.
*   **Independent Variables (IVs):** `alcohol`, `volatile acidity`, `sulphates`, `total sulfur dioxide`
    *   **Rationale:** This analysis focuses on identifying the most impactful drivers. The selection includes variables often considered primary determinants of quality or indicators of significant flaws: `alcohol` (body/intensity), `volatile acidity` (faults), and `sulphates`/`total sulfur dioxide` (preservation/aroma impact). Analyzing this focused set facilitates clearer interpretation of individual factor significance.

### Problem 3: Classifying High vs. Standard Quality Wine
*   **Question:** Can we develop a reliable classification model to distinguish between red wines perceived as 'high quality' (e.g., quality score > 6) and 'standard quality' (e.g., quality score <= 6) based solely on their physicochemical tests?
*   **Dependent Variable (DV):** `quality_category` (Binary: 1 if `quality` > 6, 0 otherwise)
    *   **Rationale:** The goal is to classify wines into discrete groups. This requires transforming the original continuous `quality` score into a categorical (binary) target variable based on a defined quality threshold (e.g., >6 for 'high quality').
*   **Independent Variables (IVs):** `alcohol`, `volatile acidity`, `fixed acidity`, `density`, `sulphates`
    *   **Rationale:** For classification, features expected to show distinct differences between the quality tiers are chosen. These include `alcohol` (often higher in better wines), `volatile acidity` (lower in better wines), `fixed acidity` (structure), `density` (related to alcohol/sugar), and `sulphates` (stability/taste). These variables represent key characteristics likely to differ systematically between standard and high-quality wines.

## Files in this Repository

*   `Data/winequality-red.csv`: The red wine quality dataset used for analysis.
*   `Data/winequality-white.csv`: The white wine quality dataset (provided but not used in this specific analysis).
*   `Data/winequality.names`: Original description file for the dataset.
*   `Exploration.py`: Python script using pandas for basic data loading and exploration of the red wine dataset.
*   `Objectives.txt`: Text file outlining the business problems and initial variable selections (simplified version).
*   `Submission.txt`: The original assignment submission text.
*   `README.md`: This file.

## Requirements

*   Python 3.x
*   pandas library (`pip install pandas`)

## How to Run the Exploration Script

1.  Clone this repository to your local machine.
2.  Ensure you have Python and pandas installed.
3.  Navigate to the repository's root directory in your terminal.
4.  Run the script using the command:
    ```bash
    python Exploration.py
    ```
    This will print basic information about the dataset (head, info, describe, quality counts) to the console.
