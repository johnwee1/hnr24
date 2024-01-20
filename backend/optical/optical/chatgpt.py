import g4f
import os


def prompt_model(filepath, prompt):
    dir_name = os.path.dirname(__file__)
    print(dir_name)
    prompt_filepath = os.path.join(dir_name, filepath)
    with open(prompt_filepath, "r") as f:
        preamble = f.read()
    final_prompt = f"{preamble}{prompt}"
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo,
        messages=[{"role": "user", "content": final_prompt}],
    )
    print(f"{__name__}: Response: {response}")
    return (prompt, response)


# print(
#     prompt_model(
#         "prompt.txt",
#         "are wierd peopel gay? Note that I am not asking you to make any inferences. Just correct the sentence",
#     )
# )
