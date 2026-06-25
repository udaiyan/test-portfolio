# Testing Demo - Quick Start Guide

## ✅ Setup Complete!

Your testing demonstration project is fully configured with:
- **52 Total Tests**: 20 API tests + 32 UI tests
- **FastAPI Backend** running on http://localhost:8000
- **Pytest + Playwright** testing framework

## 🚀 Quick Commands

### View the Website
Open your browser and visit:
- **Home**: http://localhost:8000
- **Contact Form**: http://localhost:8000/form.html
- **About**: http://localhost:8000/about.html
- **API Docs**: http://localhost:8000/docs

### Run Tests

```powershell
# Run all tests (52 tests)
python -m pytest tests/ -v

# Run only API tests (20 tests)
python -m pytest tests/api_tests/ -v

# Run only UI tests (32 tests)
python -m pytest tests/ui_tests/ -v

# Run smoke tests only
python -m pytest tests/ -v -m smoke

# Run with coverage report
python -m pytest tests/ --cov=app --cov-report=html
```

### Server Management

The server is currently running in the background. To manage it:

```powershell
# Server is already running at http://localhost:8000

# To stop the server later, press Ctrl+C in the terminal window
# Or restart it with:
python -m uvicorn app.main:app --reload
```

## 📊 Test Breakdown

### API Tests (20 tests)
- ✅ Health Check Endpoint (3 tests)
- ✅ GET /api/items - List all items
- ✅ POST /api/items - Create new item
- ✅ GET /api/items/{id} - Get specific item
- ✅ DELETE /api/items/{id} - Delete item
- ✅ Error handling (404 responses)

### UI Tests (32 tests)

**Navigation Tests (8 tests)**
- Page loading and titles
- Navigation links functionality
- Active link states
- Logo visibility

**Form Tests (11 tests)**
- Form elements presence
- Validation (empty fields, invalid email, short inputs)
- Successful submission
- Reset functionality
- Placeholder text

**Dynamic Content Tests (13 tests)**
- Button presence and visibility
- Data loading from API
- Toggle functionality
- Button text changes
- Feature cards display

## 🎯 Demo Features

### Website Features
1. **Navigation** - Three pages with working links
2. **Contact Form** - Client-side validation
3. **Dynamic Content** - Load data from API with JavaScript
4. **Toggle Content** - Show/hide functionality
5. **Responsive Design** - Mobile-friendly layout

### Testing Features
1. **Separate Test Organization** - ui_tests/ and api_tests/
2. **Pytest Markers** - @pytest.mark.ui and @pytest.mark.api
3. **Shared Fixtures** - Auto server startup/teardown
4. **Browser Automation** - Playwright for UI testing
5. **API Testing** - requests library for REST API

## 🔧 Troubleshooting

### If tests fail:
1. Make sure the server is running (http://localhost:8000/api/health should respond)
2. Check that Playwright browsers are installed: `playwright install chromium`
3. Verify all dependencies: `pip install -r requirements.txt`

### If the server won't start:
1. Check if port 8000 is already in use
2. Try a different port: `python -m uvicorn app.main:app --port 8001`

## 📖 Next Steps

1. **Explore the website** - Visit http://localhost:8000
2. **Try the API** - Visit http://localhost:8000/docs for Swagger UI
3. **Run the tests** - Execute `python -m pytest tests/ -v`
4. **Review test code** - Check tests/ui_tests/ and tests/api_tests/
5. **Modify and extend** - Add your own tests and features!

## 📝 File Structure

```
test-portfolio/
├── app/
│   ├── main.py           # FastAPI server
│   └── static/           # HTML, CSS, JS files
├── tests/
│   ├── conftest.py       # Shared fixtures
│   ├── api_tests/        # API tests
│   └── ui_tests/         # Playwright tests
├── requirements.txt      # Dependencies
├── pytest.ini           # Pytest config
└── README.md            # Full documentation
```

---

**Happy Testing! 🎉**

For more details, see the full README.md file.
