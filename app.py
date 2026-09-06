from study_data import study_data
from ai import ask_ai
from progress import update_progress, show_progress
from notes_manager import save_notes


print("================================")
print("       AI STUDY ASSISTANT")
print("================================")


while True:

    print("\n📚 Choose a topic:")

    topics = list(study_data.keys())

    for i, topic in enumerate(topics, start=1):
        print(f"{i}. {topic.title()}")

    progress_option = len(topics) + 1
    exit_option = len(topics) + 2

    print(f"{progress_option}. 📊 View Progress")
    print(f"{exit_option}. Exit")

    choice = input("\nEnter your choice: ").strip()


    # =========================
    # VIEW PROGRESS
    # =========================

    if choice == str(progress_option):
        show_progress()
        continue


    # =========================
    # EXIT
    # =========================

    if choice == str(exit_option):
        print("\nThanks for studying! Keep learning! 🚀")
        break


    if not choice.isdigit():
        print("\n❌ Please enter a number.")
        continue


    choice = int(choice)

    if choice < 1 or choice > len(topics):
        print("\n❌ Invalid choice.")
        continue


    topic = topics[choice - 1]


    # =========================
    # TOPIC MENU
    # =========================

    while True:

        print(f"\n📚 Topic: {topic.title()}")

        print("\nWhat would you like to do?")
        print("1. Ask AI")
        print("2. AI Notes Generator")
        print("3. AI Question Generator")
        print("4. Get key points")
        print("5. AI Quiz Mode")
        print("6. Choose another topic")

        option = input("\nEnter your choice: ").strip()


        # =========================
        # ASK AI
        # =========================

        if option == "1":

            question = input(
                "\n🤖 What do you want to know? "
            )

            prompt = f"""
You are a helpful AI study assistant.

The student is studying: {topic}

Explain the answer clearly and simply.
Use beginner-friendly language.
Give examples when useful.

Student's question:
{question}
"""

            print("\n🤖 AI:")
            print(ask_ai(prompt))


        # =========================
        # AI NOTES
        # =========================

        elif option == "2":

            print("\n📝 Generating AI Notes...")

            prompt = f"""
Create short, exam-friendly revision notes
for the topic: {topic}

Include:
- Definition
- Important concepts
- Key points
- A simple example

Use simple language suitable for a college student.
Keep the notes concise and easy to revise.
"""

            notes = ask_ai(prompt)

            print("\n🤖 AI Notes:")
            print(notes)

            save_choice = input(
                "\n💾 Save these notes? (Y/N): "
            ).strip().upper()

            if save_choice == "Y":

                filepath = save_notes(topic, notes)

                print(
                    f"\n✅ Notes saved to: {filepath}"
                )

            else:

                print("\n👍 Notes were not saved.")


        # =========================
        # AI QUESTION GENERATOR
        # =========================

        elif option == "3":

            count = input(
                "\nHow many questions do you want? "
            ).strip()

            if not count.isdigit():

                print("\n❌ Please enter a number.")
                continue

            count = int(count)

            if count < 1 or count > 20:

                print(
                    "\n❌ Please choose between 1 and 20."
                )

                continue

            prompt = f"""
Generate {count} study questions about {topic}.

Make them useful for exam preparation.
Use simple and clear language.
Include a mix of easy and medium difficulty questions.

Do not provide the answers.
Number each question clearly.
"""

            print("\n🤖 AI Questions:")
            print(ask_ai(prompt))


        # =========================
        # KEY POINTS
        # =========================

        elif option == "4":

            print("\n📝 Key Points:")

            for point in study_data[topic]["key_points"]:

                print("•", point)


        # =========================
        # AI QUIZ MODE
        # =========================

        elif option == "5":

            print("\n🎯 AI QUIZ MODE")

            # Difficulty
            print("\nChoose difficulty:")
            print("1. 🟢 Easy")
            print("2. 🟡 Medium")
            print("3. 🔴 Hard")

            difficulty_choice = input(
                "\nEnter difficulty: "
            ).strip()

            difficulties = {
                "1": "easy",
                "2": "medium",
                "3": "hard"
            }

            if difficulty_choice not in difficulties:

                print("\n❌ Invalid difficulty.")
                continue

            difficulty = difficulties[
                difficulty_choice
            ]


            # Number of questions
            count = input(
                "\nHow many questions? "
            ).strip()

            if not count.isdigit():

                print("\n❌ Please enter a number.")
                continue

            count = int(count)

            if count < 1 or count > 10:

                print(
                    "\n❌ Please choose between 1 and 10."
                )

                continue


            print(
                f"\n🤖 Generating {difficulty} "
                f"quiz for {topic.title()}..."
            )


            prompt = f"""
Create exactly {count} multiple-choice questions
about {topic}.

Difficulty level: {difficulty}

For every question use exactly this format:

QUESTION: question text
A) option
B) option
C) option
D) option
ANSWER: A

The ANSWER must contain only the correct letter.

Make the questions appropriate for a college student.

Difficulty rules:

Easy:
Test basic definitions and simple concepts.

Medium:
Test understanding and application.

Hard:
Test deeper understanding, tricky concepts,
and problem-solving.

Do not add explanations.
"""


            quiz_text = ask_ai(prompt)


            # =========================
            # PARSE AI QUESTIONS
            # =========================

            questions = quiz_text.split("QUESTION:")

            quiz_questions = []


            for question in questions:

                if "ANSWER:" not in question:
                    continue

                parts = question.split("ANSWER:")

                question_text = parts[0].strip()
                answer_text = parts[1].strip().upper()

                if not answer_text:
                    continue

                correct_answer = answer_text[0]

                if correct_answer not in [
                    "A", "B", "C", "D"
                ]:
                    continue

                quiz_questions.append({
                    "question": question_text,
                    "answer": correct_answer
                })


            quiz_questions = quiz_questions[:count]


            if not quiz_questions:

                print(
                    "\n❌ Could not create the quiz."
                )

                print("Please try again.")

                continue


            score = 0

            wrong_questions = []


            # =========================
            # MAIN QUIZ
            # =========================

            print("\n==============================")
            print("       🤖 AI QUIZ")
            print("==============================")


            for number, question in enumerate(
                quiz_questions,
                start=1
            ):

                print(
                    f"\nQuestion {number}/"
                    f"{len(quiz_questions)}"
                )

                print(question["question"])


                while True:

                    answer = input(
                        "\nYour answer (A/B/C/D): "
                    ).strip().upper()

                    if answer in [
                        "A", "B", "C", "D"
                    ]:
                        break

                    print(
                        "❌ Please enter "
                        "A, B, C, or D."
                    )


                if answer == question["answer"]:

                    print("✅ Correct!")

                    score += 1

                else:

                    print("❌ Incorrect!")

                    print(
                        f"Correct answer: "
                        f"{question['answer']}"
                    )

                    wrong_questions.append(
                        question
                    )


            # =========================
            # SAVE PROGRESS
            # =========================

            total_questions = len(
                quiz_questions
            )

            percentage = (
                score / total_questions
            ) * 100

            update_progress(
                score,
                total_questions,
                topic
            )


            # =========================
            # RESULTS
            # =========================

            print("\n==============================")
            print("       🎯 QUIZ COMPLETE")
            print("==============================")

            print(
                f"📚 Topic: {topic.title()}"
            )

            print(
                f"🎚️ Difficulty: "
                f"{difficulty.title()}"
            )

            print(
                f"🏆 Score: "
                f"{score}/{total_questions}"
            )

            print(
                f"📈 Percentage: "
                f"{percentage:.0f}%"
            )


            if percentage == 100:

                print("🏆 Perfect score!")

            elif percentage >= 80:

                print("🔥 Excellent work!")

            elif percentage >= 60:

                print("👍 Good job!")

            elif percentage >= 40:

                print(
                    "📚 Keep practicing!"
                )

            else:

                print(
                    "💪 Review the topic "
                    "and try again!"
                )


            # =========================
            # RETRY WRONG QUESTIONS
            # =========================

            if wrong_questions:

                print(
                    f"\n❌ You got "
                    f"{len(wrong_questions)} "
                    f"question(s) wrong."
                )

                print(
                    "\nWould you like to "
                    "retry them?"
                )

                print("1. Yes")
                print("2. No")

                retry = input(
                    "\nEnter your choice: "
                ).strip()


                if retry == "1":

                    print(
                        "\n=============================="
                    )

                    print(
                        "       🔁 RETRY MODE"
                    )

                    print(
                        "=============================="
                    )


                    retry_score = 0


                    for number, question in enumerate(
                        wrong_questions,
                        start=1
                    ):

                        print(
                            f"\nRetry Question "
                            f"{number}/"
                            f"{len(wrong_questions)}"
                        )

                        print(
                            question["question"]
                        )


                        while True:

                            answer = input(
                                "\nYour answer "
                                "(A/B/C/D): "
                            ).strip().upper()

                            if answer in [
                                "A", "B", "C", "D"
                            ]:
                                break

                            print(
                                "❌ Please enter "
                                "A, B, C, or D."
                            )


                        if answer == question["answer"]:

                            print(
                                "✅ Correct this time!"
                            )

                            retry_score += 1

                        else:

                            print(
                                "❌ Still incorrect."
                            )

                            print(
                                f"Correct answer: "
                                f"{question['answer']}"
                            )


                    print(
                        "\n=============================="
                    )

                    print(
                        "       🔁 RETRY COMPLETE"
                    )

                    print(
                        "=============================="
                    )

                    print(
                        f"Retry score: "
                        f"{retry_score}/"
                        f"{len(wrong_questions)}"
                    )


                    if retry_score == len(
                        wrong_questions
                    ):

                        print(
                            "🎉 You fixed all "
                            "your mistakes!"
                        )

                    else:

                        print(
                            "📚 Keep reviewing "
                            "these concepts!"
                        )


        # =========================
        # CHANGE TOPIC
        # =========================

        elif option == "6":

            break


        else:

            print(
                "\n❌ Invalid choice. "
                "Please enter 1-6."
            )