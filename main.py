from urllib.parse import unquote

def decode_sse(raw_text):
    lines = raw_text.splitlines()
    decoded = ""
    for line in lines:
        if line.startswith("data:"):
            content = line[len("data:"):].strip()
            decoded += unquote(content)
    return decoded