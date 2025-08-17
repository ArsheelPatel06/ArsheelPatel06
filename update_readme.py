import json

# Load roadmap
with open("roadmap.json", "r") as f:
    data = json.load(f)

# Build checklist markdown
checklist = "\n".join(
    [f"- [{'x' if g['done'] else ' '}] {g['task']}" for g in data["goals"]]
)

# Read README
with open("README.md", "r") as f:
    readme = f.read()

# Replace section between markers
start = "<!-- ROADMAP-START -->"
end = "<!-- ROADMAP-END -->"
before = readme.split(start)[0]
after = readme.split(end)[1]

new_readme = before + start + "\n" + checklist + "\n" + end + after

# Write back
with open("README.md", "w") as f:
    f.write(new_readme)
