# Demon Back

My first Pygame project. A short top-down adventure: a stranger sends you to help a frog get his cookies back from goblins. Fight through seven levels to the goblin king.

![preview](the_code/preview.gif)

## Controls

- Move: WASD or arrows
- Attack: space
- Dodge: shift

## Run

```bash
pip install pygame
python demonBack.py
```

Run from the repo root. `demonBack.py` steps through the levels as a state machine (`the_code/levels.py`); sprites, walls and assets live in `the_code/`.

## Notes

Old project, rough edges. The game loop isn't optimized, enemies don't collide with each other, and hits only register when you're right on top of them. Art credits are in the in-game credits screen.
