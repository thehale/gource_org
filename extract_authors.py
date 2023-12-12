with open("gource.log") as f:
    log = f.read()

authors = set()
for line in log.splitlines():
    timestamp, author, edit, path = line.split("|")
    authors.add(author)

with open("authors.txt", "w") as f:
    f.write("\n".join(sorted(authors)))