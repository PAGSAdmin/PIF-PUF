"""
PIF/PUF Framework — ClarityGuard
Created by Pauline Gonen-Smith (@clarityguard)
Open source under MIT License
"""

from typing import Dict, Any

def analyze_text(text: str) -> Dict[str, Any]:
    """
    Core PIF/PUF analysis function.
    Returns structured output matching the current framework.
    """
    if not text or not text.strip():
        return {"error": "No text provided"}

    t = text.lower()

    # ==================== 1. PIF Scoring ====================
    pif_cat = 0
    pif_type = "neutral"
    pif_desc = ""

    # High impact detection
    if any(word in t for word in ["hormuz", "iran standoff", "oil price", "energy crisis", "war", "conflict", "disaster", "casualty"]):
        pif_cat = 4
        pif_type = "negative"
        pif_desc = "Major population impact on energy, safety, or stability"
    elif any(word in t for word in ["lithium", "discovery", "breakthrough", "major find"]):
        pif_cat = 3
        pif_type = "positive"
        pif_desc = "Emerging positive strategic opportunity"
    elif any(word in t for word in ["shooting", "attack", "protest", "election tension"]):
        pif_cat = 3
        pif_type = "negative"
        pif_desc = "Significant security or social impact"

    # ==================== 2. Bucket Classification ====================
    if pif_cat >= 3:
        bucket = "HIGH_PIF"
    elif pif_cat > 0:
        bucket = "EMERGING_PIF"
    elif any(word in t for word in ["trump", "iran", "middle east", "politics", "policy"]):
        bucket = "POLITICS"
    elif any(word in t for word in ["study", "discovery", "research", "explain", "insight"]):
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
        "raw_text": text[:300] + "..." if len(text) > 300 else text
    }


# Simple demo / test
if __name__ == "__main__":
    sample = "Iran proposes reopening Strait of Hormuz amid rising oil prices."
    result = analyze_text(sample)
    print(result)