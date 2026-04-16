# Quizzes

## Overview

This directory is the quiz hub for the Zero-to-AI course. It does **not** yet contain quizzes for every phase.

Use this folder as a growing assessment library while the wider quiz system is being built out. Quizzes help learners:

- **Assess prior knowledge** before starting a phase (pre-quiz)
- **Validate learning outcomes** after completing a phase (post-quiz)
- **Identify knowledge gaps** for focused review
- **Track progress** throughout the course

## Quiz Format

Each quiz contains:
- **10 questions** (mix of multiple choice and code-based)
- **Time limit:** 15-20 minutes
- **Passing score:** 70% (7/10 correct)
- **Immediate feedback** with explanations

## Available Quizzes

| Phase | Topic | Pre-Quiz | Post-Quiz |
|-------|-------|----------|-----------|
| 15 | AI Agents | ✅ | ✅ |
| 16 | Model Evaluation | ✅ | ✅ |
| 17 | Debugging & Troubleshooting | ✅ | ✅ |
| 18 | Low-Code AI Tools | ✅ | ✅ |

## Planned Coverage

The long-term goal is phase-level pre- and post-quizzes across the core curriculum, but that work is still in progress. Until then:

- Treat quizzes as bonus mastery checks where available.
- Do not assume that a missing quiz means a phase is incomplete.
- Use assignments, challenges, and notebook exercises as your main self-checks in phases without quizzes.

## How to Use

### For Learners

1. **Before starting a phase:**
   - Take the **pre-quiz** if one exists to assess your baseline knowledge
   - Review your results to identify what to focus on
   - Don't worry if you score low - that's expected!

2. **After completing a phase:**
   - Take the **post-quiz** if one exists to validate your learning
   - Compare pre/post scores to measure progress
   - Review incorrect answers for deeper understanding

3. **During review:**
   - Retake quizzes after revisiting content
   - Aim for 90%+ on post-quizzes before moving forward

### For Maintainers

- Use pre-quiz results to identify weak spots in the curriculum
- Track post-quiz results to see whether explanations and notebooks are landing
- Identify common misconceptions from wrong answers
- Update quiz wording when content or phase ordering changes

## Quiz Platforms

Current quizzes in this folder are Markdown-based. Additional formats may be added later.

### Current Format
- **Markdown Files**
- **Pros:** Self-paced, easy to edit, works offline
- **Access:** This directory (`*.md` files)

## Quiz Guidelines

### Question Types

1. **Multiple Choice (60%)**
   ```
   What is the output of `len([1, 2, 3])`?
   A) 1
   B) 2
   C) 3  ✓
   D) Error
   ```

2. **Code Output (20%)**
   ```python
   x = [1, 2, 3]
   print(x[0] + x[-1])
   # What is printed?
   ```

3. **Conceptual (20%)**
   ```
   Which statement about neural networks is FALSE?
   ```

### Difficulty Levels

- **Pre-Quiz:** Mixed difficulty (30% easy, 50% medium, 20% hard)
- **Post-Quiz:** Slightly harder (20% easy, 50% medium, 30% hard)

### Scoring

- Each question: 1 point
- Total: 10 points
- Passing: 7+ points (70%)
- Excellent: 9+ points (90%)

## Quiz Creation Template

For maintainers creating new quizzes:

```markdown
# Phase X: [Topic] - [Pre/Post] Quiz

**Time:** 15 minutes  
**Questions:** 10  
**Passing Score:** 70%

---

## Question 1 (Easy)

[Question text]

A) [Option A]
B) [Option B]
C) [Option C] ✓
D) [Option D]

<details>
<summary>Explanation</summary>

[Why C is correct and others are wrong]

**Reference:** [Link to relevant content]

</details>

---

[Repeat for questions 2-10]
```

## Analytics & Insights

Track these metrics:

- **Average pre-quiz score:** Baseline knowledge
- **Average post-quiz score:** Learning effectiveness
- **Score improvement:** Delta between pre and post
- **Question difficulty:** % correct per question
- **Common mistakes:** Frequently wrong answers

## Example Results

```
Phase 6: Neural Networks
├── Pre-Quiz Average: 42% (challenging content)
├── Post-Quiz Average: 81% (strong learning)
├── Improvement: +39 points (excellent progress)
└── Hardest Question: #7 (Backpropagation math)
```

## Contributing

To add/improve quizzes:

1. Fork the repository
2. Create quiz following the template
3. Test with 3+ reviewers
4. Submit pull request with:
   - Quiz markdown file
   - Answer key
   - Optional hosted form link if you create one
   - Sample analytics if available

## Best Practices

✅ **DO:**
- Cover key learning objectives
- Mix difficulty levels
- Provide detailed explanations
- Reference course materials
- Include code examples
- Test thoroughly before deploying

❌ **DON'T:**
- Use trick questions
- Test obscure edge cases
- Make questions ambiguous
- Reuse identical questions in pre/post
- Exceed 20-minute time limit

## Resources

- [Creating Effective Quizzes](https://cft.vanderbilt.edu/guides-sub-pages/writing-good-multiple-choice-test-questions/)
- [Bloom's Taxonomy](https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/)
- [Quiz Design Principles](https://www.edutopia.org/article/designing-better-assessments)

---

**Remember:** Quizzes are learning tools, not gatekeepers. Use them to guide improvement, not discourage learners.

## What Comes Next

After using the quizzes in this folder:

- Return to the phase you are currently studying and revisit the exact topics you missed.
- Use assignments, challenges, and notebooks as the main mastery checks when a phase has no quiz yet.
- Follow the [master study guide](../docs/MASTER_STUDY_GUIDE.md) for overall navigation instead of treating this folder as a separate phase.
