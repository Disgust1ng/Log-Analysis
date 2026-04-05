log_file = "sample_log.txt"

failed_logins = 0
successful_logins = 0

users = {}

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            failed_logins += 1

            parts = line.strip().split()
            user = parts[-1]

            users[user] = users.get(user, 0) + 1

        elif "Accepted password" in line:
            successful_logins += 1
            
print("=== Log Analysis Summary ===")
print(f"Failed login attempts: {failed_logins}")
print(f"Successful logins: {successful_logins}\n")

print("Failed login attempts by user:")
for user, count in users.items():
    print(f"{user}: {count}")
