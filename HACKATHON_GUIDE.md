# PIF/PUF xAI Hackathon Starter Guide
Non-tech narrative filter → Grok-powered clarity for X.  
Open-source. Patent-pending. Ready to ship.

## 3-Hour Build Path
1. `git clone https://github.com/PAGSAdmin/PIF-PUF`
2. `pip install requests streamlit`
3. Add X/Grok keys to `config.py` (template below)
4. `streamlit run dashboard.py` → Live triage
5. Test: Hurricane Melissa demo (`pifpuf_demo.html`)

## config.py Template
```python
X_API_KEY = "your_x_key"
GROK_API_KEY = "your_grok_key"  # Hackathon early access
RSS_SOURCES = ["https://fullfact.org/rss", "https://apnews.com/rss"]
