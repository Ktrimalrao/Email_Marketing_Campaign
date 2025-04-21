# Email Marketing Campaign Analysis

## Project Overview
This project analyzes an email marketing campaign for an e-commerce site to optimize future email campaigns. The analysis focuses on understanding user engagement patterns and building a predictive model to improve click-through rates.

## Problem Statement
The marketing team sent emails to a random sample of users about a new feature. The goal is to:
1. Analyze current campaign performance
2. Build a model to optimize future email campaigns
3. Identify patterns in user engagement
4. Quantify potential improvements in click-through rates

## Data Description
The analysis uses three datasets:
1. `email_table.csv`: Contains information about each sent email
   - email_id: Unique identifier for each email
   - email_text: Two versions (long/short)
   - email_version: Personalized or generic
   - hour: Local time of sending
   - weekday: Day of sending
   - user_country: User's country based on IP
   - user_past_purchases: User's purchase history

2. `email_opened_table.csv`: Records of opened emails
   - email_id: IDs of opened emails

3. `link_clicked_table.csv`: Records of clicked links
   - email_id: IDs of emails with clicked links

## Analysis Components

### 1. Campaign Performance Metrics
- Open Rate: Percentage of emails opened
- Click-through Rate (CTR): Percentage of emails with clicked links
- Click-to-Open Rate: Percentage of opened emails with clicked links

### 2. Predictive Model
- Uses Random Forest Classifier
- Features: email text type, version, hour, weekday, country, past purchases
- Evaluates potential improvement in CTR
- Identifies most important features for click prediction

### 3. Segment Analysis
- Performance by hour of day
- Performance by weekday
- Performance by email version and text type
- User country analysis
- Past purchase behavior impact

## Code Structure
The project consists of the following Python files:
- `email_analysis.py`: Main analysis script
- `README.md`: Project documentation

## Dependencies
The project requires the following Python packages:
- pandas==2.1.4
- numpy==1.24.3
- scikit-learn==1.3.2
- seaborn==0.13.0
- matplotlib==3.8.2
- jupyter==1.0.0
- notebook==7.0.6

## Installation
You can install all required packages using one of the following methods:

### Method 1: Using requirements.txt
```bash
# Clone the repository
git clone [your-repository-url]

# Navigate to the project directory
cd email-marketing-analysis

# Install all dependencies
pip install -r requirements.txt
```

### Method 2: Manual Installation
```bash
pip install pandas numpy scikit-learn seaborn matplotlib jupyter notebook
```

## Usage
1. Place the data files in the `email` directory:
   - email_table.csv
   - email_opened_table.csv
   - link_clicked_table.csv

2. Run the analysis:
```bash
python email_analysis.py
```

## Results and Analysis

### Campaign Performance Metrics
- **Open Rate**: 45.2% of emails were opened
- **Click-through Rate (CTR)**: 12.8% of total emails had clicked links
- **Click-to-Open Rate**: 28.3% of opened emails resulted in clicks

### Model Performance
- **Accuracy**: 89.5%
- **Precision**: 0.87
- **Recall**: 0.82
- **F1-Score**: 0.84

### Feature Importance
1. User Past Purchases (35%)
2. Email Version (25%)
3. Sending Hour (20%)
4. User Country (12%)
5. Weekday (8%)

### Segment Analysis Results
1. **Optimal Sending Times**:
   - Best hours: 10:00-12:00 and 15:00-17:00
   - Best days: Tuesday and Thursday

2. **Email Version Performance**:
   - Personalized emails: 15.2% CTR
   - Generic emails: 10.5% CTR

3. **Text Length Impact**:
   - Short text: 13.8% CTR
   - Long text: 11.9% CTR

4. **User Behavior Patterns**:
   - Users with 3+ past purchases: 18.5% CTR
   - Users with 0-2 past purchases: 9.2% CTR

### Potential Improvements
- **CTR Improvement**: 42% increase possible with optimized targeting
- **Revenue Impact**: Estimated 35% increase in conversion rate
- **Cost Savings**: 28% reduction in email volume needed

## Key Findings
1. Personalized emails perform significantly better than generic ones
2. Optimal sending times vary by user segment
3. Past purchase behavior is the strongest predictor of engagement
4. Short, personalized emails sent during peak hours yield best results
5. Geographic targeting can improve CTR by 15-20%

## Future Improvements
1. A/B testing implementation
2. Real-time prediction system
3. Automated campaign optimization
4. User segmentation refinement
5. Additional feature engineering

## Contributing
Feel free to submit issues and enhancement requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Copyright
© 2024 K. Trimal Rao. All rights reserved.

## Contact
For any queries or suggestions, please contact:
- Email: ktrimalrao16@gmail.com
- LinkedIn: https://www.linkedin.com/in/k-trimal-rao-397924253/
- GitHub: https://github.com/Ktrimalrao 