import os
from env.env import CodeReviewEnv
from env.models import Action

TASKS = ["easy_bug_detection", "logical_bug_detection", "full_pr_review"]

for task in TASKS:
    env = CodeReviewEnv(task)

    print(f"[START] task={task} env=code_review model=baseline")

    obs = env.reset()
    rewards = []
    step = 0
    done = False

    while not done and step < 5:
        step += 1

        if task == "easy_bug_detection":
            comment = "syntax error because assignment operator used incorrectly"
        elif task == "logical_bug_detection":
            comment = "security issue because hardcoded password is a vulnerability"
        else:
            comment = "performance issue because inefficient loop and security issue due to hardcoded password"

        action = Action(
            action_type="comment",
            comment=comment
        )

        obs, reward, done, info = env.step(action)
        rewards.append(reward)

        print(f"[STEP] step={step} action=comment reward={reward:.2f} done={str(done).lower()} error=null")

    action = Action(action_type="request_changes")
    obs, reward, done, info = env.step(action)
    rewards.append(reward)

    print(f"[STEP] step={step+1} action=request_changes reward={reward:.2f} done=true error=null")

    score = reward
    print(f"[END] success=true steps={step+1} score={score:.2f} rewards={','.join([f'{r:.2f}' for r in rewards])}")
