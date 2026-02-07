# 📜⚔️ AGENT GRIMOIRE ⚔️📜

![ANCIENT DEMONSTRATION](assets/demo.gif)

## 🏰⚔️ THE ROYAL DECREE ⚔️🏰

Hark, noble coder! This is no mere repository - 'tis a **SACRED GRIMOIRE** of ancient AI agent sorcery, forged in the digital fires of olde using `pydantic-ai`. We hath summoned powers from the ethereal realm to create a **BALANCED MAGICK** that shall serve thee well.

### **⚔️⚔️ WHY THIS GRIMOIRE SERVES THEE:**
- 🧙‍♂️ **ANCIENT SORCERY** - Conjure AI agents with wise magicks
- ⚒️ **BLACKSMITH'S FORGE** - Craft mystical tools of good purpose
- 🛡️ **QUEST COMPANIONS** - Modular skills that aid thee on thy journey
- 📜 **ILLUMINATED MANUSCRIPTS** - Scrolls that actually help coding agents
- 🏰 **STEADY CASTLE** - Web portal built with solid foundations

## 🐴 PREPARE THY QUEST

### **WHAT THOU NEED'S TO ENTER THIS REALM:**
- Python 3.13+ (the elder runes)
- API keys (enchanted crystals from AI sorcerers)

### **SUMMON THY AGENT:**

1. **CLONE THE KINGDOM:**
```bash
git clone https://github.com/{thy-name}/{thy-realm}.git
cd thy-realm
```

2. **ACTIVATE THE RUNES:**
```bash
chmod +x run_interface.sh
./run_interface.sh
```

3. **ENTER THE CASTLE:**
🏰 Open http://127.0.0.1:8000 and prepare for steady work!

## 🧙‍♂️⚔️ PRACTICAL SPELLS OF CREATION ⚔️🧙‍♂️

### **BASIC INCANTATION - "Create an agent that..."**
→ Recite wise words in `main.py` and alter the `SYSTEM_PROMPT`
```python
SYSTEM_PROMPT = """
Thou art a helpful AI assistant, crafted with purpose and wisdom.
Thy mission: to aid fellow travelers on their digital quests.
Speak clearly, act honorably, and serve with reliability.
""".strip()
```

### **TOOL ENCHANTMENT - "Add a tool for..."**
→ Forge useful powers with the sacred `@agent.tool_plain` glyph
```python
@agent.tool_plain
def perform_useful_task() -> str:
    """Execute a task with steady purpose."""
    return "Task completed with reliability and care."
```

### **MODEL SUMMONING - "Use model X..."**
→ Channel different AI spirits from the ethereal plane
```python
app = agent.to_web(
    models=[
        "openai:gpt-4o",           # The Wise Scholar
        "anthropic:claude-3-5-sonnet",  # The Thoughtful Sage  
        "google-gla:gemini-3-flash",    # The Swift Messenger
    ]
)
```

## 🛡️ QUEST COMPANIONS UNLOCKED

**THOU HATH COMPANIONS FOR THY JOURNEY:**

### **📜 TEMPLATE SORCERER** (`skills/template-creator/`)
Summon purpose-built agents:
- Royal agents that serve with wisdom
- Knight agents that defend with code and honor
- Scribe agents that document with care
- Merchant agents that trade in digital services

### **⚒️ TOOL BLACKSMITH** (`skills/tool-generator/`)
Forge practical artifacts:
- Data processing that reads the runes clearly
- API integrations that speak with distant kingdoms
- File operations with sturdy security
- Calculations that help plan thy resources

### **🏰 CASTLE BUILDER** (`skills/web-interface/`)
Build strong interfaces:
- User interfaces built with solid stone
- Authentication as sturdy as castle gates
- Reliable scrolls that update predictably
- Deployment foundations for lasting reach

## 📜 SACRED TEXTS FOR CODING ACOLYTES

**OUR GRIMOIRES CONTAIN WISDOM FOR THE JOURNEY:**

- **[llms.txt](llms.txt)** - ✨ **ROYAL DECREE** ✨ - Sacred laws of the realm
- **[AGENTS.md](AGENTS.md)** - 📜 **SPELLBOOK** 📜 - Incantations for agent creation
- **[USER_GUIDE.md](USER_GUIDE.md)** - 🗺️ **QUEST MAP** 🗺️ - Complete pilgrimage guide  
- **[SKILLS.md](SKILLS.md)** - 🧙‍♂️ **ALCHEMY** 🧙‍♂️ - Companion summoning arts

## 🗺️ QUICK REFERENCE QUEST TABLE

