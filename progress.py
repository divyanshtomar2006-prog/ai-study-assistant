from achievements import show_achievements
import json
import os

FILE_NAME = "progress.json"


def load_progress():
    if not os.path.exists(FILE_NAME):
        return {
            "quizzes_completed": 0,
            "total_score": 0,
            "total_questions": 0,
            "best_score": 0,
            "topics": {}
        }

    with open(FILE_NAME, "r") as file:
        progress = json.load(file)

    # Add topics if an older progress.json doesn't have it
    if "topics" not in progress:
        progress["topics"] = {}

    return progress


def save_progress(progress):
    with open(FILE_NAME, "w") as file:
        json.dump(progress, file, indent=4)


def update_progress(score, total_questions, topic):
    progress = load_progress()

    # Overall progress
    progress["quizzes_completed"] += 1
    progress["total_score"] += score
    progress["total_questions"] += total_questions

    percentage = (score / total_questions) * 100

    if percentage > progress["best_score"]:
        progress["best_score"] = percentage

    # Topic progress
    if topic not in progress["topics"]:
        progress["topics"][topic] = {
            "quizzes": 0,
            "score": 0,
            "questions": 0
        }

    topic_data = progress["topics"][topic]

    topic_data["quizzes"] += 1
    topic_data["score"] += score
    topic_data["questions"] += total_questions

    save_progress(progress)


def show_progress():
    progress = load_progress()

    quizzes = progress["quizzes_completed"]
    total_questions = progress["total_questions"]

    # Overall average
    if total_questions > 0:
        average = (
            progress["total_score"]
            / total_questions
            * 100
        )
    else:
        average = 0

    print("\n================================")
    print("       📊 STUDY DASHBOARD")
    print("================================")

    print(f"\n🎯 Total Quizzes : {quizzes}")
    print(f"🏆 Best Score    : {progress['best_score']:.0f}%")

    if total_questions > 0:
        print(f"📈 Average Score : {average:.0f}%")
    else:
        print("📈 Average Score : No quizzes yet")

    # Topic progress
    if progress["topics"]:

        print("\n📚 TOPIC PROGRESS")
        print("--------------------------------")

        strongest_topic = None
        weakest_topic = None
        highest_score = -1
        lowest_score = 101

        for topic, data in progress["topics"].items():

            if data["questions"] > 0:

                topic_percentage = (
                    data["score"]
                    / data["questions"]
                    * 100
                )

                print(
                    f"{topic.title():20} : "
                    f"{topic_percentage:.0f}%"
                )

                if topic_percentage > highest_score:
                    highest_score = topic_percentage
                    strongest_topic = topic

                if topic_percentage < lowest_score:
                    lowest_score = topic_percentage
                    weakest_topic = topic

        if strongest_topic:
            print(
                f"\n🔥 Strongest Topic : "
                f"{strongest_topic.title()}"
            )

        if weakest_topic:
            print(
                f"📖 Needs Practice  : "
                f"{weakest_topic.title()}"
            )

    else:
        print("\n📚 TOPIC PROGRESS")
        print("--------------------------------")
        print("No topic data yet.")
    show_achievements(progress)
    print("\n================================")