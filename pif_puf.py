"""
PIF/PUF Framework — ClarityGuard
Created by Pauline Gonen-Smith (@clarityguard)
Open source under MIT License

Updated May 4, 2026 — Broader Emerging PIF logic included
"""

from typing import Dict, Any

def analyze_text(text: str) -> Dict[str, Any]:
    """
    Core PIF/PUF analysis function.
    Now includes broader Emerging PIF detection while avoiding speculation.
    """
    if not text or not text.strip():
        return {"error": "No text provided"}

    t = text.lower()

    # ==================== 1. PIF Scoring ====================
    pif_cat = 0
    pif_type = "neutral"
    pif_desc = ""
    is_emerging = False

    # High impact detection
    if any(word in t for word in ["hormuz", "iran standoff", "oil price", "energy crisis", "war", "conflict", "disaster", "casualty", "emergency"]):
        pif_cat = 4
        pif_type = "negative"
        pif_desc = "Major population impact on energy, safety, or stability"

    elif any(word in t for word in ["lithium", "discovery", "breakthrough", "major find", "strategic resource"]):
        pif_cat = 3
        pif_type = "positive"
        pif_desc = "Emerging positive strategic opportunity"
        is_emerging = True

    # Broader Emerging PIF detection (Cat 2 level)
    elif any(word in t for word in ["battery", "solid state", "ai drug", "ai discovery", "nuclear smr", "next gen", "long term"]):
        pif_cat = 2
        pif_type = "positive"
        pif_desc = "Medium-term emerging opportunity"
        is_emerging = True

    # ==================== 2. Bucket Classification ====================
    if pif_cat >= 3:
        bucket = "HIGH_PIF"
    elif pif_cat == 2 or is_emerging:
        bucket = "EMERGING_PIF"
    elif any(word in t for word in ["trump", "iran", "politics", "policy", "election"]):
        bucket = "POLITICS"
    elif any(word in t for word in ["study", "research", "explain", "insight", "history"]):
        bucket = "UNDERSTANDING"
    elif any(word in t for word in ["fun", "joke", "garden", "event", "how to"]):
        bucket = "FUN"
    else:
        bucket = "MISC"

    return {
        "pif_cat": pif_cat,
        "pif_type": pif_type,
        "pif_desc": pif_desc,
        "bucket": bucket,
        "is_emerging": is_emerging,
        "raw_text": text[:300] + "..." if len(text) > 300 else text
    }

# Simple demo / test
if __name__ == "__main__":
    samples = [
        "Iran proposes reopening Strait of Hormuz amid rising oil prices.",
        "Appalachia lithium discovery could transform U.S. energy security.",
        "New solid-state battery breakthrough announced."
    ]
    for sample in samples:
        result = analyze_text(sample)
        print(result)