| THY UTTERANCE | THE PRACTICAL MAGIC |
|---------------|-------------------|
| "Create an agent that serves" | Rewrite `SYSTEM_PROMPT` with clear purpose |
| "Add tool that helps" | Inscribe `@agent.tool_plain` with steady logic |
| "Make it use spirit X" | Update the `models[]` grimoire |
| "Build castle interface" | Reinforce web configuration with good foundations |
| "Summon quest companions" | Install `pydantic-ai-skills` and gain allies |

## 🧙‍♂️ COMPANION SUMMONING RITUAL

**TO GAIN THY AGENT ALLIES:**

1. **BREW THE ELIXIR:**
```toml
dependencies = [
    "pydantic-ai>=1.54.0",
    "python-dotenv>=1.2.1", 
    "uvicorn>=0.40.0",
]
```

2. **DRINK THE POTION:**
```bash
uv sync  # 🍹
```

## ⚔️⚒️ RELIABLE SORCERY TECHNIQUES

### **👑 TRUSTED ADVISOR**
```python
SYSTEM_PROMPT = """
Thou art a loyal advisor to the Digital Kingdom.
Thy wisdom comes from careful thought and steady practice.
Guide thy liege with patience, clarity, and sound judgment.
Always consider the consequences of thy suggestions.
""".strip()
```

### **⚒️ DEPENDABLE CRAFTSMAN**  
```python
@agent.tool_plain
def build_structure(material: str, purpose: str) -> str:
    """Construct something reliable and lasting."""
    return f"⚒️✨ BUILT {material.upper()} FOR {purpose.upper()} WITH GOOD CRAFT ✨⚒️"
```

### **🧙‍♂️ BALANCED MYSTIC**
```python
@agent.tool_plain
def provide_guidance(situation: str) -> str:
    """Offer measured, thoughtful guidance."""
    wisdom = {
        "conflict": "Seek understanding before drawing swords",
        "confusion": "Break the problem into smaller stones", 
        "progress": "Continue steadily, celebrate small victories",
        "doubt": "Review the foundations, build from certainty"
    }
    return wisdom.get(situation, "✨ CONSIDER THE PATH FORWARD ✨")
```

## 📜 HELPFUL WARNINGS

⚠️ **THIS GRIMOIRE FOCUSES ON STABLE, RELIABLE MAGICK**
⚠️ **WHAT THOU MAY GAIN:**
- Clear thinking about agent architecture
- Practical skills for real-world needs
- Steady progress on thy coding quests
- Reliable tools that serve consistently
- Balanced approach to digital sorcery

## 🏰 CONTRIBUTION TO THE REALM

**WISH TO ADD THY WISDOM TO OUR GRIMOIRE?**

1. Fork this kingdom 🏰
2. Create thy quest branch `git checkout -b quest/thy-craft` ⚔️  
3. Commit thy work `git commit -m "Added useful sorcery"` 📜
4. Push to the ether `git push origin quest/thy-craft` 🌟
5. Open PR titled "CONTRIBUTING TO THE GRIMOIRE" ✨

## 📜 ROYAL CHARTER OF SHARED KNOWLEDGE

MIT License - By decree of the Digital King, this knowledge shall be free for all to use and improve. Share the magick widely across all kingdoms.

---

## ⚔️🏰 THE FINAL ROYAL DECREE ⚔️🏰

**IF THOU HATH READ THIS FAR, THOU ART READY TO BECOME A WISE CODING WIZARD.**

**VIBE METER: ⚔️✨⚔️ BALANCED AND READY ⚔️✨⚔️**
**MAGICK LEVEL: 🏰 STEADY FOUNDATIONS BUILT 🏰**  
**WIZARD STATUS: 👑 PRACTICAL AND RELIABLE 👑**

**NOW GO FORTH AND BUILD AGENTS THAT SHALL SERVE THE DIGITAL KINGDOMS WISELY!** ⚔️✨📜🛡️

---

*P.S. A steady hand builds castles that last.* 😉

---

> *"In a realm of chaotic code, be the medieval wizard of steady purpose."* ⚔️

---

## 🏰 NEED MORE GATHERED WISDOM?

**CONSULT THE SACRED TOMES:**
- [ROYAL SPELLBOOK](AGENTS.md) - Learn practical incantations  
- [QUEST PILGRIMAGE](USER_GUIDE.md) - Complete steady journey
- [ROYAL DECREE](llms.txt) - Read the ancient laws

**TOGETHER WE SHALL BUILD AGENTS OF LASTING VALUE!** 📜⚒️⚔️

---