import re
import sys
import os
import getpass
import warnings

COMMON = {"password", "123456", "qwerty", "letmein", "admin", "welcome"}

def score_password(pw: str) -> tuple[int, list[str]]:
    suggestions: list[str] = []
    score = 0

    if len(pw) >= 12:
        score += 2
    elif len(pw) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 12 characters")

    if re.search(r"[a-z]", pw): score += 1
    else: suggestions.append("Add lowercase letters")

    if re.search(r"[A-Z]", pw): score += 1
    else: suggestions.append("Add uppercase letters")

    if re.search(r"\d", pw): score += 1
    else: suggestions.append("Add digits")

    if re.search(r"[^\w\s]", pw): score += 1
    else: suggestions.append("Add symbols (e.g., !@#$)")

    if pw.lower() in COMMON:
        suggestions.append("Avoid common passwords")
        score = max(score - 2, 0)

    return score, suggestions

def running_in_git_bash() -> bool:
    # Heuristic: Git Bash/mintty typically sets MSYSTEM and TERM like xterm
    return bool(os.environ.get("MSYSTEM")) and "xterm" in os.environ.get("TERM", "").lower()

def prompt_password(argv: list[str]) -> str:
    # CLI arg for quick testing
    if len(argv) >= 2 and not argv[1].startswith("-"):
        return argv[1]

    # Optional flag to force visible input everywhere
    if "--visible" in argv:
        return input("Enter password (visible): ")

    # Avoid hidden prompt on Git Bash where it can hang
    if running_in_git_bash():
        return input("Enter password (visible): ")

    # Try hidden input; fall back if getpass warns or errors
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        try:
            pw = getpass.getpass("Enter password (input hidden): ")
        except Exception:
            return input("Enter password (visible): ")
        for warn in w:
            # If the terminal can't disable echo, use visible prompt
            if getattr(warn, "category", None).__name__ == "GetPassWarning":
                return input("Enter password (visible): ")
        return pw

def main():
    pw = prompt_password(sys.argv)
    score, suggestions = score_password(pw)

    clamped = min(score, 5)
    verdicts = ["Very weak", "Weak", "OK", "Good", "Strong", "Very strong"]
    verdict = verdicts[clamped]

    print(f"Score: {clamped}/5 - {verdict}")
    if suggestions:
        print("Suggestions:")
        for s in suggestions:
            print(f"- {s}")

if __name__ == "__main__":
    main()
