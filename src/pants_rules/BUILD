# -*- python -*-

pex_binary(
    name="main",
    entry_point="main.py",
)

python_sources(
    overrides={
        "main.py": {"dependencies": ["src/pants_rules/demo/register.py"]},
    }
)
