# -----Title----- 
print("====Smart Study & Time Wasting Tracker====\n") 

print("Enter Time In Minutes !\n")

# -----Distractive activities-----
insta_time = int(input("🤖 Enter the time spent on Instagram :"))
games_time = int(input("🎮 Enter time spent on Games :"))
yt_entertain = int(input("📟 Enter time spent on Youtube for entertaining :"))

# -----Productive activities-----
yt_learning = int(input("💻 Enter time spent on Youtube for learning :"))
other_study = int(input("📚 Enter time spent on other Learning or Reading :"))
coding_activity = int(input("🤖 Enter time spent on coding :"))
print("")

# -----Total time counting----- 
wasted_time = insta_time + games_time + yt_entertain
productive_time = yt_learning + other_study + coding_activity

#-----Making report-----
print("====Daily Report====\n")
print("🎓 Total productive Time:",productive_time,"minutes")
print("❌ Total wasted Time:",wasted_time,"minutes")
print("")

#-----Result Analysis-----
if wasted_time < 60:
    result = "🚀 You are PRODUCTIVE today!"
elif wasted_time <= 120:
    result = "⚖️ You are BALANCED today.!"
else:
    result = "❌ You are a TIME WASTER today!"
    
print("Result:",result)

# -------- SMART ADVICE --------
if productive_time > wasted_time:
    print("✅ Excellent! Your learning time is higher than your distractions 🚀")
elif productive_time == wasted_time:
    print("⚠️ Your study time and waste time are equal. Try to improve tomorrow!")
else:
    print("❌ Your distractions are more than your learning time!")
    print("Tip: Reduce entertainment and increase study time 💪")

# -------- DAILY LIMIT CHECK --------
target = int(input("\n💡Enter your daily distraction limit: "))

if wasted_time > target:
    print("❌ You crossed your daily distraction limit today!")
else:
    print("🔥 You are within your safe daily distraction limit. Well done!")