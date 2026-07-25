from client import EnterpriseAgenticCrmOrchestratorClient

def main():
    client = EnterpriseAgenticCrmOrchestratorClient()
    res = client.orchestrate_crm({"company": "Acme Corp", "estimated_mrr": 5000}, "QUALIFY")
    print(f"Pipeline Stage: {res['pipeline_stage']}")
    print(f"Next Best Action: {res['next_best_action']}")
    print(f"Notes: {res['agent_notes']}")

if __name__ == "__main__":
    main()
