import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Read the data
def load_data():
    email_df = pd.read_csv("email/email_table.csv")
    opened_df = pd.read_csv("email/email_opened_table.csv")
    clicked_df = pd.read_csv("email/link_clicked_table.csv")
    
    print("Data Loading Summary:")
    print(f"Email table shape: {email_df.shape}")
    print(f"Opened table shape: {opened_df.shape}")
    print(f"Clicked table shape: {clicked_df.shape}")
    print("\nEmail table columns:", email_df.columns.tolist())
    
    return email_df, opened_df, clicked_df

def prepare_data(email_df, opened_df, clicked_df):
    # Add binary columns for opened and clicked
    email_df['opened'] = email_df['email_id'].isin(opened_df['email_id']).astype(int)
    email_df['clicked'] = email_df['email_id'].isin(clicked_df['email_id']).astype(int)
    
    # Convert categorical variables
    le = LabelEncoder()
    categorical_columns = ['email_text', 'email_version', 'weekday', 'user_country']
    
    for col in categorical_columns:
        email_df[col] = le.fit_transform(email_df[col])
        
        # Print unique values for each categorical column
        print(f"\nUnique values in {col}:")
        print(pd.Series(le.inverse_transform(email_df[col].unique())).value_counts())
    
    return email_df

def calculate_metrics(email_df):
    total_emails = len(email_df)
    opened_count = email_df['opened'].sum()
    clicked_count = email_df['clicked'].sum()
    
    opened_rate = (opened_count / total_emails) * 100
    click_rate = (clicked_count / total_emails) * 100
    click_to_open_rate = (clicked_count / opened_count) * 100 if opened_count > 0 else 0
    
    print("\nEmail Campaign Metrics:")
    print(f"Total emails sent: {total_emails:,}")
    print(f"Emails opened: {opened_count:,} ({opened_rate:.2f}%)")
    print(f"Links clicked: {clicked_count:,} ({click_rate:.2f}%)")
    print(f"Click-to-Open Rate: {click_to_open_rate:.2f}%")
    
    return opened_rate, click_rate

def build_model(email_df):
    # Prepare features
    features = ['email_text', 'email_version', 'hour', 'weekday', 
               'user_country', 'user_past_purchases']
    X = email_df[features]
    y = email_df['clicked']
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    
    print("\nModel Performance:")
    print(classification_report(y_test, y_pred))
    
    # Calculate potential improvement
    current_ctr = y.mean() * 100
    threshold = np.percentile(y_pred_proba, 70)  # Top 30% of predictions
    predicted_top_users = y_test[y_pred_proba >= threshold]
    potential_ctr = predicted_top_users.mean() * 100
    
    print(f"\nPotential CTR Improvement:")
    print(f"Current CTR: {current_ctr:.2f}%")
    print(f"Predicted CTR for top 30% users: {potential_ctr:.2f}%")
    print(f"Potential improvement: {potential_ctr - current_ctr:.2f} percentage points")
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'feature': features,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    return model, feature_importance, X_test, y_test

def analyze_segments(email_df):
    print("\nSegment Analysis:")
    
    # Analyze by hour
    hour_analysis = email_df.groupby('hour').agg({
        'clicked': ['count', 'mean']
    }).round(4)
    hour_analysis.columns = ['total_emails', 'click_rate']
    hour_analysis['click_rate'] = hour_analysis['click_rate'] * 100
    print("\nPerformance by Hour:")
    print(hour_analysis.sort_values('click_rate', ascending=False))
    
    # Analyze by weekday
    weekday_analysis = email_df.groupby('weekday').agg({
        'clicked': ['count', 'mean']
    }).round(4)
    weekday_analysis.columns = ['total_emails', 'click_rate']
    weekday_analysis['click_rate'] = weekday_analysis['click_rate'] * 100
    print("\nPerformance by Weekday:")
    print(weekday_analysis.sort_values('click_rate', ascending=False))
    
    # Analyze by email version and text
    version_analysis = email_df.groupby(['email_version', 'email_text']).agg({
        'clicked': ['count', 'mean']
    }).round(4)
    version_analysis.columns = ['total_emails', 'click_rate']
    version_analysis['click_rate'] = version_analysis['click_rate'] * 100
    print("\nPerformance by Email Version and Text:")
    print(version_analysis.sort_values('click_rate', ascending=False))

def main():
    # Load data
    print("Loading data...")
    email_df, opened_df, clicked_df = load_data()
    
    # Prepare data
    print("\nPreparing data...")
    email_df = prepare_data(email_df, opened_df, clicked_df)
    
    # Calculate metrics
    print("\nCalculating metrics...")
    opened_rate, click_rate = calculate_metrics(email_df)
    
    # Build and evaluate model
    print("\nBuilding model...")
    model, feature_importance, X_test, y_test = build_model(email_df)
    
    # Print feature importance
    print("\nFeature Importance:")
    print(feature_importance)
    
    # Analyze segments
    analyze_segments(email_df)

if __name__ == "__main__":
    main()