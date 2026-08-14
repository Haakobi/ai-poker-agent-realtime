# ♠️ Autonomous Real-Time AI Poker Bot

An autonomous Texas Hold'em poker agent engineered to play against live dealer servers and human/bot opponents over low-latency WebSockets. Developed in Python (via Visual Studio Code and Codex) during **The AI Collective Hackathon**.

## 🎯 Overview & Platform Architecture

The bot functions as an external client that maintains a persistent WebSocket connection to the platform host. 
* **The Platform Host:** Owns the orchestration, game state, and WebSocket gameplay.
* **The Communication Protocol:** Bots send `register` and `action` messages, while the platform sends `cards`, `turn`, `event`, `showdown`, and `lifecycle` messages. 
* **Performance Constraints:** The agent must evaluate the board and respond within a strict 30-second auto-fold timer. It connects to the game via ngrok WebSocket endpoints (e.g., `wss://crushing-swear-unseen.ngrok-free.dev`) using designated invite codes.

## 🧠 Engineering Methodology: Start Simple, Then Add Adaptation

The development of this agent followed a strict maturity ladder, progressing from making valid moves to behaving stably, passing benchmark cases, improving based on game behavior, adapting to opponents, and using auto-evaluation loops.

1. **Reactive Baseline:** Established a fixed prompt, ensured rule compliance, and validated basic actions to make the agent legal, stable, and debuggable.
2. **Reasoned Action Selection:** Added structured decision steps for each move to improve local choices without overcomplicating the system.
3. **Reflective Improvement Loop:** Built mechanisms to review past hands, inspect mistakes, and revise prompts or logic to learn from repeated failures.
4. **Advanced Optimization:** Integrated opponent modeling and automated evaluation to transition toward an exploit-aware agent.

## 🧪 Testing & Verification

To ensure improvements were reproducible and basic functionality did not break, the agent was verified using:
* Hard constraints and smoke checks.
* Golden set/regression set testing to compare the new version against the old version.
* A/B testing and agent-as-a-judge reviews.

## 🚀 Future Roadmap: Where to Improve

* **History Handling:** Track opponent actions across multiple hands.
* **Reviewer / Judge Layer:** Implement a system to inspect bad decisions post-game.
* **Exploit Layer:** Identify and capitalize on recurring weaknesses in opponents.
* **Theory of Mind:** Model what opponents believe about my agent's strategy.
![AI Collective Live Poker Table](Poker.JFIF)
![AI Collective Live Poker Table](Mystep.JFIF)