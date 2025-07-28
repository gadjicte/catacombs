# 🕳️ Catacombs
### *A terminal-based fantasy adventure powered by sarcasm and AI*

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-00ADD8?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Development-FF6B35?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Terminal-1E1E1E?style=for-the-badge&logo=windowsterminal&logoColor=white)

**A modern take on classic text adventures with AI-powered companionship**

</div>

---

## 🎮 Overview

**Catacombs** reimagines the classic text adventure genre by introducing an intelligent, sarcastic AI companion that fundamentally changes how you experience dungeon crawling. Built with modern NLP capabilities and retro terminal aesthetics, it bridges the gap between nostalgia and innovation.

### Core Philosophy
- **Intelligence-Augmented Gameplay**: Your AI companion doesn't just respond to commands—it understands context, remembers your journey, and adapts its personality to your playstyle
- **Dynamic Narrative**: Every interaction shapes the story, with the AI generating contextually relevant responses that feel natural and engaging
- **Terminal-First Design**: Optimized for keyboard warriors who appreciate the purity of text-based interfaces

---

## ✨ Key Features

### 🧠 **Advanced AI Companion System**
```python
# Your companion understands natural language queries
> "What's the tactical advantage of the shadow blade?"
> "Should I rest here or push forward?"
> "Analyze my current loadout for the boss fight"
```

### 🎯 **Intelligent Game Mechanics**
- **Context-Aware Inventory Management**: Ask about items naturally - *"What's that glowing thing I picked up?"*
- **Strategic Combat Advice**: Get tactical recommendations based on your current situation
- **Dynamic Difficulty Scaling**: The AI adjusts challenge based on your performance
- **Procedural Storytelling**: Narratives that evolve based on your choices and AI interactions

### 🔧 **Technical Architecture**
- **Modular Command System**: Extensible parser supporting both classic commands and natural language
- **State Management**: Persistent game world with complex interaction tracking
- **NLP Integration**: Lightweight language model optimized for gaming contexts
- **Cross-Platform Terminal Support**: Works seamlessly across Unix, Windows, and macOS terminals

---

## 🚀 Quick Start

### Prerequisites
```bash
# Ensure you have Python 3.8+ installed
python --version

# Clone the repository
git clone https://github.com/yourusername/catacombs.git
cd catacombs
```

### Installation
```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch the game
python catacombs.py
```

### Docker Support
```bash
# Build and run with Docker
docker build -t catacombs .
docker run -it catacombs
```

---

## 🎯 Gameplay Mechanics

### Command System
The game supports both traditional text adventure commands and natural language:

```bash
# Classic Commands
go north | take sword | use potion | inventory | look

# Natural Language (AI Companion)
talk "What should I do with this mysterious key?"
ask "How do I defeat the shadow guardian?"
chat "Tell me about the lore of this place"
```

### AI Companion Capabilities
| Feature | Description | Example |
|---------|-------------|---------|
| **Contextual Help** | Provides guidance based on current situation | *"That trap looks ancient—try the disarm technique I taught you"* |
| **Item Analysis** | Explains item properties and tactical uses | *"The Venom Dagger: +3 poison damage, -1 to stealth. Perfect for your aggressive playstyle"* |
| **Strategic Planning** | Suggests optimal approaches to challenges | *"With your current mana, I'd recommend the fire spell combo"* |
| **Narrative Enhancement** | Adds flavor text and world-building | *"These catacombs predate the kingdom by centuries..."* |

---

## 🔬 Technical Deep Dive

### Architecture Overview
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Game Engine   │◄──►│   AI Companion   │◄──►│  NLP Processor  │
│                 │    │                  │    │                 │
│ • State Mgmt    │    │ • Context Aware  │    │ • Intent Parser │
│ • World Logic   │    │ • Memory System  │    │ • Entity Extract│
│ • Command Parse │    │ • Personality    │    │ • Sentiment     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

### Performance Optimizations
- **Lazy Loading**: Game assets loaded on-demand to minimize memory footprint
- **Efficient State Serialization**: Quick save/load with compressed game states
- **Optimized AI Inference**: Lightweight model with sub-100ms response times
- **Terminal Rendering**: Hardware-accelerated text rendering where available

---

## 🎨 Sample Gameplay

```text
┌─ Catacombs v1.0 ─────────────────────────────────────┐
│                                                      │
│ > examine ancient door                               │
│                                                      │
│ The door bears intricate runes that pulse with a    │
│ faint blue light. Age-old mechanisms are visible    │
│ along its edges.                                     │
│                                                      │
│ > talk "How do I open this door?"                    │
│                                                      │
│ Companion: "Those runes are Draconic—probably a     │
│ riddle lock. Try 'speak' instead of brute force.    │
│ Unless you enjoy being incinerated, of course."     │
│                                                      │
│ > speak "friend"                                     │
│                                                      │
│ The door glows brighter and slowly creaks open,     │
│ revealing a treasure chamber beyond...              │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

## 🛠️ Development Roadmap

### Phase 1: Core Systems ✅
- [x] Basic game engine and command parsing
- [x] AI companion integration
- [x] Inventory and combat systems

### Phase 2: Enhanced AI 🚧
- [ ] Advanced memory and context tracking
- [ ] Personality customization system
- [ ] Multi-language support for AI responses

### Phase 3: Content Expansion 📅
- [ ] Procedurally generated dungeons
- [ ] Multiple companion personalities
- [ ] Multiplayer cooperative mode

### Phase 4: Polish & Distribution 📅
- [ ] Steam release preparation
- [ ] Achievement system
- [ ] Comprehensive mod support

---

## 🤝 Contributing

We welcome contributions from developers, writers, and AI enthusiasts!

### Development Setup
```bash
# Fork the repository and clone your fork
git clone https://github.com/yourusername/catacombs.git

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Check code quality
flake8 catacombs/
black catacombs/
```

### Contribution Areas
- **🐍 Core Development**: Python, game logic, AI integration
- **📝 Content Creation**: Story writing, dialogue, world-building
- **🧠 AI/ML**: NLP improvements, personality modeling
- **🎨 UX/UI**: Terminal interface design, accessibility
- **📚 Documentation**: Code docs, tutorials, guides

---

## 📊 Technical Specifications

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Runtime** | Python 3.8+ | Core game engine |
| **AI/NLP** | Transformers, spaCy | Natural language processing |
| **Terminal** | Rich, Colorama | Enhanced terminal UI |
| **Data** | SQLite, JSON | Game state persistence |
| **Testing** | pytest, unittest | Quality assurance |
| **CI/CD** | GitHub Actions | Automated testing & deployment |

---

## 📄 License & Credits

```
MIT License - See LICENSE file for details
```

### Acknowledgments
- Inspired by classic text adventures like **Zork** and **Adventure**
- AI personality design influenced by **GLaDOS** and **Cortana**
- Terminal UI patterns from **Rich** and **Textual** libraries

---

<div align="center">

### 🎮 Ready to Descend?

**[Download Latest Release](https://github.com/yourusername/catacombs/releases)** | **[View Documentation](https://github.com/yourusername/catacombs/wiki)** | **[Join Discord](https://discord.gg/catacombs)**

*Built with ❤️ and excessive amounts of caffeine*

</div>