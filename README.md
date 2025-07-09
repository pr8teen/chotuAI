# 💬 ChotuAI — Your Dumbest Smart Assistant for Kirana Shops

> “Calculator toh hai na... Chotu kyu?”  
> — Every dukaan owner, ever.

---

## 👋 Hi, I'm Prasannajeet (yes, it’s a long name)

I built **Chotu** — not because I wanted to start a startup,  
but because I saw something unfair:  

> **Everyone's building for rich startups, not small shopkeepers.**

So I made something *small, stupid-simple, but surprisingly smart*.  
Kinda like your *chhota bhai* who failed maths but now does stock predictions. 🤷‍♂️

---

## 🧠 What We *Think* Shopkeepers Need

- Billing software  
- Dashboards  
- Monthly subscriptions  
- “Premium features” (whatever that means)  
- Excel 2.0 with fancier buttons

---

## ❌ What They Actually Need

- Something that *just works*
- No setup, no coding, no training
- Talks in **Hinglish**, not jargon
- Can say **“bhaiya, stock khatam ho gaya”** when needed
- Doesn't cost more than their chai machine

Basically... **they don’t want SaaS.**  
They want **sass**. And **Chotu’s got plenty.**

---

## 🤖 Meet Chotu

> “Built using an LLM, but runs like your cousin Pintu.”

Chotu is a tiny, offline, llama3.2-powered chatbot that:

- 💬 Understands your inventory questions
- 📦 Knows stock levels
- 📊 Suggests what to reorder
- 📉 Tries to forecast, but don’t expect magic (it's still Chotu, not ChatGPT-Enterprise)
- 🤪 Tells jokes when you’re bored
- 🔢 Does math like a pro (no, seriously)
- 📓 Learns from what he doesn’t know
- 🔌 Works without internet (yes, even in *gaon waale* laptops)

We’re not promising the moon.  
We’re promising *mehmaan-level service* from a local AI.

---

## 🚨 The Brutal Truth

- ❌ No web app yet
- ❌ No fancy dashboards
- ❌ Not for enterprise-y “let’s integrate this with Salesforce” people
- ✅ Just me + my laptop + too much chai
- 🧠 Runs llama3.2 locally — **you’ll need a decent machine** (at least 8GB RAM unless you enjoy fans spinning like helicopters)

---

## 🧪 Status: Barely Alive, but Learning

**This project is not launched. Not VC funded.**  
Just an MVP — or as my mom calls it:  
> “Accha beta, ab isse paise kab aayenge?”

Used `Streamlit`, `PostgreSQL`, and `Ollama` for now because I’m testing if even 1 dukaan owner can use this *without rage-quitting*.

---

## 🎯 Target Users

We’re NOT building this for “TAM 13 million kirana shops in India”.

We’re building it for **just 10**. Yes, literally **10 shops**.

Why?

- Because we want **100% retention**, not 100k downloads.
- To **observe behavior**, not just collect metrics.
- To make something **they never want to uninstall**.

If we can change life for **10 kirana stores**,  
we’ve won more than most apps ever do.

---

## 📈 TAM - SAM - SOM (But Make It Real)

| Type | Description | Estimate |
|------|-------------|----------|
| **TAM** | All retail stores in India | ~13M |
| **SAM** | Digitally reachable ones | ~5M |
| **SOM** | Stores we’re going after | **10**

> "Everyone's selling to India. We’re *talking* to it."

---

## 🥊 Competition (We're not hating, just vibing)

### TOHANDS Smart Calculator
- ✅ Affordable
- ❌ Zero AI, just math
- ❌ No learning, no sass

### Dhanda AI (EZO)
- ✅ Prints menus and bills
- ✅ Offers long-term pricing plans
- ❌ ₹2999+ setup = **Chotu got anxiety**
- ❌ Interface not for small town folks

### Zapier, Excel, Notion templates?
- ❌ They don’t even know what kirana shops are
- ❌ Built for product managers, not Pintu bhaiya

### ✅ ChotuAI
- Free (for now)
- Tries to be funny
- Talks like your cousin
- Learns like your intern
- Crashes *only sometimes* 🥲

---

## 🔮 What’s Coming

- 📂 CSV uploader for those using pen-paper (aka 99% of India)
- 🧾 Print-friendly invoices
- 📊 Forecasting + basic charts (offline!)
- 🎙️ Voice commands in regional langs
- 🧠 Internet search fallback for unknowns
- 💬 Follow-up questions to grow business, not just answer queries
- 📽️ 2-minute video onboarding for uncles and aunties

⚠️ **System Requirements**  
> Will not work on toaster laptops.  
> Use something with a decent brain (a.k.a. 8GB+ RAM)

---

## 🤝 Why This Exists

I didn’t build this to raise funds.  
I built this because **tech should help people who don’t ask for it**.

- Not to replace jobs.  
- Not to “automate everything”.  
- But to **assist**.

If you’re here to copy it — copy with love.  
If you’re here to test it — I’ll wait for your feedback like Zomato delivery updates.  
If you’re here to improve it — *bhai, chalo milke banate hain!*

---

## 📸 Screenshots?

Nope. Not yet. This thing is still in its **chaddi phase**.

---

## 🧡 Made With

- Streamlit  
- LangChain  
- Llama3.2  
- Way too much caffeine  
- A little bit of delusion  
- A lot of hope

---

## 🙏 Final Thoughts

> “Calculator se kaam chal raha tha.”  
> — And that’s okay.

But if someday, they say:  
> **“Chotu ke bina kaam hi nahi chalta”**

Then maybe… we did something right. 💫

---

## 🛠️ How to Run (if you dare)

```bash
git clone https://github.com/yourusername/chotu-ai
cd chotu-ai

# Add a .env file like:
# DB_USER=postgres
# DB_PASSWORD=yourpass
# DB_NAME=atliq_tshirts
# DB_HOST=localhost

# Run llama3.2 using Ollama
ollama run llama3

# Then run Chotu
streamlit run main.py


---
