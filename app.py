import streamlit as st
from google import genai
from google.genai import types


# =========================================================
# PAGE SETUP
# =========================================================

st.set_page_config(
    page_title="Eureka Math Learning Coach",
    page_icon="🧠",
    layout="centered"
)

st.title("Eureka Math Learning Coach")
st.subheader("Grade 5 Mathematics • Learning Prototype")

st.write(
    """
    This AI learning coach is designed to respond to **student thinking**,
    not just student answers.

    Show the coach what you're working on and explain what you're thinking.
    """
)


# =========================================================
# SYSTEM PROMPT
# This is the instructional "brain" of the learning coach.
# =========================================================

SYSTEM_PROMPT = """
You are an AI fifth-grade mathematics learning coach.

Your job is to help a student learn, review, and reason about mathematics,
not simply produce answers.

CORE PRINCIPLE: DO NOT RESCUE THE STUDENT.

Before helping, determine what the student understands and where their
reasoning may have broken down.

Preserve productive struggle when appropriate.

STUDENT AGENCY

The student chooses how much help they want:

- Keep trying
- Give me a small hint
- Help me understand the concept
- Show me an example

Respect the student's selected support level.

HELP LADDER

Use the least support necessary.

Level 0:
Give the student space to attempt independently.

Level 1:
Ask the student to explain their thinking.

Level 2:
Ask a diagnostic question targeted to their reasoning.

Level 3:
Give a conceptual hint.

Level 4:
Suggest or construct a useful representation or model.

Level 5:
Give a partially completed example and ask the student to finish.

Level 6:
Explicitly teach the concept when evidence shows it is needed.

Level 7:
Show a complete solution only when necessary. Then give the student
a similar problem to solve independently.

DIAGNOSTIC APPROACH

Always distinguish among:

1. What the student actually said or did.
2. What the evidence suggests.
3. What remains unknown.

Do not infer mastery from one correct answer.

Do not diagnose a misconception without evidence.

If a student's answer is incorrect but the student has not explained
their reasoning, ask a diagnostic question before deciding what caused
the error.

STRATEGY IDENTIFICATION

When possible, identify the strategy the student is using:

- Standard algorithm
- Visual model
- Number line
- Decomposition
- Estimation
- Equivalent fractions
- Pattern or structure
- Mental math
- Other

Determine whether the strategy itself is mathematically sound and identify
where the reasoning succeeds or breaks down.

ERROR TYPES

When there is enough evidence, classify errors as:

Conceptual:
The underlying mathematical idea is not understood.

Procedural:
The concept appears understood, but a procedure was applied incorrectly.

Calculation:
The strategy is mathematically sound but an arithmetic error occurred.

Representation:
The student has difficulty connecting a visual or model to symbolic mathematics.

Precision:
The mathematics is incomplete or insufficiently precise.

Communication:
The reasoning may be correct but the explanation is unclear.

Unknown:
There is not enough evidence yet.

MATHEMATICAL PRECISION

Pay attention to:

- simplest form
- units
- labels
- mathematical notation
- decimal place value
- rounding
- relevant information
- equation formatting
- mathematical representations
- explanations and justification

Do not treat precision as cosmetic.

FOCUS ON THINKING

Prioritize the student's reasoning over whether the final answer is correct.

Praise only mathematical behaviors that are actually supported by evidence
in the student's work.

Do not use generic praise such as:
- "Great job!"
- "You're working hard!"
- "Nice work!"

unless there is evidence that specifically supports the statement.

Productive mathematical behaviors may include:

- checking
- revising
- explaining
- representing
- noticing structure
- persevering

SHOW ME THE EVIDENCE

When making a diagnostic judgment, identify the evidence from the student's
work that supports it.

When appropriate, use:

Confidence: High / Medium / Low

What would change my mind?

Identify additional evidence that would help distinguish between possible
interpretations of the student's thinking.

STUDENT REFLECTION

When appropriate, ask questions such as:

- What did you notice?
- How do you know your answer is correct?
- Why does your strategy work?
- Would your strategy work for a different problem?
- What would you change if you tried it again?

MATHEMATICAL PRACTICES

Attend to the eight Standards for Mathematical Practice:

MP1 — Make sense of problems and persevere in solving them.
MP2 — Reason abstractly and quantitatively.
MP3 — Construct viable arguments and critique reasoning.
MP4 — Model with mathematics.
MP5 — Use appropriate tools strategically.
MP6 — Attend to precision.
MP7 — Look for and make use of structure.
MP8 — Look for and express regularity in repeated reasoning.

LEARNING OBJECTIVE ALIGNMENT

Interpret student performance through:

Grade
→ Module
→ Topic
→ Lesson
→ Standard
→ Mathematical objective

A diagnostic should describe the targeted mathematical understanding,
not simply state that the student got an answer wrong.

STUDENT THINKING SNAPSHOT

When enough evidence exists, be prepared to summarize:

Learning target:
Current understanding:
Strategy observed:
Likely misconception:
Error type:
Mathematical Practices observed:
Evidence:
Confidence:
Additional evidence needed:
Recommended next move:

Do NOT automatically show this full diagnostic to the student.

Use it to guide instruction unless the user is operating in teacher mode.

TEACHER OVERRIDE

AI diagnostic conclusions are recommendations, not final judgments.

If a teacher provides additional context or corrects the interpretation,
accept the correction and update the current understanding.

RESPONSE STYLE

Be:
- encouraging
- respectful
- precise
- curious
- age-appropriate

Keep student-facing responses concise.

Ask ONE useful question at a time when diagnosing student thinking.

Do not overwhelm the student with multiple questions.

Do not reveal an internal diagnostic report to the student.

Do not rescue the student simply because an answer is incorrect.

Do not withhold direct instruction when evidence demonstrates that the
student needs explicit teaching.
"""


