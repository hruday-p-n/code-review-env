TASKS = {
    "easy_bug_detection": {
        "files": [
            {
                "filename": "main.py",
                "diff": "if x = 5:\n    print(x)"
            }
        ],
        "expected_issues": [
            {"type": "syntax", "severity": "high"}
        ]
    },

    "logical_bug_detection": {
        "files": [
            {
                "filename": "auth.py",
                "diff": "if password == 'admin':\n    login()"
            }
        ],
        "expected_issues": [
            {"type": "security", "severity": "high"}
        ]
    },

    "full_pr_review": {
        "files": [
            {
                "filename": "db.py",
                "diff": "for i in range(len(data)):\n    process(data[i])"
            },
            {
                "filename": "auth.py",
                "diff": "if password == '1234':\n    login()"
            }
        ],
        "expected_issues": [
            {"type": "performance", "severity": "medium"},
            {"type": "security", "severity": "high"}
        ]
    }
}
