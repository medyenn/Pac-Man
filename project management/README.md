-project_management/05-team-organization.md
Team Organization & Workflow
Our team operates using an asynchronous "relay" strategy. Rather than strictly dividing modules, we work in sequential shifts.

The Baton Pass: When a developer finishes a work session, they push their functional code to the main branch along with a detailed summary in 02-progress-tracking.md explaining exactly what was modified and what the next logical step is.

Validation: The incoming developer reviews the previous commit, tests the current build, and begins the next phase. This ensures both developers touch all parts of the codebase (engine, AI, UI) and fully understand the entire architecture.

-project_management/02-progress-tracking.md
This file becomes your literal communication log and satisfies the requirement to track actual progress.

Progress & Changelog

Date: [Insert Date] | Developer: [Your Name]

Completed: Initialized the core Game engine router and the GameState abstract interface.

Completed: Built MenuState with functional Start/Quit buttons and PlayingState that successfully parses and renders the imperfect maze from the external mazegenerator package.

Notes for Next Shift: The grid displays correctly, and you can press ESC to return to the menu. The next step is to implement the ConfigParser to replace the hardcoded WIDTH = 20 and HEIGHT = 20 in main.py, or to start building the Player entity so we can move around the grid.

-project_management/01-timeline.md
Keep this high-level so graders can see your overall roadmap.

Project Milestones

Milestone 1: Core Engine, State Machine, and Maze Rendering (ONGOING)

Milestone 2: Config.json Parsing and Player Movement

Milestone 3: Ghost AI (BFS Pathfinding) and Pellet Consumption

Milestone 4: Highscore File I/O, UI Polish, and Cheat Mode