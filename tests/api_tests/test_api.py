import pytest
import requests


@pytest.mark.api
class TestHealthEndpoint:
    """Test suite for health check endpoint"""

    def test_health_check_returns_200(self, api_client):
        """Test that health endpoint returns 200 status"""
        response = api_client.get("/api/health")
        assert response.status_code == 200

    def test_health_check_response_structure(self, api_client):
        """Test that health endpoint returns correct structure"""
        response = api_client.get("/api/health")
        data = response.json()

        assert "status" in data
        assert "message" in data
        assert data["status"] == "healthy"

    def test_health_check_message(self, api_client):
        """Test that health endpoint returns expected message"""
        response = api_client.get("/api/health")
        data = response.json()

        assert "running" in data["message"].lower()


@pytest.mark.api
class TestItemsEndpoints:
    """Test suite for items CRUD endpoints"""

    def test_get_all_items_returns_200(self, api_client):
        """Test that GET /api/items returns 200"""
        response = api_client.get("/api/items")
        assert response.status_code == 200

    def test_get_all_items_returns_list(self, api_client):
        """Test that GET /api/items returns list of items"""
        response = api_client.get("/api/items")
        data = response.json()

        assert "items" in data
        assert isinstance(data["items"], list)

    def test_get_all_items_contains_default_items(self, api_client):
        """Test that default items are present"""
        response = api_client.get("/api/items")
        data = response.json()

        # Should have at least 2 default items
        assert len(data["items"]) >= 2

        # Check first item structure
        first_item = data["items"][0]
        assert "id" in first_item
        assert "name" in first_item
        assert "description" in first_item

    def test_create_item_returns_201_or_200(self, api_client):
        """Test that POST /api/items creates a new item"""
        new_item = {
            "name": "Test Item",
            "description": "This is a test item"
        }

        response = api_client.post("/api/items", json=new_item)
        assert response.status_code in [200, 201]

    def test_create_item_returns_created_item(self, api_client):
        """Test that POST /api/items returns the created item with ID"""
        new_item = {
            "name": "Another Test Item",
            "description": "Testing creation"
        }

        response = api_client.post("/api/items", json=new_item)
        data = response.json()

        assert "id" in data
        assert data["name"] == new_item["name"]
        assert data["description"] == new_item["description"]
        assert isinstance(data["id"], int)

    def test_create_item_without_description(self, api_client):
        """Test creating an item without description"""
        new_item = {
            "name": "Item Without Description"
        }

        response = api_client.post("/api/items", json=new_item)
        assert response.status_code in [200, 201]

        data = response.json()
        assert data["name"] == new_item["name"]
        assert "id" in data

    def test_get_specific_item_returns_200(self, api_client):
        """Test that GET /api/items/{id} returns 200 for existing item"""
        response = api_client.get("/api/items/1")
        assert response.status_code == 200

    def test_get_specific_item_returns_correct_item(self, api_client):
        """Test that GET /api/items/{id} returns correct item data"""
        response = api_client.get("/api/items/1")
        data = response.json()

        assert data["id"] == 1
        assert "name" in data
        assert "description" in data

    def test_get_nonexistent_item_returns_404(self, api_client):
        """Test that GET /api/items/{id} returns 404 for non-existent item"""
        response = api_client.get("/api/items/99999")
        assert response.status_code == 404

    def test_get_nonexistent_item_error_message(self, api_client):
        """Test error message for non-existent item"""
        response = api_client.get("/api/items/99999")
        data = response.json()

        assert "detail" in data
        assert "not found" in data["detail"].lower()

    def test_delete_item_returns_200(self, api_client):
        """Test that DELETE /api/items/{id} returns 200"""
        # First create an item to delete
        new_item = {"name": "Item to Delete", "description": "Will be deleted"}
        create_response = api_client.post("/api/items", json=new_item)
        created_item = create_response.json()
        item_id = created_item["id"]

        # Delete the item
        delete_response = api_client.delete(f"/api/items/{item_id}")
        assert delete_response.status_code == 200

    def test_delete_item_returns_deleted_item(self, api_client):
        """Test that DELETE returns the deleted item info"""
        # Create item
        new_item = {"name": "Item to Delete 2", "description": "Will be deleted"}
        create_response = api_client.post("/api/items", json=new_item)
        item_id = create_response.json()["id"]

        # Delete item
        delete_response = api_client.delete(f"/api/items/{item_id}")
        data = delete_response.json()

        assert "message" in data or "item" in data

    def test_delete_nonexistent_item_returns_404(self, api_client):
        """Test that deleting non-existent item returns 404"""
        response = api_client.delete("/api/items/99999")
        assert response.status_code == 404

    def test_item_deleted_is_not_accessible(self, api_client):
        """Test that deleted item cannot be retrieved"""
        # Create and delete item
        new_item = {"name": "Item to Delete 3"}
        create_response = api_client.post("/api/items", json=new_item)
        item_id = create_response.json()["id"]

        api_client.delete(f"/api/items/{item_id}")

        # Try to get deleted item
        get_response = api_client.get(f"/api/items/{item_id}")
        assert get_response.status_code == 404


@pytest.mark.api
@pytest.mark.smoke
class TestAPISmoke:
    """Quick smoke tests for API availability"""

    def test_api_is_accessible(self, api_client):
        """Smoke test: API is accessible"""
        response = api_client.get("/api/health")
        assert response.status_code == 200

    def test_items_endpoint_responds(self, api_client):
        """Smoke test: Items endpoint responds"""
        response = api_client.get("/api/items")
        assert response.status_code == 200

    def test_api_returns_json(self, api_client):
        """Smoke test: API returns JSON content"""
        response = api_client.get("/api/health")
        assert "application/json" in response.headers.get("content-type", "")
