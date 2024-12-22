def positive_feedback(ratings):
    if not ratings:
        return None
    return (ratings.count(4)+ratings.count(5))/len(ratings)*100
input_string=input("Enter ratings (comma-separated, 1-5): ").strip()
if not input_string:
    print("No ratings available.")
else:
    ratings = list(map(int, input_string.split(',')))
    positive_percentage=positive_feedback(ratings)
    print(f"Positive Feedback: {positive_percentage:.1f}%")


