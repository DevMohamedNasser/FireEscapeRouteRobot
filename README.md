# 🔥 Fire Escape Route Agent using AI Search Algorithms

## 📌 Project Overview

This project is a university **Artificial Intelligence** course project that simulates a **fire emergency scenario inside a mall**.

The system represents a **3D maze environment** where an intelligent agent acts as a **fire escape guide**.
In case of fire, this agent helps people navigate from dangerous areas to a **safe exit gate** using classical AI search algorithms.

Different search strategies are applied and visualized to analyze which algorithm provides the **most efficient escape route**, considering optimal paths and minimal visualization time under difficult conditions.

---

## 🎯 Project Objective

* Implement and compare classical **AI search algorithms**
* Simulate a realistic **fire evacuation scenario**
* Identify the **most efficient algorithm** for guiding people safely to exits
* Evaluate algorithms based on:

  * Path length
  * Number of discovered nodes
  * Total movements
  * Visualization time

---

## 🤖 Scenario Description

* The environment is represented as a **3D grid-based maze**
* The maze simulates a **mall under emergency conditions**
* Walls represent blocked paths, shops, or unsafe areas
* The agent starts from a predefined location
* The goal is a **safe exit gate**
* Each experiment runs **one algorithm at a time**
* The simulation visualizes:

  * Exploration phase
  * Final escape path
* This setup allows observing how different algorithms behave under **hard and constrained conditions**

---

## 🧠 Implemented Search Algorithms

| Algorithm                            | Description                                                                                                                          |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Breadth First Search (BFS)**       | Tries to reach the goal by exploring all neighboring nodes level by level, guaranteeing the shortest path in unweighted environments |
| **Depth First Search (DFS)**         | Explores one path deeply before backtracking                                                                                         |
| **Iterative Deepening Search (IDS)** | Combines DFS depth limits with BFS completeness                                                                                      |
| **Uniform Cost Search (UCS)**        | Expands the node with the lowest cumulative cost                                                                                     |
| **A* Search**                        | Uses both path cost and a heuristic function to efficiently reach the goal                                                           |
| **Hill Climbing**                    | A greedy approach that selects the neighbor closest to the goal                                                                      |

---

## 🛠 Technologies Used

* **Python 3**
* **PyOpenGL** (OpenGL, GLU, GLUT)
* 3D Maze visualization
* Standard Python libraries

---

## 📁 Project Structure

```
Project_code/
│
├── main.py          # Main entry point & OpenGL visualization
├── maze.py          # 3D maze, agent, and environment logic
├── search_algo.py   # AI search algorithms implementations
│
└── Team Contributions/
    └── team_members.txt
```

---

## ▶ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/DevMohamedNasser/FireEscapeRouteAgent
cd Project_code
```

### 2️⃣ Install required libraries

```bash
pip install PyOpenGL PyOpenGL_accelerate
```

> Make sure **Python 3** is installed.

### 3️⃣ Run the program

```bash
python main.py
```

You will be prompted to choose an algorithm:

| Command   | Algorithm                                 |
| --------- | ----------------------------------------- |
| `bfs`     | Breadth First Search                      |
| `dfs`     | Depth First Search                        |
| `ucs`     | Uniform Cost Search                       |
| `astar`   | A* Search                                 |
| `ids`     | Iterative Deepening Search                |
| `hill`    | Hill Climbing                             |
| `compare` | Compare all algorithms (no visualization) |

---

## 📊 Evaluation Criteria

* Path length
* Number of discovered nodes
* Total movements
* Visualization time
* Algorithm efficiency in emergency conditions

---

## 👥 Team Members

*(Sorted alphabetically)*

* Heba Ahmed Ibrahim Agamy
* Maram Hazem Fouad Ismail Ahmed
* Menna Ahmed Ibrahim Agamy
* Mohamed Elsayed Mohamed Ahmed Aboelsoud
* Mohamed Khaled El-Daheesh Ahmed
* Mohamed Refat Mustafa Abd-Elmajid Nasser
* Wessam Mohamed El-Sayed Al-Hanafy
