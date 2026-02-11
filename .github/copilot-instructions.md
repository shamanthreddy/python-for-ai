# Copilot Instructions for python-for-ai

## Project Overview
This is a Python learning and experimentation repository focused on AI, data analysis, and practical workflows. It contains standalone example scripts and a `sales_analysis/` case study demonstrating data processing patterns.

**Key Principle**: Code is organized by learning domain (API interactions, functions, data retrieval) with isolated case studies (sales_analysis) that demonstrate applied patterns.

## Architecture & Data Flow

### Root-Level Scripts
- **`apis.py`**: API interaction examples
- **`functions.py`**: Function definition patterns and tutorials
- **`get_data.py`**: Data retrieval and external data handling
- **`requirements.txt`**: Core dependencies (pandas, jupyter, httpx for HTTP requests, data processing libs)

### `sales_analysis/` Case Study
A self-contained subproject demonstrating data analysis workflow:
- **`helpers.py`**: Utility functions (`calculate_total()`, `format_currency()`) - reusable computation layer
- **`analyzer.py`**: Main analysis script that imports and uses helpers, reads CSV, processes data, outputs formatted results
- **`analyzer_with_helpers.py`**: Alternative implementation showing same data flow but with inline processing
- **`classes.py`**: OOP patterns alternative to functional approach
- **Data pipeline**: `data/sales.csv` → [read + calculate + format] → outputs (JSON, CSV, Excel)

**Critical Pattern**: `sales_analysis/` scripts assume relative paths from their directory (e.g., `data/sales.csv`, `output/` directory creation). Always run from the subdirectory root.

## Developer Workflows

### Setup & Execution
```bash
# Install dependencies
pip install -r requirements.txt

# Run root-level scripts (from project root)
python hello.py
python apis.py

# Run sales_analysis scripts (from sales_analysis/ directory)
cd sales_analysis
python analyzer.py  # Reads data/sales.csv, outputs to output/
```

### Key Files Exemplifying Patterns
- **Modular design**: [sales_analysis/analyzer.py](sales_analysis/analyzer.py) → [sales_analysis/helpers.py](sales_analysis/helpers.py)
- **Data I/O**: [sales_analysis/analyzer.py](sales_analysis/analyzer.py) uses pandas (read_csv → process → to_json/to_csv)
- **Error patterns**: [sales_analysis/try_and_except.py](sales_analysis/try_and_except.py) demonstrates exception handling

## Project-Specific Conventions

### Code Style & Patterns
1. **Modular organization**: Helper functions extracted to separate files (e.g., `helpers.py`); main scripts import and use them
2. **Data processing**: Use pandas DataFrames for CSV operations; iterate rows with `.iterrows()`
3. **Output creation**: Always use `os.makedirs('output', exist_ok=True)` before writing files to `output/`
4. **String formatting**: Use f-strings for display output; `format_currency()` pattern for user-facing numbers
5. **Imports at top**: Standard library → third-party (pandas, httpx) → local imports

### Working with sales_analysis
- Treat as a self-contained case study with its own `data/` and `output/` subdirectories
- Scripts in this folder use relative paths; they must be executed from within the folder
- `helpers.py` is the single source of truth for calculations (`calculate_total`, formatting functions)
- Extensions should follow the analyzer pattern: read CSV → apply helpers → output multiple formats

### When Adding New Code
- For root-level scripts: focus on single concepts (API usage, function patterns, data retrieval)
- For sales_analysis extensions: maintain the helper → analyzer flow; add new calculations to `helpers.py`
- Test with: `python script.py` from correct directory; check `output/` directory for file generation

## Common Paths & Import Patterns
- **Relative paths in sales_analysis**: `data/sales.csv`, `output/` (not `sales_analysis/data/`)
- **Pandas operations**: `pd.read_csv()` → `df.iterrows()` → `df.to_json()`, `df.to_csv()`, `df.to_excel()`
- **Imports in analyzer.py**: `from helpers import calculate_total, format_currency`

## Integration Points & Dependencies
- **External data**: HTTP requests via `httpx` (see requirements.txt); `get_data.py` shows patterns
- **Jupyter integration**: Full Jupyter support (ipykernel, jupyterlab); scripts can run as notebooks
- **Output formats**: JSON, CSV, Excel (all pandas-supported)
- **No database**: All data is file-based (CSV input, JSON/CSV output)
