def get_achievements(progress):
    achievements = []

    quizzes = progress["quizzes_completed"]
    total_questions = progress["total_questions"]
    best_score = progress["best_score"]
    topics = progress.get("topics", {})

    if quizzes >= 1:
        achievements.append("🥉 First Step")

    if quizzes >= 3:
        achievements.append("🔥 Getting Serious")

    if best_score >= 100:
        achievements.append("🏆 Perfect Mind")

    if len(topics) >= 5:
        achievements.append("📚 Knowledge Seeker")

    if total_questions >= 100:
        achievements.append("💯 Century Club")

    return achievements


def show_achievements(progress):
    achievements = get_achievements(progress)

    print("\n================================")
    print("       🏅 ACHIEVEMENTS")
    print("================================")

    if achievements:
        print("\n🎉 Unlocked Badges:\n")

        for badge in achievements:
            print(f"  {badge}")

    else:
        print("\n🔒 No achievements unlocked yet.")
        print("Keep studying to unlock badges!")

    print("\n================================")