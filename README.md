# 📝 Spelling Correction Using Closest Match

A simple Python-based spelling correction project developed for **BhashaTHON**. It uses basic string similarity to suggest the most likely correct sentence for a given misspelled one.


## 📂 Project Structure

Spelling_Correction/ 
├── main.py # Main logic for correction 
├── Problems.txt # File with misspelled sentences 
├── artificial.train.tgt # File with correct reference sentences 
├── english_eval.corrected.txt # Output: corrected results 
├── requirements.txt # Dependencies └── README.md # Project documentation



## 🔧 How It Works
- Takes misspelled sentences from `Problems.txt`.
- Compares each with the reference list from `artificial.train.tgt`.
- Finds the closest match using string similarity (Levenshtein-like approach via `difflib`).
- Saves the corrected sentences to `english_eval.corrected.txt`.


## 🚀 Getting Started

#### 📦 Prerequisites
- Python 3.x
- pip

#### 🔧 Installation
git clone https://github.com/yourusername/Spelling_Correction.git
cd Spelling_Correction
pip install -r requirements.txt

### ▶️ Run the Project
python main.py
The output will be saved to english_eval.corrected.txt.

## 🖥️ Environment

- **OS:** Windows / Linux / macOS  
- **Python:** 3.x  
- **Libraries:** [`rapidfuzz`](https://pypi.org/project/rapidfuzz/) or built-in `difflib` (depending on usage)

## 🎥 Demo

You can find a demo walkthrough of the project in the included video file: `Video.mp4`.


## 👨‍💻 Team: Code Crafters

- **Ladani Vidhi**  
- **Dhyey Shah**  
- **Palak Kanjiya**  
- **Parth Chandegara**  


## ✅ Conclusion

This project showcases a straightforward yet impactful method for correcting misspelled sentences using Python's string similarity tools. It is designed to be lightweight, easy to implement, and a great starting point for those exploring the world of natural language processing.


## 🙏 Thank You

Thank you for taking the time to explore our project. We appreciate your interest and support.  
– Team **Code Crafters**
