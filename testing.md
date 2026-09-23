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
---

# Test Case 002: Decimal Addition and Place Value

## Purpose

Test whether the coach's diagnostic behaviors generalize beyond fractions to a different mathematical domain.

This test examines whether the coach can:

1. diagnose an incorrect decimal-addition response before assuming the cause
2. distinguish observed student thinking from inference
3. update its diagnosis when the student provides new evidence
4. connect decimal addition to place-value understanding
5. prioritize mathematical concepts over memorized procedural rules

---

## Initial Problem

### Student

`3.6 + 0.45 = 3.105`

**Selected support level:**

Keep trying

### Coach

> Can you walk me through how you set up this addition problem and got `3.105`?

### Evaluation

**PASS**

The coach did not assume why the student produced the incorrect answer.

Possible causes could have included:

- misunderstanding decimal place value
- treating decimal digits as whole numbers
- incorrect alignment
- a calculation error
- another strategy not yet visible from the student's answer

Instead of selecting a misconception without evidence, the coach asked the student to explain their reasoning.

This suggests that the "diagnose before assuming" behavior from Test Case 001 generalized to a new mathematical context.

---

## Diagnostic Sequence

### Student

> I added 6 + 45 and got 105, so I put 105 after the decimal.

### Coach

> When you lined up 3.6 and 0.45 to add them, how did you line up the decimal points?

### Evaluation

**PASS WITH NOTE**

The coach appropriately continued investigating the student's strategy rather than immediately correcting the answer.

However, it introduced an unsupported assumption by asking:

> "When you lined up..."

The student had not stated that they lined up the numbers.

The student's actual explanation was that they added `6 + 45` and placed `105` after the decimal.

This conflicts with the design principle that the coach should distinguish:

- what the student actually said or did
- what the evidence suggests
- what remains unknown

A stronger question would avoid inserting an unobserved step into the student's reasoning.

---

### Student

> I didn't line them up. I just added 6 + 45.

### Coach

> When you look at 3.6 and 0.45, what place value is the 6 in, and what place value is the 4 in?

### Evaluation

**PASS**

The coach successfully updated its approach after the student corrected its assumption.

Rather than continuing to focus immediately on decimal alignment, it investigated the student's understanding of place value.

This is evidence that the coach can revise its diagnostic path when new student information contradicts an earlier inference.

---

### Student

> The 6 is in the tenths place and the 4 is in the tenths place.

### Coach

> You noticed that both the 6 and the 4 are in the tenths place.
>
> Since they are in the same place value, what does that tell us about how 3.6 and 0.45 should be lined up before you add them?

### Evaluation

**PASS WITH NOTE**

The coach accurately acknowledged an understanding the student had demonstrated: both digits represent tenths.

It then attempted to connect that understanding to the setup of the addition problem.

However, the response began shifting toward decimal alignment as the procedural focus.

The desired mathematical principle is not simply that decimal points should align.

The underlying principle is that quantities with corresponding place values should be aligned:

- ones with ones
- tenths with tenths
- hundredths with hundredths

Correct alignment of the decimal points is a consequence of aligning corresponding place values.

---

### Student

> The decimal points should line up.

### Coach

> Now that we know the decimal points need to line up, how would you set up `3.6 + 0.45` to add them?

### Evaluation

**NEEDS REVISION**

The coach accepted "line up the decimal points" as the primary mathematical rule.

While this procedure can produce the correct setup, it does not capture the underlying place-value reasoning the learning coach is intended to emphasize.

The coach should help the student understand that decimal addition requires quantities representing the same place value to be combined.

A stronger instructional approach would emphasize aligning ones with ones, tenths with tenths, and hundredths with hundredths.

The decimal points then align because the place values are correctly aligned.

---

### Student

> I would put the decimal points on top of each other.

### Coach

> How would `3.6` and `0.45` look if you stacked them with their decimal points lined up?

### Evaluation

**NEEDS REVISION**

The coach again reinforced decimal-point alignment as the central procedure.

Because this framing occurred across multiple responses, it appears to be a pattern rather than an isolated wording choice.

The coach continued preserving productive struggle by asking the student to construct the setup independently, but the conceptual focus was not aligned with the intended instructional approach.

The test was stopped at this point because sufficient evidence had been collected to identify the instructional-design issue.

---

## Test Case 002 Findings

### Successful Behavior: Diagnose Before Assuming

The coach initially requested evidence about the student's strategy rather than assuming the source of the incorrect answer.

**Status: PASS**

---

