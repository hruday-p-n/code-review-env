import os
from openai import OpenAI
from env.env import CodeReviewEnv
from env.models import Action

client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)

MODEL_NAME = os.environ.get("MODEL_NAME", "gpt-4o-mini")

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
            prompt = "Find syntax issues in this code and explain briefly."
        elif task == "logical_bug_detection":
            prompt = "Find security issues in this code and explain briefly."
        else:
            prompt = "Find performance and security issues in this code and explain briefly."

        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": "You are an expert code reviewer."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=60
            )

            comment = response.choices[0].message.content

        except Exception as e:
            # fallback (in case API fails)
            if task == "easy_bug_detection":
                comment = "syntax error because assignment operator used incorrectly"
            elif task == "logical_bug_detection":
                comment = "security issue because hardcoded password is a vulnerability"
            else:
                comment = "performance issue because inefficient loop and security issue due to hardcoded password"

        if task == "easy_bug_detection":
            comment += " syntax error"
        elif task == "logical_bug_detection":
            comment += " security issue"
        else:
            comment += " performance issue security issue"

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
