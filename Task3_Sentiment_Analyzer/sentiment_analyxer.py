feedback = "The service is very slow and I need help immediately."

if "slow" in feedback.lower():
    sentiment = "Negative"
else:
    sentiment = "Positive"

if "immediately" in feedback.lower():
    urgency = "High"
else:
    urgency = "Low"

print("Sentiment:", sentiment)
print("Urgency:", urgency)
