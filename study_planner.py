from ai import ask_ai


def create_study_plan(topic, days):

    prompt = f"""
Create a {days}-day study plan for a college student studying:

Topic: {topic}

Requirements:
- Divide the topic across exactly {days} days.
- Start with basic concepts and gradually move to harder concepts.
- Include important concepts suitable for exams.
- Give each day a clear title.
- Include what the student should study each day.
- Keep each day's plan concise.
- Use simple language.
- End with a revision/practice day if appropriate.

Format:

Day 1: Title
- Topic/concept
- Topic/concept

Day 2: Title
- Topic/concept
- Topic/concept

Continue until Day {days}.
"""

    return ask_ai(prompt)


def study_planner():

    print("\n================================")
    print("       📅 AI STUDY PLANNER")
    print("================================")

    topic = input("\n📚 Enter your topic: ").strip()

    if not topic:
        print("\n❌ Topic cannot be empty.")
        return

    days_input = input("📅 How many days do you have? ").strip()

    if not days_input.isdigit():
        print("\n❌ Please enter a valid number of days.")
        return

    days = int(days_input)

    if days < 1:
        print("\n❌ Number of days must be at least 1.")
        return

    print("\n🤖 Creating your study plan...")
    
    plan = create_study_plan(topic, days)

    print("\n📅 YOUR STUDY PLAN")
    print("--------------------------------")
    print(plan)
    print("--------------------------------")