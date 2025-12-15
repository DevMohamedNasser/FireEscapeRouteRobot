# 🏬 Mall Exit Optimization using AI Search Algorithms

## 📌 Project Overview

This is a collaborative university project for the Artificial Intelligence course.
The project simulates a **shopping mall environment** where multiple autonomous robots attempt to reach an **exit point** using different AI search algorithms.

Each robot is programmed with a specific search strategy.
The algorithm that reaches the exit **faster and more efficiently** is selected as the best solution for real-world deployment.

---

## 🎯 Project Objective

* Apply and compare classical **AI search algorithms**
* Analyze performance based on:

  * Time to reach the exit
  * Path length
  * Optimality
* Determine the most efficient navigation strategy

---

## 🤖 Scenario Description

* The mall is represented as a **2D grid map**
* Obstacles represent walls, shops, or blocked paths
* All robots start from the same position
* Each robot runs **one search algorithm at a time**
* The robot that reaches the **exit point first** is considered the optimal solution

> ⚠ To ensure fair comparison, only **one agent is executed per run** (no collisions).

---

## 🧠 Implemented Search Algorithms

| Algorithm                        | Description                                     |
| -------------------------------- | ----------------------------------------------- |
| Breadth First Search (BFS)       | Finds shortest path in unweighted graphs        |
| Depth First Search (DFS)         | Explores depth-first paths                      |
| Iterative Deepening Search (IDS) | Combines DFS depth limits with BFS completeness |
| Uniform Cost Search (UCS)        | Finds the lowest cumulative cost path           |
| A* Search                        | Uses heuristic to optimize search               |
| Hill Climbing                    | Greedy local optimization search                |

---

## 🛠 Technologies Used

* **Python 3**
* Standard Python libraries
* Terminal-based simulation

---

## ▶ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/DevMohamedNasser/SafeExit-AI.git
cd SafeExit-AI
```

### 2️⃣ Run the program

```bash
python main.py
```

> Make sure Python 3 is installed on your system.

---

## 👥 Team Members & Responsibilities

### 🔹 A* Search

* Mohamed Refat Mustafa
* Abd-Elmajid Nasser
  **ID:** 2023176

---

### 🔹 Iterative Deepening Search (IDS)

* Mohamed Khaled El-Daheesh
  **ID:** 2023174

---

### 🔹 Breadth First Search (BFS)

* Mohamed Elsayed Mohamed
* Ahmed Aboelsoud
  **ID:** 2023168

---

### 🔹 Project Management

* Maram Hazem Fouad
* Ismail Ahmed
  **ID:** 2023202

---

### 🔹 Hill Climbing Search

* Menna Ahmed
* Ibrahim Agamy
  **ID:** 2023222

---

### 🔹 Uniform Cost Search (UCS)

* Heba Ahmed Ibrahim
* Agamy
  **ID:** 2023244

---

### 🔹 Depth First Search (DFS)

* Wessam Mohamed El-Sayed
* Al-Hanafy
  **ID:** 2023249

---

## 📊 Evaluation Criteria

* Path length
* Execution time
* Search optimality
* Algorithm efficiency

---

## 🚀 Future Enhancements

* Visual simulation using Pygame
* Dynamic obstacles
* Multi-agent environment
* Performance comparison charts

---

## 📜 License

This project is developed for educational purposes only.
