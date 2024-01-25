import os

from openai import OpenAI

client = OpenAI(
    api_key="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"
)


def dealWithImage():
    response = client.images.generate(
        model="dall-e-3",
        prompt="a white siamese cat",
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    print(image_url)


def dealTextContent():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": "Where was it played?"}
        ]
    )
    print("展示response==${}".format(response))


if __name__ == '__main__':
    dealTextContent()
