from study_data import study_data

print("================================")
print("       AI STUDY ASSISTANT")
print("================================")

while True:

    print("\n📚 Choose a topic:")

    topics = list(study_data.keys())

    for i, topic in enumerate(topics, start=1):
        print(f"{i}. {topic.title()}")

    print(f"{len(topics) + 1}. Exit")

    choice = input("\nEnter your choice: ").strip()

    if not choice.isdigit():
        print("\n❌ Please enter a number.")
        continue

    choice = int(choice)

    if choice == len(topics) + 1:
        print("\nThanks for studying! Keep learning! 🚀")
        break

    if choice < 1 or choice > len(topics):
        print("\n❌ Invalid choice.")
        continue

    topic = topics[choice - 1]
    data = study_data[topic]

    while True:

        print(f"\n📚 Topic: {topic.title()}")

        print("\nWhat would you like to do?")
        print("1. Get a simple explanation")
        print("2. Get key points")
        print("3. Generate questions")
        print("4. Quiz Mode")
        print("5. Choose another topic")

        option = input("\nEnter your choice: ").strip()

        if option == "1":
            print("\n📖 Explanation:")
            print(data["explanation"])

        elif option == "2":
            print("\n📝 Key Points:")

            for point in data["key_points"]:
                print("•", point)

        elif option == "3":
            print("\n❓ Questions:")

            for item in data["questions"]:
                print("•", item["question"])

        elif option == "4":
            print("\n🎯 QUIZ MODE")

            score = 0

            for item in data["questions"]:
                print("\nQuestion:")
                print(item["question"])

                answer = input("Your answer: ").lower().strip()

                if item["answer"] in answer:
                    print("✅ Correct!")
                    score += 1
                else:
                    print("❌ Not quite.")
                    print("Correct answer:", item["answer"])

            print("\n====================")
            print("Quiz Complete!")
            print(f"Your score: {score}/{len(data['questions'])}")
            print("====================")

        elif option == "5":
            break

        else:
            print("\n❌ Invalid choice. Please enter 1-5.")