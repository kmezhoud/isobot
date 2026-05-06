import re

# Parser ISO intelligent
def extract_iso_structure(text: str):
    """
    Parse un document ISO en sections hiérarchiques.
    Retourne une liste de blocs structurés.
    """

    # Regex pour sections ISO (ex: 8.4, 7.1.2, etc.)
    section_pattern = r'(\d+(\.\d+){1,3})\s+([A-Za-zÀ-ÿ ,\-]+)'

    matches = list(re.finditer(section_pattern, text))

    structured_blocks = []

    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)

        section_id = match.group(1)
        title = match.group(3).strip()
        content = text[start:end].strip()

        structured_blocks.append({
            "section": section_id,
            "title": title,
            "content": content
        })

    return structured_blocks


# Chunking intelligent par section ISO

def iso_chunker(structured_blocks, max_words=250):

    chunks = []

    for block in structured_blocks:

        words = block["content"].split()

        for i in range(0, len(words), max_words):
            chunk_text = " ".join(words[i:i + max_words])

            # 🔥 sécurité Ollama
            if len(chunk_text) > 1500:
                chunk_text = chunk_text[:1500]

            chunks.append({
                "text": chunk_text,
                "metadata": {
                    "section": block["section"],
                    "title": block["title"]
                }
            })

    return chunks

