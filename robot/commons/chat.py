import openai
s_key = "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"
# org = "org-yMwBO3sXumI2BVGovkVbJMKh"
# openai.organization = org
openai.api_key = s_key


def gen_res(text):
    res = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=1024,
        temperature=0.5,
    )
    return res["choices"][0]["text"]
