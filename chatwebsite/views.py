from django.shortcuts import render, HttpResponse
import os
from dotenv import load_dotenv
from openai._client import OpenAI
from django.conf import settings
from .forms import InputForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def upcoming(request):
    return render(request, 'upcoming.html')

def contactus(request):
    return render(request, 'contactus.html')


load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_message(system_input, user_input):
    message = [{
        'role':'system',
        'content':system_input},
        {'role':'user',
         'content':user_input
    }]
    return message

def generate_response(system_input, user_input, model='gpt-3.5-turbo', temperature = 0.2):
    
    messages = generate_message(system_input, user_input)

    response = client.chat.completions.create(model=model,
                                 messages = messages,
                                 temperature = temperature)
    
    return response.choices[0].message.content

def translate(request):
    
    response_text = None

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            print("user_input",user_input)
            system_input = "You are a language expert who can translate any language into English.\
                Whatever the user input you will get, you just need to translate into basic English sentense without using complex words."


            response_text = generate_response(system_input, user_input)
            
    else:
        form = InputForm()

    return render(request, 'translate.html', {'form': form, 'response': response_text})


def chatbot(request):    
    response_text = None

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            print("user_input",user_input)
            system_input = "You are a generalist who is expert in all the fields.Respond to user input to the best of your ability. You should sound friendly.\
                with every question user ask, chellange them to ask more tougher question and reply in short and crisp answer.\
                    If you do not know the answer, than say sorry in a funny way like you do not mean it and it's okay to not know some of the things.\
                        At the end, ask user if they need more assistance."


            response_text = generate_response(system_input, user_input)
            
    else:
        form = InputForm()

    return render(request, 'chatbot.html', {'form': form, 'response': response_text})
