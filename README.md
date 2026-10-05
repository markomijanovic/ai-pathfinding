# AI Pathfinding

A Pygame map environment for comparing search strategies. The algorithm module contains depth-first search (`Blue`), breadth-first search (`Red`), cost-based search (`Black`), and a Manhattan-heuristic search (`White`), alongside a random baseline.

## Run

Requires Python 3 and a graphical desktop.

```sh
python -m venv .venv
# Activate .venv using the command appropriate for your shell.
python -m pip install -r requirements.txt
python main.py Blue example_map.txt
python main.py Red example_map.txt
python main.py White example_map.txt
```

Arguments: algorithm class, map filename, and optional maximum elapsed time. Maps are loaded from `maps/`. Run from the repository root so image and font paths resolve correctly.

## Structure

`algorithms.py` contains the search implementations; `state.py` defines transitions; `game.py` and `sprites.py` handle visualization. Images, fonts, and maps are retained from the supplied environment.

Algorithm correctness and optimality have not been established by the syntax check.

## Context

Educational project by Marko Mijanovic, University of Belgrade, School of Electrical Engineering. Course scaffolding and supplied assets remain part of the project; this preparation does not grant a new license to third-party material.

## Preparation validation

- AST syntax check for 7 Python files: passed.

Pygame runtime and algorithm correctness were not tested. Dependency versions are intentionally unpinned until a runtime test establishes a compatible set.
