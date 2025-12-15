# Phase 14: AI Agents - Post-Quiz

Test your knowledge after completing the AI Agents phase.

---

## Instructions

- Answer all 10 questions
- Try to answer without referring to materials
- Time limit: 20 minutes
- Compare your score with the pre-quiz!

---

## Questions

### Question 1
**Which tool schema property tells the LLM WHEN to use a function?**

- A) name
- B) description
- C) parameters
- D) required

<details>
<summary>Answer</summary>
B) description

**Explanation:** The description field explains what the function does and when it should be used, helping the LLM make intelligent tool selection decisions.
</details>

---

### Question 2
**In the ReAct pattern, what comes after an Action?**

- A) Final Answer
- B) Another Action
- C) Observation
- D) Thought

<details>
<summary>Answer</summary>
C) Observation

**Explanation:** The ReAct loop is: Thought → Action → Observation → (repeat) → Final Answer. Observations provide results of actions.
</details>

---

### Question 3
**What is the purpose of the `max_iterations` parameter in agent loops?**

- A) To make the agent faster
- B) To prevent infinite loops
- C) To improve accuracy
- D) To reduce costs

<details>
<summary>Answer</summary>
B) To prevent infinite loops

**Explanation:** max_iterations caps the number of agent steps, preventing the agent from looping forever if it can't reach a final answer.
</details>

---

### Question 4
**Which validation is most critical for a date input parameter?**

- A) Check if it's a string
- B) Verify the format (YYYY-MM-DD) and logical validity
- C) Make sure it's not empty
- D) Convert to uppercase

<details>
<summary>Answer</summary>
B) Verify the format (YYYY-MM-DD) and logical validity

**Explanation:** Dates need format validation (correct pattern) AND logic validation (not in past if required, start < end, etc.).
</details>

---

### Question 5
**What's the main advantage of using `enum` in parameter schemas?**

- A) Faster execution
- B) Limits choices to valid options
- C) Reduces token usage
- D) Improves accuracy

<details>
<summary>Answer</summary>
B) Limits choices to valid options

**Explanation:** Enums restrict the LLM to a predefined set of valid values, preventing invalid inputs.
</details>

---

### Question 6
**In a multi-agent system, what role does a "Planner" agent typically have?**

- A) Executing all tasks
- B) Breaking down complex tasks into steps
- C) Reviewing outputs for quality
- D) Managing API calls

<details>
<summary>Answer</summary>
B) Breaking down complex tasks into steps

**Explanation:** Planner agents analyze the overall task and create a step-by-step plan for other agents to execute.
</details>

---

### Question 7
**What is "short-term memory" in agent systems?**

- A) The model's training data
- B) Recent conversation history
- C) Cached API responses
- D) User profile data

<details>
<summary>Answer</summary>
B) Recent conversation history

**Explanation:** Short-term memory stores the current conversation context (recent messages) for immediate reference.
</details>

---

### Question 8
**Why use exponential backoff in retry logic?**

- A) To fail faster
- B) To give services time to recover between retries
- C) To save money
- D) To improve accuracy

<details>
<summary>Answer</summary>
B) To give services time to recover between retries

**Explanation:** Exponential backoff (1s, 2s, 4s, 8s...) prevents overwhelming struggling services with rapid retry attempts.
</details>

---

### Question 9
**Which LangChain component manages the agent's decision-making?**

- A) Tools
- B) Memory
- C) AgentExecutor
- D) Chains

<details>
<summary>Answer</summary>
C) AgentExecutor

**Explanation:** The AgentExecutor runs the agent loop, deciding which tools to call and when to stop.
</details>

---

### Question 10
**What is "self-correction" in the ReAct pattern?**

- A) Fixing syntax errors
- B) The agent detecting mistakes and trying different approaches
- C) Error handling in code
- D) Validating inputs

<details>
<summary>Answer</summary>
B) The agent detecting mistakes and trying different approaches

**Explanation:** Self-correction occurs when the agent sees an error/unexpected result and reasons about how to fix it, then tries again.
</details>

---

## Advanced Questions (Bonus)

### Question 11
**What's the primary difference between LangChain and LangGraph?**

