# Pylint report

```
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:8:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:34:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:39:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:42:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:46:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module shows
shows.py:1:0: C0114: Missing module docstring (missing-module-docstring)
shows.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
shows.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)
shows.py:34:0: C0116: Missing function or method docstring (missing-function-docstring)
shows.py:62:0: C0116: Missing function or method docstring (missing-function-docstring)
shows.py:88:0: C0116: Missing function or method docstring (missing-function-docstring)
shows.py:102:0: C0116: Missing function or method docstring (missing-function-docstring)
shows.py:111:0: C0116: Missing function or method docstring (missing-function-docstring)
shows.py:119:0: C0116: Missing function or method docstring (missing-function-docstring)
shows.py:128:0: C0116: Missing function or method docstring (missing-function-docstring)
shows.py:136:0: C0116: Missing function or method docstring (missing-function-docstring)
shows.py:149:0: C0116: Missing function or method docstring (missing-function-docstring)
shows.py:165:0: C0116: Missing function or method docstring (missing-function-docstring)
shows.py:174:0: C0116: Missing function or method docstring (missing-function-docstring)
shows.py:182:0: C0116: Missing function or method docstring (missing-function-docstring)
shows.py:190:0: C0116: Missing function or method docstring (missing-function-docstring)
shows.py:200:0: C0116: Missing function or method docstring (missing-function-docstring)
shows.py:210:0: C0116: Missing function or method docstring (missing-function-docstring)
shows.py:218:0: C0116: Missing function or method docstring (missing-function-docstring)
shows.py:226:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module db
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:7:0: C0413: Import "import routes" should be placed at the top of the module (wrong-import-position)
app.py:7:0: W0611: Unused import routes (unused-import)
************* Module routes
routes.py:1:0: C0114: Missing module docstring (missing-module-docstring)
routes.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
routes.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
routes.py:44:0: C0116: Missing function or method docstring (missing-function-docstring)
routes.py:60:0: C0116: Missing function or method docstring (missing-function-docstring)
routes.py:82:0: C0116: Missing function or method docstring (missing-function-docstring)
routes.py:105:0: C0116: Missing function or method docstring (missing-function-docstring)
routes.py:117:0: C0116: Missing function or method docstring (missing-function-docstring)
routes.py:129:0: C0116: Missing function or method docstring (missing-function-docstring)
routes.py:153:0: C0116: Missing function or method docstring (missing-function-docstring)
routes.py:165:0: C0116: Missing function or method docstring (missing-function-docstring)
routes.py:170:0: C0116: Missing function or method docstring (missing-function-docstring)
routes.py:176:0: C0116: Missing function or method docstring (missing-function-docstring)
routes.py:189:0: C0116: Missing function or method docstring (missing-function-docstring)
routes.py:198:0: C0116: Missing function or method docstring (missing-function-docstring)
routes.py:210:0: C0116: Missing function or method docstring (missing-function-docstring)
routes.py:1:0: R0401: Cyclic import (app -> routes -> users -> db) (cyclic-import)
routes.py:1:0: R0401: Cyclic import (app -> routes -> shows -> db) (cyclic-import)
routes.py:1:0: R0401: Cyclic import (app -> routes) (cyclic-import)

------------------------------------------------------------------
Your code has been rated at 8.14/10 (previous run: 8.17/10, -0.03)
```

## What hasn't been fixed and why

### Docstring errors

Most of the application's pylint errors are about missing docstrings, i.e.: 

```
routes.py:1:0: C0114: Missing module docstring (missing-module-docstring)
routes.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
```

These errors haven't been fixed because I've decided to not use docstrings for this application.
The application's functions are relatively simple and their names are descriptive enough that it should be enough for the scope of this project.

### Import errors

Below we have the errors related to imports:

```
************* Module app
app.py:7:0: W0611: Unused import routes (unused-import)
************* Module routes
routes.py:1:0: R0401: Cyclic import (app -> routes -> users -> db) (cyclic-import)
routes.py:1:0: R0401: Cyclic import (app -> routes -> shows -> db) (cyclic-import)
routes.py:1:0: R0401: Cyclic import (app -> routes) (cyclic-import)
```

The application doesn't work without the "Unused import routes", which is why it's still there,
and the cyclic import errors are directly related to this. 