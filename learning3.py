tenants = {
    "John": {"stay": 14, "feedback": [5, 4, 5]},
    "Emily": {"stay": 9, "feedback": [3, 4]},
    "Sam": {"stay": 20, "feedback": []},
    "Anna": {"stay": 5, "feedback": [4]},
}

def tenant_feedback_summary(tenants,stay):
    return {
        tenant: round(sum((tenants[tenant]["feedback"])) / len(tenants[tenant]["feedback"]),1) 
        if tenants[tenant]["feedback"] else "No feedback"
        for tenant in tenants if tenants[tenant]["stay"] >= stay
    }

print(tenant_feedback_summary(tenants, 7))