- A) LangChain is faster
- B) LangGraph provides graph-based workflow control
- C) LangChain is newer
- D) There's no difference

<details>
<summary>Answer</summary>
B) LangGraph provides graph-based workflow control

**Explanation:** LangGraph extends LangChain with graph-based state management, enabling more complex agent architectures with cycles and conditionals.
</details>

---

### Question 12
**In agent memory, what is a "vector database" used for?**

- A) Storing images
- B) Semantic search over past information
- C) Faster SQL queries
- D) Caching API calls

<details>
<summary>Answer</summary>
B) Semantic search over past information

**Explanation:** Vector databases store embeddings, allowing semantic similarity search to retrieve relevant past memories.
</details>

---

### Question 13
**What problem does "token usage tracking" solve?**

- A) Prevents API rate limits
- B) Monitors costs and optimizes context length
- C) Improves accuracy
- D) Speeds up responses

<details>
<summary>Answer</summary>
B) Monitors costs and optimizes context length

**Explanation:** Tracking tokens helps control costs (tokens = money) and prevents context overflow errors.
</details>

---

### Question 14
**In multi-agent systems, what is "delegation"?**

- A) Deleting agents
- B) One agent assigning tasks to other agents
- C) Error handling
- D) Parallel execution

<details>
<summary>Answer</summary>
B) One agent assigning tasks to other agents

**Explanation:** Delegation allows a coordinator agent to distribute work to specialized agents based on their capabilities.
</details>

---

### Question 15
**What's a key limitation of current AI agents?**

- A) They're too expensive
- B) They can hallucinate and make mistakes
- C) They're too slow
- D) They require too much code

<details>
<summary>Answer</summary>
B) They can hallucinate and make mistakes

**Explanation:** LLMs can generate incorrect information confidently. Agents need validation, error handling, and human oversight for critical tasks.
</details>

---

## Scoring Guide

### Basic Questions (1-10)
- **0-5 correct:** Review the notebooks - some concepts need reinforcement
- **6-7 correct:** Good understanding - practice with challenges
- **8-9 correct:** Strong grasp of concepts - ready for production
- **10 correct:** Excellent! You've mastered the fundamentals

### Advanced Questions (11-15)
- **0-2 correct:** Focus on advanced notebooks and frameworks
- **3-4 correct:** Solid advanced knowledge - keep practicing
- **5 correct:** Expert level - ready to build complex agents!

---

## Compare Your Growth

**Pre-Quiz Score:** _____ / 10

**Post-Quiz Score:** _____ / 15

**Improvement:** Look at questions you got wrong initially - did you get them right this time?

---

## Next Steps

Based on your score:

**If you scored 8+/10 on basics:**
- ✅ Complete the assignment (build your own agent)
- ✅ Try advanced challenges (multi-agent, memory)
- ✅ Explore LangChain/LangGraph in depth
- ✅ Build a production agent for a real use case

**If you scored 5-7/10:**
- 📚 Review notebooks 2-4 (function calling, ReAct, frameworks)
- 🛠️ Complete challenges 1-4
- 💪 Practice with more examples
- 🔄 Retake quiz in a few days

**If you scored below 5/10:**
- 🔄 Re-read notebooks from the beginning
- ✏️ Type out all code examples (don't just read)
- 🤔 Ask questions in Discord/forums
- 📝 Take notes on key concepts
- 🎯 Focus on notebooks 1-3 first

---

## Key Concepts to Master

Make sure you understand:
- [ ] Difference between chatbots and agents
- [ ] How function calling works
- [ ] Tool schema design (name, description, parameters)
- [ ] Input validation strategies
- [ ] ReAct pattern (Thought → Action → Observation)
- [ ] Error handling and self-correction
- [ ] Agent memory (short-term vs long-term)
- [ ] Multi-agent coordination
- [ ] Using LangChain for agents
- [ ] Production considerations (logging, rate limiting, caching)

---

## Feedback

Which topics were:
- **Clearest?** _______________
- **Most confusing?** _______________
- **Most useful?** _______________
- **Want to learn more about?** _______________

---

**Congratulations on completing the AI Agents phase! 🎉**

You now have the skills to build intelligent, autonomous agents that can solve complex, multi-step problems. Time to build something amazing! 🚀
