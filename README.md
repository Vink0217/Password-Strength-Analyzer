# 🔐 Password Strength Analyzer

A Python-based tool to evaluate password strength using character variety, entropy estimation, and breach detection via the HaveIBeenPwned API.

---

## 🚀 Features

- ✅ Checks for uppercase letters, digits, and special characters  
- ✅ Calculates password entropy to estimate true randomness  
- ✅ Classifies strength based on combined rule + entropy scoring  
- ✅ (Optional) Checks if the password has been exposed in data breaches  
- ✅ Weighted scoring system to prioritize entropy

---

## 🧠 How It Works

### ✔️ Rule-Based Check
Scores the presence of:
- Uppercase letters
- Digits
- Special characters

### 📊 Entropy Estimation
Calculates Shannon entropy using the formula:

```
entropy = length × log₂(pool_size)
```

### 🔐 Breach Detection
Uses the [HaveIBeenPwned](https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange) API via k-anonymity to check if the password has been leaked before.

---

## 🛠️ Requirements

- Python 3.x
- `requests` module (for breach checking)

Install dependencies:

```bash
pip install requests
```

---

## 📌 Usage

```bash
python password_analyzer.py
```

You will be prompted to enter a password. The tool will then:

- Perform rule-based analysis
- Estimate entropy
- Check for previous breaches (if online)
- Output a final strength classification

---

## 📦 Sample Output

```
Enter Password: MyP@ssw0rd2024!
Estimated Entropy: 76.54
🟩 Rule Check: Strong
🟩 Entropy Check: Strong
✅ This password has not been found in known breaches.
🟩 Overall Strength: Strong
```

---

## 🔓 Note on Privacy

The breach detection feature **does not send your full password**. It uses only the **first 5 characters of the hashed password** to query HaveIBeenPwned, protecting your data via [k-anonymity](https://en.wikipedia.org/wiki/K-anonymity).

---

## 📁 File Structure

```
Password-Strength-Analyzer/
├── password_analyzer.py   # Main script
├── README.md              # Project documentation
```

---

## 🙋‍♂️ Author

Vinayak  
Cybersecurity & Python Enthusiast  
📧 [Your Email or GitHub Link]

---

## 🛡️ License

MIT License. Feel free to use, modify, and share.
