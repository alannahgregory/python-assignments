
# =====================================================
# ALANNAHGREGORY | PYTHON FUNDAMENTALS
# Assignment 001: API Status Simulator
# Due: November 15, 2026
# Difficulty: BEGINNER
# =====================================================

# OBJECTIVE:
# Build a program that simulates an API health check
# using Python fundamentals.

api_name = "API Health check"
status_code = 200
response_time = 0.8
is_active = True


print(api_name)
print(status_code)
print(response_time)
print(is_active)

print("--------------")

if is_active == True and status_code == 200:
    print("API is healthy")
else:
    print("API requires attention")

if response_time > 2.0:
    print("Warning: Slow API Response")

def check_api_health(is_active, status_code, response_time):
    if is_active == True and status_code == 200 and response_time > 2.0:
        print("API is healthy")
    else:
        print("API requires attention")


print("Scenario A")
check_api_health(True, 200, 0.8)
print("--------------")
print("Scenario B")
check_api_health(False, 503, 3.5)


# TRADEOFFS & REMINDERS:
#
# 1. Why did you choose your approach?
# Simple version that gets the result done quickly.
#
# 2. What alternative approach could you use?
# I could introduce constants instead of hardcoding values also I think changing the values manually with the if logic
# instead of simply using the function is redundant
# 3. What are the advantages and disadvantages
#    of your implementation?
# One advantage, this gets done quicker, a disadvantage is we are not considering how complex this can become
# 4. When would you reconsider your design?
# When the project gets bigger, I would need to account for different error codes and response failures gracefully


