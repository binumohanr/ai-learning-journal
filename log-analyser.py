# IT Log Analyser
# Binu Mohan — IT Engineer

logs = [
    "ERROR: Database connection timeout after 30s",
    "INFO: Server started successfully on port 8080",
    "ERROR: CPU usage at 95% — threshold exceeded",
    "WARNING: Disk space at 85% on /dev/sda1",
    "ERROR: Application crashed — out of memory",
    "INFO: Backup completed successfully",
]
print("=== IT Log Analyser ===")
print("Scanning " + str(len(logs)) + " log entries...\n")

errors = 0
warnings = 0
info = 0

for log in logs:
    if "ERROR" in log:
        print("🔴 " + log)
        errors += 1
    elif "WARNING" in log:
        print("🟡 " + log)
        warnings += 1
    else:
        print("🟢 " + log)
        info += 1
print("\n=== Summary ===")
print("🔴 Errors: " + str(errors))
print("🟡 Warnings: " + str(warnings))
print("🟢 Info: " + str(info))