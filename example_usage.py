"""Example usage for CQRS Read-Model Projector."""
from client import CQRSReadModelProjector

if __name__ == "__main__":
    res = CQRSReadModelProjector.project_and_invalidate([
        {"entity_id": "usr_101", "field": "email", "value": "test@genpark.ai"}
    ])
    print("Projected View:", res["projected_view"], "Tags:", res["invalidation_tags"])
