import re
def classify_with_regex(log_message):
    regex_patterns = {
        r"User User\d+ logged (in|out)": "User action",
        r"Backup (started|ended) at .*": "System notification",
        r"backup completed successfully": "System notification",    
        r"System updated to version .*" : "System notification",
        r"file .* uploaded successfully by user .*": "system notification",
        r"disk cleanup completed successfully": "System notification",
        r"system reboot initialized by user .*": "System notification",
        r"account with ID .* created by .*":"user action",
        r"account with ID .* deleted by .*":"user action",
        r"failed login attempt for user .* from IP .*":"security event",
        r"unauthorized access attempt detected from IP .*":"security event",
        r"malware detected in file .* uploaded by user .*":"security event",
    }

    for pattern, label in regex_patterns.items():
        if re.search(pattern, log_message, re.IGNORECASE):
            return label
        return None
    

if __name__ == "__main__":
    print(classify_with_regex('user user123 logged in'))
    print(classify_with_regex('Backup started at 2024-06-01 12:00:00'))
    print(classify_with_regex('System updated to version 2.1.0'))
    print(classify_with_regex('file report.pdf uploaded successfully by user user456'))
    print(classify_with_regex('relax honey'))