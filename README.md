# Eureka Math Learning Coach

An AI-powered Grade 5 mathematics learning coach designed to respond to student thinking, support productive struggle, and make instructional decisions based on evidence of student understanding.

## Why I Built This

As an elementary mathematics teacher, I spent much of my time trying to understand what students were thinking—not simply whether their answers were right or wrong.

A correct answer does not always demonstrate understanding, and an incorrect answer does not necessarily reveal why a student is struggling. Effective instructional support requires looking at the evidence a student has actually provided, identifying what remains unresolved, and deciding what support will help the student take the next step independently.

I built this prototype to explore how those same instructional decisions could be incorporated into an AI-powered mathematics learning coach.

The project is grounded in Grade 5 mathematics and draws on instructional principles I used in the classroom, including formative assessment, conceptual understanding, mathematical precision, productive struggle, and responsiveness to student strategies.

## Design Goals

The learning coach is designed to:

- diagnose student thinking before assuming a misconception
- distinguish observed student evidence from inferred reasoning
- preserve productive struggle rather than immediately supplying answers
- provide the least amount of support necessary
- ask one purposeful question at a time
- prioritize mathematical concepts before procedures
- reason explicitly with mathematical units
- preserve mathematically valid student strategies
- distinguish conceptual misunderstandings from calculation errors
- use precise but accessible mathematical language
- maintain mathematical precision
- align coaching decisions with the learning objective
- stop questioning once sufficient evidence of understanding has been demonstrated

## How It Works

The prototype is built with:

- Python
- Streamlit
- Gemini API
- GitHub

The current version includes a curriculum-aware evaluation layer.

For the initial implementation, curriculum metadata identifies:

- topic
- standard
- learning objective
- required evidence of understanding

The system then uses the student's conversation to distinguish:

**OBSERVED** — What the student actually wrote, calculated, represented, explained, revised, or demonstrated.

**INFERRED** — Reasoning that might plausibly explain the student's response but that the student has not actually demonstrated.

Student progress toward the objective is classified as:

- `NOT_MET`
- `PARTIALLY_MET`
- `MET`

The evaluator also identifies the specific evidence that is still missing.

That evaluation is passed to the coaching model so the next instructional response can be based on what the student has actually demonstrated rather than simply whether an answer is correct.

## An Important Design Problem

One of the most useful discoveries in this project came from something that was not working.

During early testing, the coach frequently continued asking questions even after a student had demonstrated sufficient understanding.

The additional questions were often mathematically valuable, but they were not instructionally necessary.

I repeatedly strengthened the system prompt with stopping criteria, including the principle:

> A mathematically valuable next question is not automatically a necessary next question.

Testing showed that prompt instructions alone did not reliably solve the problem.

That led to an architectural change.

Instead of asking the coaching model to simultaneously determine what the student understood and decide what to say next, I began separating those decisions:

**Learning Objective**  
↓  
**Required Evidence**  
↓  
**Student Conversation**  
↓  
**Observed Evidence**  
↓  
**Objective Status**  
↓  
**Coaching Decision**

The current prototype uses a separate objective evaluator and passes its evaluation to the coaching model.

Initial testing showed that connecting objective status to the coaching decision improved the coach's ability to stop once sufficient evidence had been demonstrated.

## Testing and Iteration

I have tested the coach using intentionally selected student responses rather than only correct examples.

Testing has included:

- common fraction misconceptions
- correct answers without demonstrated reasoning
- decimal place-value misconceptions
- calculation errors when underlying concepts may be sound
- multi-digit subtraction and regrouping
- mathematically valid nonstandard strategies
- ambiguous student explanations
- mathematical precision requirements
- situations where continued questioning becomes unnecessary

Each test examines not only mathematical accuracy but also the instructional decisions made by the coach.

The complete testing and iteration history is documented in [`testing.md`](testing.md).

## Examples of Design Insights

### Correct Answers Are Not the Same as Evidence of Understanding

A student may provide the correct answer without demonstrating how they reasoned.

The evaluator therefore distinguishes the answer that was actually observed from reasoning the AI might infer.

For example, if a student writes:

`3 ÷ 4 = 3/4`

the correct equation is evidence.

It is not automatically evidence that the student understands how the numerator and denominator relate to division or equal sharing.

### Concept Before Procedure

During decimal-addition testing, the coach initially emphasized the familiar rule:

> Line up the decimal points.

Testing led to a more conceptual approach based on place-value units.

Students should understand that ones align with ones, tenths with tenths, and hundredths with hundredths. Decimal points align as a consequence of correctly aligning corresponding place values.

### Preserve Valid Student Strategies

During subtraction testing, a student represented:

`402 = 40 tens + 2 ones`

rather than beginning with the conventional representation of 4 hundreds, 0 tens, and 2 ones.

Because the representation is mathematically valid, the coach should reason within the student's strategy rather than redirect the student toward the AI's preferred method.

This led to an important design principle:

> Concept before procedure does not mean the AI's concept before the student's strategy.

### Update the Diagnosis as Evidence Changes

Student understanding can change during a conversation.

The coach should not remain anchored to the student's original error after the student has demonstrated new understanding.

Testing therefore examines whether the system distinguishes resolved evidence from what still needs attention.

## Current Curriculum Experiment

The current curriculum-aware implementation begins with Eureka Math Grade 5 Module 4, Lesson 2.

The instructional metadata includes:

- **Topic:** Fractions as Division
- **Standard:** 5.NF.3
- **Objective:** Interpret a fraction as division.
- **Required Evidence:** Evidence used to determine whether the student has sufficiently demonstrated the relationship between a fraction and division.

The prototype currently uses this limited scope intentionally so the evaluation architecture can be tested before expanding curriculum coverage.

## Current Limitations

This is an experimental learning-engineering prototype, not a production-ready educational product.

Current limitations include:

- curriculum-aware evaluation has only been tested with a limited instructional scope
- additional testing is needed across different mathematical objectives and misconceptions
- required-evidence definitions need continued review before curriculum metadata is expanded
- `NOT_MET` behavior requires additional testing
- stopping behavior needs regression testing across objectives beyond fractions as division
- fraction notation occasionally renders incorrectly in the interface
- AI-generated instructional responses can still be inconsistent and require testing

These limitations are part of the purpose of the project: identifying where general AI behavior is insufficient for instructional use and exploring ways to make that behavior more evidence-based and reliable.

## Next Steps

Potential next iterations include:

- expand and validate curriculum metadata across additional Grade 5 mathematics objectives
- test `NOT_MET`, `PARTIALLY_MET`, and `MET` behavior across a wider range of student responses
- continue regression testing of stopping behavior
- improve mathematical notation rendering
- explore when visual or mathematical representations are more useful than continued verbal questioning
- continue testing how reliably the evaluator separates observed evidence from inferred reasoning

## What I Am Learning

Building this prototype has reinforced that designing an AI learning tool involves more than generating mathematically correct responses.

The harder questions are instructional:

- What does the student actually understand?
- What are we inferring without evidence?
- What evidence does the learning objective require?
- What remains unresolved?
- What is the least amount of support the student needs next?
- When should the AI stop?

The project is an ongoing exploration of how instructional judgment, curriculum design, formative assessment, and AI application development can work together to create more thoughtful learning experiences.
