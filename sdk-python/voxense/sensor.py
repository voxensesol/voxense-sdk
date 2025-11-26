from typing import Dict, Any

def capture_dummy() -> Dict[str, Any]:
    """
    Placeholder sensor capture.
    In real usage this will read GPS / motion / ambient from device.
    """
    return {
        "gps": {"lat": -6.2, "lng": 106.8},
        "motion": {"ax": 0.01, "ay": 0.02, "az": 0.98},
        "ambient": {"temp": 29.4, "light": 0.8},
    }
