# print_routes.py
from importlib import import_module
import os, sys

try:
    m = import_module('app')
    app = getattr(m, 'app', None)
except Exception:
    import importlib.util
    p = os.path.join(os.path.dirname(__file__), 'app.py')
    spec = importlib.util.spec_from_file_location('app_by_path', p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    app = getattr(m, 'app', None)

if app is None:
    raise SystemExit("Could not find 'app' Flask instance in app.py. Check app.py")

for rule in sorted(app.url_map.iter_rules(), key=lambda r: str(r)):
    methods = ",".join(sorted(rule.methods - {"HEAD", "OPTIONS"}))
    print(f"{rule} -> {rule.endpoint} [{methods}]")
