import ollama
import json
import re


def extract_json(text):

    match = re.search(r'\{.*\}', text, re.DOTALL)

    if match:
        return match.group(0)

    return None


def categorize_files(files):

    file_text = "\n".join(files)

    prompt = f"""
You are an AI file organizer.

Group files into meaningful folders.

Rules:

1. If the filenames clearly represent an academic or technical SUBJECT
   (like AI, DBMS, IoT, etc.), group them by that subject.

2. Otherwise group files by their purpose:
   Documents, Media, Personal, Projects, Archives, Code, etc.

3. Do not create one folder per file.

4. Folder names must be short and meaningful.

Return ONLY JSON.

Format:
{{
 "Folder Name": ["file1","file2"]
}}

Files:
{file_text}
"""

    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[{"role": "user", "content": prompt}],
        options={
            "temperature": 0,
            "num_predict": 200
        }
    )

    content = response["message"]["content"]

    json_text = extract_json(content)

    if not json_text:
        return {"error": "Model did not return JSON", "raw": content}

    try:
        return json.loads(json_text)
    except Exception as e:
        return {
            # "error": "Invalid JSON from model",
            "raw": content
        }
