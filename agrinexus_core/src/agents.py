from typing import List, Dict
from dataclasses import dataclass
import time
from .sensors import SoilSensorNetwork
from .search_tool import AgriSearch

@dataclass
class Recommendation:
    alert_level: str
    diagnosis: str
    action_plan: str
    sources: List[str]

class CropConsultant:
    """
    The main AI Agent that orchestrates the analysis.
    """
    def __init__(self, use_search: bool = True):
        self.search_tool = AgriSearch() if use_search else None
        
    def analyze_field(self, sensor_readings: List[Dict]) -> Dict:
        """
        Phase 1: Diagnosis - Analyze raw data to find anomalies.
        """
        print("\n[AI AGENT] Phase 1: Analyzing Sensor Stream...")
        anomalies = []
        
        # Aggregate logic
        avg_n = sum(r['nitrogen'] for r in sensor_readings) / len(sensor_readings)
        avg_m = sum(r['moisture'] for r in sensor_readings) / len(sensor_readings)
        
        print(f"  > Field Average N: {avg_n:.1f} mg/kg")
        print(f"  > Field Average Moisture: {avg_m:.1f} %")
        
        # Detection Logic (Simplified for Demo)
        if avg_n < 120:  # Threshold for Corn
            anomalies.append("Nitrogen Deficiency detected across multiple zones")
        if avg_m > 40: # High moisture
            anomalies.append("Excessive Soil Moisture detected")
            
        return {"avg_n": avg_n, "avg_m": avg_m, "anomalies": anomalies}

    def research_solutions(self, anomalies: List[str], crop: str) -> List[Dict]:
        """
        Phase 2: Research - Formulate queries and fetch data.
        """
        if not anomalies:
            return []
            
        print("\n[AI AGENT] Phase 2: Formulating Research Strategy...")
        findings = []
        
        for issue in anomalies:
            # Multi-hop reasoning simulation
            # 1. Broad search
            query = f"{crop} {issue} treatments"
            print(f"  > Generated Query: '{query}'")
            results = self.search_tool.search(query)
            
            # 2. Contextual Refinement (if moisture is high + nitrogen low)
            if "Nitrogen" in issue and "Moisture" in str(anomalies):
                refinement = f"{crop} nitrogen deficiency heavy rainfall leaching"
                print(f"  > Refinement Triggered: Contextualizing with Weather Data")
                print(f"  > Generated Query: '{refinement}'")
                results.extend(self.search_tool.search(refinement))
            
            findings.extend(results)
            
        return findings

    def generate_plan(self, diagnosis: Dict, research: List[Dict]) -> Recommendation:
        """
        Phase 3: Synthesis - Create the final action plan.
        """
        print("\n[AI AGENT] Phase 3: Synthesizing Recommendation...")
        time.sleep(1.0) # Simulate LLM generation time
        
        if not diagnosis["anomalies"]:
            return Recommendation(
                alert_level="GREEN",
                diagnosis="Optimal Conditions",
                action_plan="Continue monitoring. No intervention required.",
                sources=[]
            )
            
        # Mock LLM Synthesis
        alert = "RED" if len(diagnosis["anomalies"]) > 1 else "YELLOW"
        
        plan = (
            "**IMMEDIATE ACTION REQUIRED**\n\n"
            "1. **Nitrogen Application**: Field averages indicate critical N deficiency (Avg < 120mg/kg). "
            "However, due to high moisture levels, standard pre-plant application is ineffective.\n"
            "2. **Recommendation**: Switch to a **side-dress application** of UAN-28 or Urea with a urease inhibitor. "
            "Wait for soil to drain to field capacity before traffic to avoid compaction.\n"
            "3. **Rate**: Target 40-60 lbs N/acre rescue application."
        )
        
        sources = [r['title'] for r in research[:2]]
        
        return Recommendation(
            alert_level=alert,
            diagnosis="; ".join(diagnosis["anomalies"]),
            action_plan=plan,
            sources=sources
        )
