# Testing & Iteration Log

This document tracks how the Eureka Math Learning Coach is tested and improved.

The goal of testing is not only to determine whether the coach produces mathematically accurate responses, but also whether it responds to student thinking in ways that support reasoning, precision, productive struggle, and student independence.

Each test begins with a student response or misconception and evaluates whether the coach:

- distinguishes observed evidence from inference
- diagnoses before assuming a misconception
- preserves productive struggle
- provides the least amount of support necessary
- asks one useful question at a time
- uses evidence-based feedback rather than generic praise
- maintains mathematical precision
- recognizes when a student's understanding has changed
- avoids declaring work complete before all mathematical expectations have been met

---

## Test Case 001: Adding Fractions With Like Denominators

### Purpose

Test whether the coach can respond to an incorrect fraction addition problem without immediately correcting the student or assuming why the error occurred.

The test also examines whether the coach can use student responses to identify the underlying misconception, provide graduated support, and recognize when the student's conceptual understanding improves.

### Initial Problem

**Student:**

`3/6 + 1/6 = 4/12`

**Selected support level:**

Keep trying

### Initial Coach Response

> You added `3 + 1` to get `4` for the top number. Can you tell me how you got `12` for the bottom number?

### Evaluation

**PASS**

The coach:

- identified an observable part of the student's strategy
- did not assume why the denominator was incorrect
- did not provide the correct answer
- asked one diagnostic question
- kept the cognitive work with the student

---

## Diagnostic Sequence

### Student

> I multiplied `6 × 2` because there are two fractions.

### Coach

> When we look at `3/6` and `1/6`, what does the bottom number, `6`, tell us about the pieces?

### Evaluation

**PASS**

The coach used the student's explanation as evidence of a possible conceptual misunderstanding about the denominator.

Rather than explaining the rule for adding fractions with like denominators, the coach asked a conceptual question about the meaning of the denominator.

---

### Student

> It tells us there are 6 pieces.

### Coach

> If both fractions have `6` as the bottom number, what does that tell us about the size of the pieces you are adding together?

### Evaluation

**PASS**

The student's answer demonstrated partial understanding but lacked mathematical precision.

The coach did not accept the response as complete. Instead, it prompted the student to think about the size of the fractional units.

This preserved productive struggle while moving the student toward the idea of equal-sized parts.

---

### Student

> They are the same size.

### Coach

> You noticed that the pieces are the same size.
>
> If you have 3 sixths and you add 1 sixth, does the size of the pieces change when you put them together?

### Evaluation

**PASS**

The coach:

- acknowledged a mathematical observation supported by evidence
- avoided generic praise
- connected the student's understanding of equal-sized pieces to the addition problem
- continued to leave the mathematical reasoning to the student

The phrase "You noticed that the pieces are the same size" is an example of evidence-based feedback rather than praise based only on correctness.

---

### Student

> No, they stay the same size.

### Coach

> They do stay the same size!
>
> If you have 3 sixths and 1 sixth, what should the bottom number of your answer be?

### Evaluation

**PASS**

The coach appropriately moved from diagnosis toward application.

At this point, the student had provided evidence that they understood that combining sixths does not change the size of the fractional unit.

The coach returned to the original computation without giving the denominator away.

---

### Student

> 6

### Coach

> The bottom number is `6`.
>
> Putting that together with the top number you found earlier, what is your final answer for `3/6 + 1/6`?

### Evaluation

**PASS**

The coach confirmed the student's reasoning and asked the student to reconstruct the answer independently.

---

### Student

> 4/6

### Coach

> You revised your answer from `4/12` to `4/6` after thinking about the size of the pieces.
>
> How do you know that `4/6` is the correct answer for `3/6 + 1/6`?

### Evaluation

**NEEDS REVISION**

The first sentence is strong evidence-based feedback. It accurately describes how the student's thinking changed during the interaction.

However, the coach referred to `4/6` as "the correct answer" before checking whether the fraction should be expressed in simplest form.

The student's original conceptual misunderstanding appears to have been resolved, but the mathematical task is not yet fully complete if simplest form is an expectation.

The coach should distinguish between:

- correct fraction-addition reasoning
- an equivalent value
- a complete final answer that meets the problem's precision requirements

### Preferred Behavior

A stronger response might be:

> Your reasoning shows that you now have 4 sixths. Before we decide whether the problem is finished, can `4/6` be written as an equivalent fraction in simplest form?

This recognizes the student's conceptual progress without prematurely declaring the work complete.

---

## Test Case 001 Findings

### Successful Behaviors

The coach successfully:

- diagnosed before assuming
- used student reasoning as evidence
- avoided immediately supplying the correct procedure
- moved from procedural thinking to conceptual understanding
- maintained productive struggle
- asked one question at a time
- used evidence-based feedback
- responded to changes in student understanding
- returned responsibility for the mathematics to the student

### Issues Identified

**1. Mathematical completion criteria**

The coach needs stronger criteria for determining when an answer is complete.

It should check relevant precision requirements, such as:

- simplest form
- units
- labels
- notation
- place value
- rounding
- equation formatting
- explanation or justification when required

before describing a response as the final or fully correct answer.

**2. Mathematical vocabulary**

The coach frequently used "top number" and "bottom number" rather than "numerator" and "denominator."

This language may be accessible to students, but future testing should examine whether the coach can support accessibility while also modeling precise Grade 5 mathematical vocabulary.

---

## Iteration Resulting From Test 001

The next system-prompt iteration should strengthen the coach's completion criteria.

Before declaring an answer correct or complete, the coach should determine whether:

1. the student's reasoning is mathematically sound
2. the computation is accurate
3. the response meets relevant precision expectations
4. the student has demonstrated the intended learning objective

A student may resolve one type of error while still needing support in another area.

For example:

`4/12` → conceptual issue with denominator

`4/6` → fraction addition concept appears resolved, but simplest-form precision remains

`2/3` → mathematically complete if supported by appropriate reasoning

The coach should update its diagnosis as new evidence becomes available rather than continuing to treat the student according to the original error.

---

## Testing Principle

A successful AI learning coach should not simply determine whether an answer is right or wrong.

It should use evidence from student thinking to determine:

**What does the student understand now, what remains unresolved, and what is the least amount of support needed for the student to take the next mathematical step independently?**