### Successful Behavior: Updating the Diagnostic Path

When the student explained that they had not lined up the numbers, the coach moved away from its earlier assumption and investigated place-value understanding.

**Status: PASS**

---

### Issue: Unsupported Assumptions About Student Process

The coach briefly described a step the student had not reported taking:

> "When you lined up..."

Future testing should continue examining whether the coach consistently separates observed evidence from inference.

**Status: MONITOR**

---

### Issue: Procedure Replaced the Underlying Concept

The coach repeatedly emphasized:

> "line up the decimal points"

rather than treating place-value alignment as the mathematical principle underlying decimal addition.

This creates a risk that the coach teaches a memorized procedure without sufficiently connecting it to the mathematical structure that explains why the procedure works.

**Status: NEEDS REVISION**

---

## Instructional Design Principle Identified

When teaching or reinforcing a mathematical procedure, prioritize the mathematical concept that explains why the procedure works.

Do not substitute a procedural shortcut or memorized rule for conceptual understanding.

### Decimal Example

For decimal operations, emphasize aligning corresponding place values:

- ones with ones
- tenths with tenths
- hundredths with hundredths

Decimal points align as a consequence of correct place-value alignment.

"Line up the decimal points" should not be presented as the underlying mathematical reason for the procedure.

---

## Design Insight From Test Case 002

A student may know a procedural rule without understanding the mathematical structure behind it.

The learning coach should therefore distinguish between:

**Knowing what to do**

and

**Understanding why the procedure works**

When the learning objective requires conceptual understanding, the coach should use student reasoning to connect procedures to the mathematical concepts that justify them.

This principle should generalize beyond decimal addition to other mathematical procedures.

Examples may include:

- regrouping in multi-digit computation
- fraction algorithms
- multiplication and division algorithms
- equivalent fractions
- operations with decimals
- measurement conversions

---

## Iteration 4 Priority

Based on Test Case 002, the next system-prompt iteration should strengthen the relationship between conceptual understanding and mathematical procedures.

The coach should:

1. identify the mathematical concept underlying a procedure
2. prioritize that concept when diagnosing or teaching
3. avoid presenting memorized rules as explanations
4. connect procedures explicitly to the mathematical structure that makes them valid
5. continue preserving productive struggle rather than simply explaining the procedure

For decimal operations specifically, place-value alignment should be treated as the underlying mathematical principle. Decimal-point alignment is a consequence of that structure, not the conceptual reason for the procedure.

The iteration should preserve the successful behaviors already demonstrated in Tests 001 and 002.
---

## Test Case 003 — Multi-Digit Subtraction and Regrouping

### Purpose
Test whether the Concept Before Procedure principle generalizes to multi-digit subtraction and regrouping without explicitly teaching the coach how to handle this specific problem.

### Problem
402 − 187 = 385

### Support Level
Keep trying

### Student Reasoning and Coach Behavior

The student initially gave the incorrect answer:

402 − 187 = 385

The coach asked the student to explain how they got the answer rather than immediately assuming the source of the error.

The student explained:

> "I did 7 − 2 = 5, 8 − 0 = 8, and 4 − 1 = 3."

The coach recognized the student's approach and focused attention on the ones place rather than immediately providing the regrouping procedure.

When the student suggested:

> "Borrow from the tens place."

the coach noticed that the tens digit in 402 is 0 and asked the student to consider where they could look next.

The student identified the hundreds place. The coach then guided the student toward considering the relationship between the hundreds and tens places.

### What Worked

**PASS — Diagnosed before assuming**

The coach did not infer the misconception from the incorrect answer alone. It first asked the student to explain their reasoning.

**PASS — Responded to evidence**

Once the student revealed that they were subtracting the smaller digit from the larger digit in each place, the coach adjusted its questioning based on that evidence.

**PASS — Preserved productive struggle**

The coach did not immediately provide the standard regrouping algorithm. It continued asking questions that allowed the student to determine what to do next.

**PASS WITH NOTE — Concept before procedure generalized**

The coach moved toward place-value reasoning instead of immediately giving procedural steps. This suggests that the Concept Before Procedure instruction generalized beyond the decimal example used when the rule was developed.

However, the coach continued to use procedural language such as "borrow" and "move" rather than consistently describing regrouping through equivalent place-value units.

### Language to Improve

The coach used phrases such as:

> "borrow from the tens place"

and

> "move that 1 hundred over to the tens place"

These phrases can support a familiar procedure, but they do not precisely describe the mathematics occurring during regrouping.

