"""On-device intent table. No network."""

VOCAB = {
    "interval": "interval",
    "difference": "interval",
    "delta": "interval",
    "point": "point",
    "celsius": "point",
    "kelvin": "kelvin",
}


def classify(text: str) -> str:
    hits = [VOCAB[token] for token in text.lower().split() if token in VOCAB]
    return hits[-1] if hits else "point"
