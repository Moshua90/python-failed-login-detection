failed_attempts = {}

with open("auth_log.txt", "r") as file:
    for line in file:
        if "FAILED" in line:

            parts = line.split()

            ip_address = parts[4].split('=')[1]

            failed_attempts[ip_address] = failed_attempts.get(ip_address, 0) + 1

print("\nFailed login Summary:")

for ip, count in failed_attempts.items():
    print(ip, ":", count, "failed attempts")

print("\nSecurity Alerts:") 

for ip, count in failed_attempts.items():
    if count >= 3:
        print("WARNING:", ip, "has suspicious login activity!")
    else: 
        print(ip, "is below the alert threshold.")







# Check whether the login failed

# Extract the IP address

# Count failed attempts per IP address

# Display your results

# Flag suspicious IP addresses