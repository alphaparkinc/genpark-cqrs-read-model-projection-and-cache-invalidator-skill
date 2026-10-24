"""CQRS Read-Model Projection & Cache Invalidator.
100% Python Standard Library.
"""

class CQRSReadModelProjector:
    """Projects write events into denormalized read models and issues cache invalidation tags."""

    @staticmethod
    def project_and_invalidate(events: list) -> dict:
        view = {}
        invalidation_tags = set()

        for evt in events:
            entity_id = evt.get("entity_id")
            field = evt.get("field")
            val = evt.get("value")
            if entity_id:
                view.setdefault(entity_id, {})[field] = val
                invalidation_tags.add(f"entity:{entity_id}")
                invalidation_tags.add(f"field:{field}")

        return {
            "projected_entities_count": len(view),
            "projected_view": view,
            "invalidation_tags": sorted(list(invalidation_tags))
        }
