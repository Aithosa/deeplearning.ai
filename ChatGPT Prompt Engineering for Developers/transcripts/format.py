import os
import re

transcripts_dir = r'd:\deeplearning.ai\ChatGPT Prompt Engineering for Developers\Transcripts'
files = [f for f in os.listdir(transcripts_dir) if f.endswith('.md')]

timestamp_pattern = re.compile(r'^(\d{1,2}:\d{2})(.*)')

for filename in files:
    filepath = os.path.join(transcripts_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        match = timestamp_pattern.match(line)
        if match:
            timestamp = match.group(1)
            text = match.group(2).strip()
            
            # If no text on same line, look ahead
            if not text:
                i += 1
                while i < len(lines) and not lines[i].strip():
                    i += 1
                if i < len(lines):
                    text = lines[i].strip()
            
            new_lines.append(f"[{timestamp}] {text}\n")
        elif line: # preserve non-timestamped non-empty lines if any (unlikely in these transcripts)
             # But wait, we might have already consumed it in the 'look ahead'
             # If it's not a timestamp and not consumed, we might want to keep it?
             # Based on observation, every sentence has a timestamp.
             # Let's just append it if it wasn't a timestamp line.
             new_lines.append(line + "\n")
        
        i += 1

    # Remove consecutive empty lines if any were introduced or existed
    # (Though new_lines above doesn't add many empty ones)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

print("Formatting complete.")

