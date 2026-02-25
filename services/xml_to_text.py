import xml.etree.ElementTree as ET

files = [
    "storage/reference/ES2002a.A.wordalign.xml",
    "storage/reference/ES2002a.B.wordalign.xml",
    "storage/reference/ES2002a.C.wordalign.xml",
    "storage/reference/ES2002a.D.wordalign.xml"
]

words = []

for file in files:
    tree = ET.parse(file)
    root = tree.getroot()

    for w in root.iter("word"):
        if w.text:
            words.append(w.text)

text = " ".join(words)

with open("storage/reference/reference_full.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Reference transcript created successfully.")
print("Total words:", len(words))