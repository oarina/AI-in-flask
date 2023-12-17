from openai import OpenAI
from flask import Flask, request, jsonify
# import requests # this may be possibly needed to send formatted answer to the API
client = OpenAI()

@app.route('/submit-task', methods=['POST']) # LOOK INTO MORE about routing not the page but to a form?
def user_input():
    task = request.form.get['taskInput'] # call your api with 'task' as input
    response = requests.post
    print(user_input)

return user_input # that will be slotted into the call 

#  -------------user_input needs to be a string with brackets "xxxxx"

# this is the format it shoud be in "Compose a poem that explains the concept of recursion in programming."

#  ============================================================================================================================  API call
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": user_input}
  ]
)

print(completion.choices[0].message)
'''