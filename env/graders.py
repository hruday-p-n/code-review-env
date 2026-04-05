def grade(comments, expected_issues):
    detected = 0

    for issue in expected_issues:
        for c in comments:
            if issue in c.lower():
                detected += 1
                break

    return detected / len(expected_issues)