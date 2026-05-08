import os
import re

directory = r"D:\OneDrive\Notes\deeplearning.ai\Claude Code A Highly Agentic Coding Assistant\subtitles"
files = [f for f in os.listdir(directory) if f.endswith('.ass')]

def has_chinese(text):
    return any('\u4e00' <= char <= '\u9fff' for char in text)

suspicious_lines = []

for filename in files:
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith('Dialogue:'):
                # Extract the text part. Usually after the 9th comma
                parts = line.split(',', 9)
                if len(parts) > 9:
                    text = parts[9].strip()
                    # Split by \N to get Chinese and English parts
                    # In this format it's {\fs80}Chinese\N{\fs50}English
                    sub_parts = text.split(r'\N')
                    chinese_part = sub_parts[0]
                    
                    # Clean up {\fsXX} tags
                    clean_chinese = re.sub(r'\{\\fs\d+\}', '', chinese_part)
                    
                    if clean_chinese and not has_chinese(clean_chinese):
                        # It might be just numbers or punctuation, check if it's alphanumeric english
                        if re.search(r'[a-zA-Z]', clean_chinese):
                            suspicious_lines.append({
                                'file': filename,
                                'line_number': i + 1,
                                'text': line.strip()
                            })

for item in suspicious_lines:
    print(f"File: {item['file']}, Line: {item['line_number']}")
    print(f"  {item['text']}")
