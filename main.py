"""One-line vending-machine pickup line for make.fun.

Pure Python stdlib, deterministic, no network. Writes a single pickup
line (at most 200 characters, no trailing newline) to /output/entry.txt.
"""

LINE = "Are you exact change? Because you're the only thing I never give back."


def main():
    assert 1 <= len(LINE) <= 200, "line must be 1-200 chars"
    assert LINE == LINE.strip(), "line must not have surrounding whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
