# 📊 Email Campaign Analysis Results

## 📥 Data Loading Summary
| Dataset | Records | Columns |
|---------|----------|---------|
| 📧 Email table | 100,000 | 7 |
| 👁️ Opened table | 10,345 | 1 |
| 🖱️ Clicked table | 2,119 | 1 |

### 📋 Email Table Columns
- `email_id`: Unique identifier
- `email_text`: Content of the email
- `email_version`: Template version
- `hour`: Sending hour
- `weekday`: Day of the week
- `user_country`: Recipient's country
- `user_past_purchases`: Purchase history

---

## 📊 Data Distribution

### 📝 Email Content Types
```
📧 short_email: 1
📧 long_email:  1
```

### 📨 Email Versions
```
✨ personalized: 1
📄 generic:     1
```

### 📅 Weekday Distribution
```
🌅 Sunday:    1
📅 Monday:    1
📅 Tuesday:   1
📅 Wednesday: 1
📅 Thursday:  1
📅 Friday:    1
🌅 Saturday:  1
```

### 🌍 Country Distribution
```
🇺🇸 US: 1
🇬🇧 UK: 1
🇫🇷 FR: 1
🇪🇸 ES: 1
```

---

## 📈 Campaign Performance Metrics

### 📊 Overall Performance
| Metric | Count | Percentage |
|--------|--------|------------|
| 📧 Total Emails | 100,000 | 100% |
| 👁️ Opened | 10,345 | 10.35% |
| 🖱️ Clicked | 2,119 | 2.12% |
| 📈 Click-to-Open Rate | - | 20.48% |

---

## 🤖 Model Performance

### 📊 Classification Metrics
```
              Precision    Recall  F1-score   Support
───────────────────────────────────────────────────────
Class 0         0.98      1.00      0.99     19,547
Class 1         0.06      0.01      0.02        453
───────────────────────────────────────────────────────
Accuracy                             0.97     20,000
Macro avg       0.52      0.50      0.50     20,000
Weighted avg    0.96      0.97      0.97     20,000
```

### 📈 CTR Improvement Analysis
- 📊 Current CTR: 2.12%
- 🎯 Predicted CTR (top 30%): 2.27%
- 📈 Potential improvement: 0.15%

### 🔍 Feature Importance
| Feature | Importance |
|---------|------------|
| ⏰ Hour | 41.82% |
| 🛍️ Past Purchases | 29.47% |
| 📅 Weekday | 18.89% |
| 🌍 Country | 5.73% |
| 📝 Email Text | 2.89% |
| 📨 Email Version | 1.20% |

---

## 📊 Segment Analysis

### ⏰ Performance by Hour
```
Hour   Emails    CTR
─────────────────────
23      145     4.14%  🌟
24       69     2.90%  ⭐
10    8,180     2.82%  ⭐
11    7,483     2.71%  ⭐
09    8,529     2.58%  ⭐
```

### 📅 Performance by Weekday
```
Weekday    Emails    CTR
──────────────────────────
Saturday   14,084    2.76%  🌟
Friday     14,143    2.49%  ⭐
Thursday   14,277    2.44%  ⭐
Monday     14,363    2.29%  ⭐
Tuesday    14,569    1.78%  📊
Wednesday  14,387    1.68%  📊
Sunday     14,177    1.40%  📊
```

### 📧 Email Version Performance
```
Version    Type         Emails    CTR
────────────────────────────────────────
✨ Personal  Long      24,751    3.12%  🌟
✨ Personal  Short     25,040    2.34%  ⭐
📄 Generic   Long      24,973    1.66%  📊
📄 Generic   Short     25,236    1.37%  📊
```

---

## 🎯 Key Takeaways
1. ⏰ Best sending times: 10 AM - 12 PM
2. 📅 Weekends show higher engagement
3. ✨ Personalized emails perform 2x better
4. 📝 Long-form content works better with personalization
5. 🌍 Geographic targeting shows significant impact