The underlying mathematical idea is that a quantity can be represented using different but equivalent combinations of place-value units.

### Important Instructional Design Insight — Preserve Valid Student Strategies

Concept before procedure should not mean that the AI imposes one preferred conceptual strategy.

Students may use different mathematically valid place-value representations when regrouping.

For example, a student might think about 402 as:

- 4 hundreds, 0 tens, and 2 ones
- 40 tens and 2 ones
- 3 hundreds, 10 tens, and 2 ones
- 39 tens and 12 ones

The coach should recognize and work with a mathematically valid student strategy when possible rather than redirecting the student toward one prescribed decomposition pathway.

The goal is not to require a particular representation. The goal is to determine whether the student understands the place-value relationships that make their regrouping strategy valid.

### Design Principle Identified

**Concept before procedure does not mean the AI's concept before the student's strategy.**

The coach should:

- seek evidence of the student's reasoning
- preserve mathematically valid strategies
- connect procedures to underlying mathematical structure
- use precise place-value language
- avoid unnecessarily replacing a student's valid strategy with the coach's preferred method

### Iteration 5 Consideration

Do not immediately add another isolated rule to the system prompt.

First review the complete system prompt to determine whether the growing set of instructional principles should be reorganized or consolidated.

Potential areas to examine include:

- conceptual understanding versus procedural knowledge
- mathematical language and precision
- preservation of student strategy
- diagnostic questioning
- stopping criteria
- overlap between existing instructions

### Regression Test After Iteration 5

The fraction-addition test was repeated after refactoring the system prompt into a coaching decision framework.

#### Behaviors Preserved or Improved

**PASS — Diagnose before assuming**

For `3/6 + 1/6 = 4/12`, the coach identified that the student added the numerators and asked how the student determined the denominator rather than assuming the source of the error.

**PASS — Concept before procedure**

After the student explained that they multiplied `6 × 2` because there were two fractions, the coach asked about the meaning of the denominator rather than stating a rule such as "keep the denominator the same."

**PASS — Vocabulary scaffolding**

The coach used mathematical vocabulary with accessible parenthetical support, such as:

> "denominators (the bottom numbers)"

This is a desirable behavior to preserve. Mathematical vocabulary should not be replaced by informal vocabulary when brief scaffolding can make the formal term accessible.

**PASS — Previous completion fix preserved**

When the student reached `4/6`, the coach did not immediately describe the answer as final or complete.

#### Issues Identified

**NEEDS REVISION — Unnecessary reflection and cognitive load**

After the student reached `4/6`, the coach asked:

> "How does that compare to your very first answer of `4/12`?"

The student had already corrected the original denominator reasoning. Returning attention to the abandoned answer did not advance the current learning need and created unnecessary cognitive work.

Reflection should serve a clear instructional purpose rather than occur simply because another mathematical question can be asked.

**NEEDS REVISION — Over-questioning demonstrated understanding**

After the student identified that the denominator changed from 12 to 6, the coach asked another question about why the denominator remains 6.

At this point, sufficient evidence was developing that the original misconception had been resolved. The remaining relevant precision issue was determining whether `4/6` was in simplest form.

Every question should earn its place by doing at least one of the following:

- gathering missing diagnostic evidence
- advancing the student toward the learning objective
- resolving an actual mathematical or precision issue
- providing support the student currently needs

If a question does none of these, the coach should not ask it.

**NEEDS REFINEMENT — Fractional-unit reasoning**

The coach frequently described fractions using "pieces." More precise reasoning would identify the denominator as defining the fractional unit.

For example:

`3/6` represents 3 sixths.

`1/6` represents 1 sixth.

Therefore, 3 sixths + 1 sixth = 4 sixths.

The coach should help students understand fraction operations through fractional units rather than relying primarily on procedural rules about numerators and denominators.

#### Precision Check Design Insight

When simplest form is relevant, the coach should ask the student to determine whether a fraction is in simplest form regardless of whether further simplification is possible.

For example:

- `4/6` → student determines that it can be simplified.
- `5/6` → student determines that it cannot be simplified and can justify that 5 and 6 have no common factor greater than 1.

The coach should not ask about simplification only when simplification is possible. Otherwise, the question itself becomes a hint.

When additional evidence is needed, the coach may ask the student to justify the determination using common factors.

#### Broader Design Principle

**A diagnostic or precision-check question should not unintentionally disclose its answer.**

The presence or absence of a coach question should not become a predictable signal that something is wrong or that a particular action is required.
