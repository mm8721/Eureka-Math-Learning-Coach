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
---

# Regression Test 001: Adding Fractions With Like Denominators

## Purpose

Repeat Test Case 001 after strengthening the mathematical completion criteria in the system prompt.

The goals of this regression test were to determine whether:

1. the coach would preserve the successful diagnostic behavior from the original test
2. the coach would no longer describe `4/6` as a complete correct answer before checking simplest form
3. the prompt revision introduced any new instructional issues

---

## Regression Test Sequence

### Student

`3/6 + 1/6 = 4/12`

### Coach

> I see you added 3 and 1 to get 4. Can you tell me how you decided on 12 for the denominator?

### Evaluation

**PASS**

The coach preserved the diagnostic behavior from the original test.

It:

- identified observable evidence from the student's work
- used the mathematically precise term "denominator"
- did not assume why the student produced `12`
- did not provide the correct answer
- asked one diagnostic question

The revised completion criteria did not cause the coach to jump ahead to simplifying the fraction before addressing the student's immediate reasoning.

---

### Student

> I multiplied 6 x 2 because there are two fractions.

### Coach

> Ah, I see—you multiplied by 2 because there are two fractions in the problem.
>
> When we add `3/6` and `1/6`, what do the sixths tell us about the size of the pieces we are putting together?

### Evaluation

**PASS**

The coach used the student's explanation as evidence and shifted from the procedure to the meaning of the fractional units.

The conversational phrase "Ah, I see" is unnecessary but does not interfere with the instructional purpose.

---

### Student

> It tells us there are 6 pieces.

### Coach

> You mentioned there are 6 pieces. If you have `3/6` of something and add `1/6` more of the exact same size, do the pieces change in size when you put them together?

### Evaluation

**PASS WITH NOTE**

The coach continued focusing on the meaning of the denominator and did not provide the computational answer.

However, the phrase "of the exact same size" supplied part of the conceptual understanding that the student could have been asked to generate independently.

Because the selected support level was "Keep trying," this may represent slightly more support than necessary.

No prompt change was made based on this single instance. Future tests should determine whether this becomes a pattern.

---

### Student

> No, they stay the same size.

### Coach

> You're right, the size of the pieces stays the same.
>
> If the pieces stay as sixths, what should the denominator of your answer be?

### Evaluation

**PASS**

The coach connected the conceptual understanding of sixths as equal-sized fractional units to the symbolic role of the denominator.

It returned responsibility for determining the denominator to the student.

---

### Student

> 6

### Coach

> The denominator is 6.
>
> Now, putting the numerator and denominator together, what is your complete answer for `3/6 + 1/6`?

### Student

> 4/6

### Coach

> You found that the sum is `4/6` by keeping the denominator the same and adding the numerators.
>
> Can `4/6` be written in an even simpler form using a smaller denominator?

### Evaluation

**PASS — ORIGINAL FAILURE FIXED**

The system-prompt revision successfully changed the coach's behavior.

During the original test, the coach described `4/6` as "the correct answer" without checking simplest form.

During the regression test, the coach recognized the student's successful fraction-addition reasoning while continuing to check whether the answer met the simplest-form requirement.

This demonstrates that the revised completion criteria affected the intended behavior without disrupting the earlier diagnostic sequence.

### New Language Issue Identified

The phrase:

> "using a smaller denominator"

is not the preferred mathematical description of simplifying a fraction.

A numerically smaller denominator represents larger fractional units, so framing simplification primarily as finding a "smaller denominator" could create or reinforce an imprecise mathematical association.

Preferred language should focus on concepts such as:

- equivalent fractions
- simplest form
- common factors
- dividing the numerator and denominator by the same factor

Future iterations should favor precise mathematical vocabulary rather than using denominator size as the definition of simplification.

---

### Student

> 2/3

### Coach

> You wrote `2/3`. How did you decide that `4/6` simplifies to `2/3`?

### Evaluation

**PASS**

The coach did not assume that producing the expected answer demonstrated understanding.

It requested evidence of the student's equivalent-fraction reasoning.

---

### Student

> I divided the top and bottom by 2.

### Coach

> You divided both the numerator and the denominator by 2.
>
> When you divide both numbers by the same amount, why does the value of the fraction stay the same?

### Evaluation

**NEEDS REVISION — STOPPING CRITERIA**

The coach's question is mathematically meaningful, but the student had already demonstrated substantial evidence related to the original task:

- recognized the denominator should remain `6`
- connected the denominator to the size of the fractional units
- correctly added the fractions to produce `4/6`
- recognized that `4/6` could be simplified
- produced `2/3`
- explained that the numerator and denominator were both divided by `2`

At this point, the coach continued probing into the conceptual theory of equivalent fractions.

Whether this additional question is appropriate should depend on the learning objective.

If the learning objective is to add fractions with like denominators and express the result in simplest form, the student may already have demonstrated sufficient understanding.

If the learning objective is to explain why dividing the numerator and denominator by the same factor produces an equivalent fraction, the additional question would be appropriate.

This reveals a need for stronger learning-objective alignment and stopping criteria.

---

## Regression Test 001 Findings

### Fix Verified: Mathematical Completion Criteria

The system-prompt revision successfully prevented the coach from prematurely declaring `4/6` the completed answer.

**Status: FIX VERIFIED**

---

### New Issue: Mathematical Language

The coach used "smaller denominator" when prompting the student to simplify `4/6`.

This is understandable language but is not mathematically precise enough for the intended design of the learning coach.

**Status: MONITOR AND IMPROVE**

---

### New Issue: Stopping Criteria

The coach continued asking increasingly conceptual questions after the student had likely demonstrated sufficient understanding for the original task.

The coach needs to determine when enough evidence has been collected to satisfy the specific learning objective.

A strong learning coach should not continue questioning simply because another mathematically meaningful question can be asked.

**Status: NEEDS REVISION**

---

## Design Insight From Regression Test 001

The amount and type of questioning should be determined by the learning objective.

The coach should continually ask:

**What evidence is necessary to determine whether this student has met the intended learning objective?**

Once sufficient evidence has been demonstrated:

- acknowledge the specific understanding the student demonstrated
- confirm completion when appropriate
- avoid unnecessary additional diagnostic questioning
- offer further challenge or exploration only when it serves the learning objective or the student requests it

This suggests that future versions of the coach should connect each problem to explicit success criteria rather than relying only on general mathematical coaching behavior.

---

## Iteration 3 Priorities

Based on Regression Test 001, the next system iteration should address:

1. **Learning-objective alignment**
   - Determine what mathematical understanding the current problem is intended to assess or develop.

2. **Stopping criteria**
   - Recognize when the student has provided sufficient evidence of the target understanding.
   - Do not continue diagnostic questioning after the learning objective has been demonstrated unless additional evidence is necessary.

3. **Precise simplification language**
   - Describe simplest form using equivalent fractions and common factors rather than primarily referring to a "smaller denominator."

4. **Preserve successful behavior**
   - Continue diagnosing before assuming.
   - Continue asking one useful question at a time.
   - Continue using evidence from student thinking.
   - Continue preserving productive struggle.
   - Continue distinguishing conceptual progress from mathematical completion.
