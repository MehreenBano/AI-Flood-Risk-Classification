# AI-Flood-Risk-Classification
AI Problem Design – Flood Risk Classification
1. Problem Statement

Floods can cause serious damage to communities, homes, roads, and other infrastructure. This project proposes a small AI-based classification system that uses environmental data to classify flood risk into three categories: Low, Medium, or High.

The goal is to explore how AI can help identify potentially high-risk conditions from available environmental information.

2. Target User

The proposed system is intended for:

People living in flood-prone areas
Local emergency-management teams
Communities that need simple information about changing flood-risk conditions

The system is designed as a prototype and is not intended to replace official weather or emergency warnings.

3. Data Source

The project will use a small publicly available dataset containing environmental and flood-related information, such as rainfall and other relevant weather or water-level features.

The dataset will be used only for educational and prototype development purposes.

4. Constraints

The project will have the following constraints:

The dataset will be relatively small.
Only a limited number of environmental features will be used.
The model should be simple enough for a beginner-friendly prototype.
The results may not represent real-time conditions.
The system will not be used as an official emergency warning system.

5. Success Criteria

The AI model will be considered successful if it can classify flood-risk levels reasonably well on previously unseen test data.

The model will be evaluated using:

Accuracy
Precision
Recall
F1-score

A target of approximately 80% test accuracy will be used as an initial goal, while also checking that the model does not perform well on only one risk category.

6. Evaluation Approach

The dataset will be divided into training and testing data.

A simple classification model, such as a Decision Tree or Random Forest, will be trained using the training data. The model's predictions will then be compared with the actual risk categories in the test data.

The evaluation results will be used to determine how well the model can classify Low, Medium, and High flood-risk conditions.

7. Expected Outcome

The expected outcome is a beginner-friendly AI prototype that demonstrates how environmental data can be used for flood-risk classification. This project can later be expanded with additional features and developed into a complete AI-based disaster-management application.
## Task 2 – Model or API Integration

For this task, I integrated the Open-Meteo Weather API into the flood risk classification project.

The API provides current environmental data including:
- Temperature
- Precipitation
- Rain

The Python program sends latitude and longitude to the API and receives the current weather data. Based on precipitation and rain values, the program classifies the current flood risk as Low, Medium, or High.

### Integration Flow

User Location → Weather API → Environmental Data → Flood Risk Classification

### Example

For latitude 35.92 and longitude 74.31, the API returned:

- Temperature: 20.5 °C
- Precipitation: 0.0 mm
- Rain: 0.0 mm
- Flood Risk: Low

This is an educational prototype and is not intended to replace official flood warnings or emergency-management systems.

## Task 3 – Intelligent Feature, Error Handling and Evaluation

### Intelligent Feature

The prototype will be improved with an intelligent risk explanation feature.
Instead of only displaying the flood risk level, the system will also provide a simple explanation based on the precipitation and rain values.

For example:
- Low Risk: Low precipitation and rainfall indicate lower current flood-risk conditions.
- Medium Risk: Moderate precipitation or rainfall suggests that weather conditions should be monitored.
- High Risk: Heavy precipitation or rainfall may indicate a higher possibility of flood risk.