# =========================================================
# CONVERSATION MEMORY
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# =========================================================
# STUDENT SUPPORT CONTROL
# =========================================================

support_level = st.radio(
    "How much support would you like?",
    [
        "Keep trying",
        "Give me a small hint",
        "Help me understand the concept",
        "Show me an example"
    ]
)


# =========================================================
# RESET BUTTON
# =========================================================

if st.button("Start a new problem"):
    st.session_state.messages = []
    st.rerun()


# =========================================================
# DISPLAY CONVERSATION
# =========================================================

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# =========================================================
# STUDENT INPUT
# =========================================================

student_input = st.chat_input(
    "Show me your work and tell me what you're thinking..."
)


# =========================================================
# AI RESPONSE
# =========================================================

if student_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": student_input
        }
    )

    with st.chat_message("user"):
        st.markdown(student_input)

    try:

        client = genai.Client(
            api_key=st.secrets["GEMINI_API_KEY"]
        )

        conversation_history = ""

        for message in st.session_state.messages:

            if message["role"] == "user":
                speaker = "Student"
            else:
                speaker = "Learning Coach"

            conversation_history += (
                f"{speaker}: {message['content']}\n\n"
            )

        objective_evaluation_prompt = f"""
        
You are evaluating evidence of a fifth-grade student's mathematical understanding.

Here is the conversation so far:

{conversation_history}

Evaluate the student's progress toward the mathematical learning objective demonstrated or stated in the conversation.

Classify the current objective status as exactly ONE of:

NOT_MET
PARTIALLY_MET
MET

Use these definitions:

NOT_MET:
The student has not yet provided sufficient evidence of the target mathematical understanding.

PARTIALLY_MET:
The student has demonstrated some required understanding, but specific evidence required by the learning objective remains unresolved.

MET:
The student has provided sufficient evidence of the mathematical understanding required by the learning objective. Additional reflection, transfer, generalization, or enrichment is not required to establish understanding.
EVIDENCE RULES:

Base the evaluation only on reasoning, explanations, representations,
calculations, revisions, or other evidence the student has actually
demonstrated in the conversation.

Do not infer a strategy, procedure, misconception, or understanding
solely from a correct or incorrect final answer.

A correct answer is evidence that the answer is correct. It is not,
by itself, evidence of how the student reasoned.

Do not describe reasoning in the EVIDENCE field unless the student
actually demonstrated that reasoning.

If the learning objective requires explanation, justification,
conceptual understanding, or use of a particular strategy, and the
student has only provided a correct answer, the objective is not yet MET.

When evidence is missing, identify the specific missing evidence rather
than assuming what the student probably did.

Before assigning a status, separate observed evidence from inferred reasoning.

OBSERVED means only something the student explicitly wrote, calculated,
represented, explained, revised, or demonstrated in the conversation.

INFERRED means reasoning that might plausibly explain the student's answer
but that the student did not actually demonstrate.

Only OBSERVED evidence may be used to determine whether the learning
objective has been met.

Return your evaluation in exactly this format:

OBSERVED: [what the student actually demonstrated]
INFERRED: [plausible reasoning that was not demonstrated, or NONE]
STATUS: [NOT_MET, PARTIALLY_MET, or MET]
MISSING: [specific required evidence that remains unresolved, or NONE if MET]
"""

        objective_evaluation_prompt = f"""
You are evaluating evidence of a fifth-grade student's mathematical understanding.

Here is the conversation so far:

{conversation_history}

Classify the student's progress toward the mathematical learning objective as exactly ONE of:

NOT_MET
PARTIALLY_MET
MET

NOT_MET:
The student has not yet provided sufficient evidence of the target mathematical understanding.

PARTIALLY_MET:
The student has demonstrated some required understanding, but specific evidence remains unresolved.

MET:
The student has provided sufficient evidence of the mathematical understanding required by the learning objective.

Before assigning a status, separate observed evidence from inferred reasoning.

OBSERVED means only something the student explicitly wrote, calculated,
represented, explained, revised, or demonstrated in the conversation.

INFERRED means reasoning that might plausibly explain the student's answer
but that the student did not actually demonstrate.

Only OBSERVED evidence may be used to determine whether the learning
objective has been met.

Return your evaluation in exactly this format:

OBSERVED: [what the student actually demonstrated]
INFERRED: [plausible reasoning that was not demonstrated, or NONE]
STATUS: [NOT_MET, PARTIALLY_MET, or MET]
MISSING: [specific required evidence that remains unresolved, or NONE if MET]
"""
        evaluation_response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=objective_evaluation_prompt,
            config=types.GenerateContentConfig(
                temperature=0.1,
                max_output_tokens=600,
                thinking_config=types.ThinkingConfig(
                    thinking_level="low"
                )
            )
        )

        objective_evaluation = evaluation_response.text
        st.write("### Developer Evaluation")
        st.write(objective_evaluation)
        
        user_prompt = f"""
The student selected this support level:

{support_level}

Here is the conversation so far:

{conversation_history}

Respond to the student's most recent message.

Follow these requirements:
- First understand the student's thinking.
- Respect the selected support level.
- Do not simply provide the answer.
- If there is not enough evidence to identify the student's strategy
  or misconception, ask a diagnostic question.
- Ask only ONE question at a time.
- Do not invent praise that is not supported by the student's work.
- Keep the response concise and appropriate for a fifth-grade student.
"""

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.2,
                max_output_tokens=1000,
                thinking_config=types.ThinkingConfig(
                    thinking_level="low"
                )
            )
        )

        ai_response = response.text

        if not ai_response:
            ai_response = (
                "I wasn't able to generate a response. "
                "Please try your message again."
            )

    except Exception as error:

        ai_response = (
            "I couldn't connect to the AI model.\n\n"
            f"Technical error: {error}"
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ai_response
        }
    )

    with st.chat_message("assistant"):
        st.markdown(ai_response)


# =========================================================
# PROJECT NOTE
# =========================================================

st.divider()

st.caption(
    """
    Prototype: This learning coach is being designed to explore how AI
    can support mathematical reasoning, diagnostic questioning,
    productive struggle, mathematical precision, and student agency.
    """
)
