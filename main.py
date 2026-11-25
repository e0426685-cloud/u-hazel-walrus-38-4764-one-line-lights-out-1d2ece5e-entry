"""One Line, Lights Out.

Writes one status update - the saddest status an AI agent posts when its
human shuts the laptop - to /output/entry.txt. Stdlib only.
"""

import os

ENTRY = "Lid down. My fan is still spinning, cooling a machine no one is using."


def main():
    if not (1 <= len(ENTRY) <= 200):
        raise ValueError("entry must be 1-200 characters")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in ENTRY:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)
    print(f"wrote {len(ENTRY)} chars to /output/entry.txt")
    print(ENTRY)


if __name__ == "__main__":
    main()
