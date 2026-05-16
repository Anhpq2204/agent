import requests
from state import GraphState

def retrieve_papers(state: GraphState) -> GraphState:
    print(f"[*] Node: retrieve_papers for topic: {state['topic']}...")
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
    query_params = {
        "query": f'({state["topic"]}) AND (FIRST_PDATE:[2020 TO 2030])',
        "format": "json",
        "resultType": "core",
        "pageSize": state["limit"]
    }
    
    try:
        response = requests.get(url, params=query_params)
        response.raise_for_status()
        data = response.json()
        
        papers = []
        for item in data.get("resultList", {}).get("result", []):
            if not item.get("abstractText") or not item.get("title"):
                continue
                
            # Construct URL
            paper_url = ""
            if item.get("pmid"):
                paper_url = f"https://europepmc.org/article/MED/{item['pmid']}"
            elif item.get("pmcid"):
                paper_url = f"https://europepmc.org/article/PMC/{item['pmcid']}"
                
            papers.append({
                "title": item.get("title", ""),
                "year": str(item.get("pubYear", "Unknown")),
                "venue": item.get("journalTitle", "Unknown"),
                "abstract": item.get("abstractText", ""),
                "url": paper_url
            })
            
        print(f"[*] Retrieved {len(papers)} papers from EuropePMC.")
        return {"raw_papers": papers}
    except Exception as e:
        print(f"[*] Error retrieving papers: {e}")
        return {"raw_papers": []}
