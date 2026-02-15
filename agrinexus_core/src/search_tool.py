import random
import time
try:
    from duckduckgo_search import DDGS
except ImportError:
    DDGS = None

class AgriSearch:
    """
    Search engine wrapper. Uses DuckDuckGo for live data but includes
    a deterministic simulation mode for robust article demos.
    """
    def __init__(self, simulation_mode: bool = True):
        self.simulation_mode = simulation_mode
        self.mock_db = {
            "corn nitrogen deficiency treatments": [
                {"title": "Management of Nitrogen Deficiency in Corn", "body": "Apply side-dress nitrogen immediately at V4-V8 stages. Sources like UAN or Urea are effective. Rate: 40-60 lbs/acre. Delayed application can recover up to 90% of yield potential."},
                {"title": "Identifying Nutrient Deficiencies in Corn", "body": "Yellowing in V-shape starting at leaf tip indicates N deficiency. Wet soils can exacerbate leaching, requiring supplemental N."},
                {"title": "Wet Season Corn Nitrogen Management", "body": "In years with excessive rainfall, additional N applications (30-50 lbs N/acre) are profitable. Rescue applications must occur before silking."}
            ],
            "corn nitrogen deficiency heavy rainfall": [
                 {"title": "Nitrogen Loss from Heavy Rains", "body": "Heavy rainfall causes denitrification and leaching. For every inch of rain above soil saturation, expect 2-4% nitrate loss. Supplemental N is critical."},
            ],
            "soybean moisture requirements": [
                {"title": "Soybean Water Requirements", "body": "Soybeans require 15-25 inches of water per season. Critical period is pod filling (R3-R6)."},
            ]
        }

    def search(self, query: str, max_results: int = 3):
        """
        Executes a search query.
        """
        print(f"  [SEARCH ENGINE] Searching for: '{query}'...")
        
        if self.simulation_mode:
            # Deterministic Mock for Article Consistency
            time.sleep(0.8) # Simulate network latency
            # Simple keyword matching for mock DB
            query_lower = query.lower()
            
            # Prioritize matches
            results = []
            for key, res_list in self.mock_db.items():
                if all(k in query_lower for k in key.split()):
                    results.extend(res_list)
            
            if results:
                return results[:max_results]
            
            # Fallback generic mock if no match
            return [
                {"title": f"Agricultural Bulletin: {query}", "body": f"Recent studies show that regarding {query}, optimal management requires monitoring soil conditions and weather patterns closely."}
            ]

        # Live Mode (Best Effort)
        if DDGS:
            try:
                # DuckDuckGo rate limits can be strict, so we wrap in try-except
                results = DDGS().text(query, max_results=max_results)
                return [{"title": r['title'], "body": r['body']} for r in results]
            except Exception as e:
                print(f"  [WARNING] Search API failed: {e}. Falling back to simulations.")
                pass
        
        # Fallback to mock if DDG fails or not available
        return self.mock_db.get("corn nitrogen deficiency treatments") 
