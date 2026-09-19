from pathlib import Path

def load_documents(directory):
    documents = []
    directory = Path(directory)
    
    for file_path in directory.rglob('*'):
        if file_path.is_file() and file_path.suffix.lower() == '.txt':
            text = file_path.read_text(encoding='utf-8')
            documents.append({"text": text, "source": str(file_path)})
    return documents