import pandas as pd
import re

# Extract the raw text of the PDF from the file content
from PyPDF2 import PdfReader

def extract_economics_marks():
    """
    Extract Economics marks from PDF and calculate total for students with >=79 marks in groups 1-30
    """
    # Load the PDF - use local file path
    pdf_path = "q-extract-tables-from-pdf.pdf"
    reader = PdfReader(pdf_path)

    # Extract text from all pages
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() + "\n"

    print("PDF Text Extraction Complete")
    print(f"Total characters extracted: {len(full_text):,}")

    # Extract tables per group
    group_pattern = r"Student marks - Group (\d+)\s+Maths Physics English Economics Biology\n((?:\d+ \d+ \d+ \d+ \d+\n?)+)"
    matches = re.findall(group_pattern, full_text)

    print(f"Found {len(matches)} groups in the PDF")

    # Collect relevant Economics marks
    econ_marks = []
    groups_processed = 0
    
    for group_number, table in matches:
        group_number = int(group_number)
        if 1 <= group_number <= 30:
            groups_processed += 1
            rows = table.strip().split("\n")
            for row in rows:
                columns = list(map(int, row.split()))
                economics_score = columns[3]  # Economics is the 4th column (index 3)
                if economics_score >= 79:
                    econ_marks.append(economics_score)

    # Calculate total
    total_economics_marks = sum(econ_marks)
    
    print(f"\n=== RESULTS ===")
    print(f"Groups processed (1-30): {groups_processed}")
    print(f"Students with Economics >= 79: {len(econ_marks)}")
    print(f"Total Economics marks (>=79): {total_economics_marks:,}")
    print(f"Average Economics score (>=79): {total_economics_marks/len(econ_marks):.1f}")
    
    return total_economics_marks, econ_marks

if __name__ == "__main__":
    total_marks, scores = extract_economics_marks()
    
    # Save detailed results to file
    with open("economics_analysis_results.txt", "w") as f:
        f.write("Economics Marks Analysis Results\n")
        f.write("=" * 40 + "\n\n")
        f.write(f"Total Economics marks (>=79) in groups 1-30: {total_marks:,}\n")
        f.write(f"Number of students with Economics >=79: {len(scores)}\n")
        f.write(f"Individual scores >=79: {sorted(scores, reverse=True)}\n")
        f.write(f"Average score: {total_marks/len(scores):.1f}\n")
    
    print(f"\nDetailed results saved to 'economics_analysis_results.txt'")
    print(f"\nANSWER: The total Economics marks of students who scored 79 or more in Economics in groups 1-30 is {total_marks:,}")

