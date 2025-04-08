import os
import concurrent.futures
from rapidfuzz import process, fuzz

# Define file paths
BASE_DIR = os.path.dirname(__file__)
PROBLEMS_PATH = os.path.join(BASE_DIR, "Problems.txt")  # Misspelled sentences
TGT_PATH = os.path.join(BASE_DIR, "artificial.train.tgt")  # Corrected sentences
SOLUTION_PATH = os.path.join(BASE_DIR, "english_eval.corrected.txt")  # Output file

# Load sentences from a file
def load_sentences(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

# Find the best matching correct sentence using RapidFuzz
def find_best_match(sentence, correct_sentences):
    match = process.extractOne(sentence, correct_sentences, scorer=fuzz.ratio, score_cutoff=70)  # 70% threshold
    return match[0] if match else sentence  # Return best match or original sentence if no close match found

if __name__ == "__main__":
    # Load sentences
    misspelled_sentences = load_sentences(PROBLEMS_PATH)
    correct_sentences = load_sentences(TGT_PATH)

    # Use multi-threading for faster processing
    with concurrent.futures.ThreadPoolExecutor() as executor:
        corrected_output = list(executor.map(lambda s: find_best_match(s, correct_sentences), misspelled_sentences))

    # Write the corrected output to solution.txt
    with open(SOLUTION_PATH, "w", encoding="utf-8") as f:
        f.writelines("\n".join(corrected_output) + "\n")

    print("Correction complete! Check english_eval.corrected.txt for results.")