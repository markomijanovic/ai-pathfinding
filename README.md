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

## Search strategies

| Class | Strategy |
|---|---|
| `ExampleAlgorithm` | Random legal actions |
| `Blue` | Depth-first graph search |
| `Red` | Breadth-first graph search with a FIFO deque |
| `Black` | Uniform-cost search |
| `White` | Cost plus a Manhattan-based assignment heuristic |

The heuristic uses greedy goal assignment; admissibility and optimality are not guaranteed. Random search can fail to terminate on difficult maps.

## Structure

`algorithms.py` contains the search implementations; `state.py` defines transitions; `game.py` and `sprites.py` handle visualization. Images, fonts, and maps are retained from the supplied environment.

Algorithm correctness and optimality have not been established by the syntax check.

## Search checks

Run `python -m unittest discover -s tests -v`. These standard-library tests use a small synthetic graph to check breadth-first edge count, uniform-cost route cost, already-solved states, and unreachable goals. Desktop configuration is isolated during the tests; full map integration and the heuristic remain outside their scope.

## Context

Educational project by [Marko Mijanovic](https://github.com/markomijanovic), University of Belgrade, School of Electrical Engineering. Supplied course scaffolding and assets retain their original licensing terms.

## Verification

- Python syntax checks and three synthetic graph tests passed.
- Full Pygame/map integration and heuristic optimality have not been verified. Dependency versions remain unpinned until desktop validation establishes a compatible set.
