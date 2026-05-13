# clean_headings.py

with open('app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

cleaned_lines = []
for line in lines:
    if line.strip().startswith("###") or line.strip().startswith("##"):
        # Convert markdown heading to comment
        cleaned_lines.append("# " + line.lstrip('#').strip() + "\n")
    else:
        cleaned_lines.append(line)

with open('app.py', 'w', encoding='utf-8') as f:
    f.writelines(cleaned_lines)

print("✨ Headings cleaned from app.py!")
