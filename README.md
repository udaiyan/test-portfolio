# Testing Demo - Python Pytest & Playwright

A demonstration project showcasing a modern testing framework using Python pytest and Playwright for both UI and API testing.

## 🎯 Purpose

This project demonstrates:
- **UI Testing** with Playwright and pytest
- **API Testing** with pytest and requests
- **Test Organization** with separate test suites
- **CI/CD Integration** with GitHub Actions
- **Best Practices** for automated testing

## 🛠️ Technology Stack

- **Backend**: FastAPI
- **Frontend**: Static HTML, CSS, JavaScript
- **Testing Framework**: pytest
- **UI Testing**: Playwright
- **API Testing**: requests library
- **CI/CD**: GitHub Actions

## 📁 Project Structure

```
test-portfolio/
├── app/
│   ├── main.py              # FastAPI server with REST API
│   └── static/
│       ├── index.html       # Home page with dynamic content
│       ├── form.html        # Contact form page
│       ├── about.html       # About page
│       ├── styles.css       # CSS styling
│       └── script.js        # JavaScript for interactions
├── tests/
│   ├── conftest.py          # Shared pytest fixtures
│   ├── ui_tests/            # Playwright UI tests
│   │   ├── test_navigation.py
│   │   ├── test_forms.py
│   │   └── test_dynamic_content.py
│   └── api_tests/           # API tests
│       └── test_api.py
├── .github/
│   └── workflows/
│       └── test.yml         # GitHub Actions CI/CD
├── requirements.txt         # Python dependencies
├── pytest.ini              # Pytest configuration
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository** (if using Git):
   ```bash
   git clone <repository-url>
   cd test-portfolio
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**:
   ```bash
   playwright install chromium
   ```

## 🌐 Running the Application

Start the FastAPI server:

```bash
# From the project root directory
python -m uvicorn app.main:app --reload
```

The application will be available at:
- **Website**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs (Swagger UI)
- **API**: http://localhost:8000/api/

## 🧪 Running Tests

### Run All Tests

```bash
pytest tests/ -v
```

### Run Only UI Tests

```bash
pytest tests/ui_tests/ -v -m ui
```

### Run Only API Tests

```bash
pytest tests/api_tests/ -v -m api
```

### Run Smoke Tests

```bash
pytest tests/ -v -m smoke
```

### Run Tests with Coverage

```bash
pytest tests/ --cov=app --cov-report=html
```

Then open `htmlcov/index.html` in your browser to view the coverage report.

### Run Specific Test File

```bash
pytest tests/ui_tests/test_navigation.py -v
```

## 📡 API Endpoints

The demo includes a simple REST API:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Health check endpoint |
| GET | `/api/items` | List all items |
| POST | `/api/items` | Create a new item |
| GET | `/api/items/{id}` | Get item by ID |
| DELETE | `/api/items/{id}` | Delete item by ID |

### Example API Usage

```bash
# Health check
curl http://localhost:8000/api/health

# Get all items
curl http://localhost:8000/api/items

# Create a new item
curl -X POST http://localhost:8000/api/items \
  -H "Content-Type: application/json" \
  -d '{"name": "New Item", "description": "Test item"}'

# Get specific item
curl http://localhost:8000/api/items/1

# Delete item
curl -X DELETE http://localhost:8000/api/items/1
```

## 🧩 Test Coverage

### UI Tests (32 tests)
- **Navigation Tests** (8 tests): Page routing, links, titles
- **Form Tests** (11 tests): Validation, submission, reset
- **Dynamic Content Tests** (13 tests): Data loading, toggles, API interaction

### API Tests (21 tests)
- **Health Check** (3 tests): Endpoint availability
- **CRUD Operations** (15 tests): Create, read, delete operations
- **Error Handling** (3 tests): 404 responses, validation

## 🔧 Configuration

### pytest.ini

Customize pytest behavior:
- Test discovery patterns
- Custom markers (ui, api, smoke, slow)
- Output verbosity
- Asyncio mode

### Playwright Configuration

Browser settings are configured in `tests/conftest.py`:
- Viewport size: 1280x720
- Browser context options
- Automatic server startup/teardown

## 🚦 CI/CD

The project includes a GitHub Actions workflow that:
- Runs on push to main/develop branches
- Tests against Python 3.10 and 3.11
- Executes UI and API tests separately
- Generates coverage reports
- Archives test results
- Optional linting with flake8 and black

## 📝 Best Practices Demonstrated

1. **Test Organization**: Separate directories for UI and API tests
2. **Fixtures**: Reusable fixtures for server, API client, and page objects
3. **Markers**: Custom pytest markers for test categorization
4. **Assertions**: Clear, descriptive test assertions
5. **Documentation**: Docstrings for test classes and methods
6. **CI/CD**: Automated testing on code changes

## 🎓 Learning Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Playwright Python Documentation](https://playwright.dev/python/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

## 🤝 Contributing

This is a demonstration project. Feel free to:
- Fork and modify for your own learning
- Suggest improvements via issues
- Add more test scenarios
- Enhance the UI/API features

## 📄 License

This project is created for demonstration and educational purposes.

## 🙋 Support

For questions or issues:
1. Check the test output for detailed error messages
2. Review pytest and Playwright documentation
3. Ensure all dependencies are installed correctly
4. Verify Python version compatibility (3.10+)

---

**Happy Testing! 🚀**
