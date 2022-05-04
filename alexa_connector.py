from numpy import full
import nltk
import nltk.corpus
import logging
import json
import re
from sanic import Blueprint, response
from sanic.request import Request
from typing import Text, Optional, List, Dict, Any

from rasa.core.channels.channel import UserMessage, OutputChannel
from rasa.core.channels.channel import InputChannel
from rasa.core.channels.channel import CollectingOutputChannel
from pprint import pprint
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize #pass string text into word tokenize
from nltk.probability import FreqDist #Importing FreqDist library from nltk and passing token into FreqDist: finds frequency distinct in the tokens
from nltk.stem import PorterStemmer #checking the word for 'waiting'
from nltk.stem import LancasterStemmer #importing LancasterStemmer from nltk
from nltk.stem import WordNetLemmatizer #importing lemmatizer library from nltk
from nltk.corpus import stopwords #importing stopwords from nltk library
from nltk import ne_chunk #tokenise and POS tagging before doing chunk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer #import the vader sentiment libraray

logger = logging.getLogger(__name__)

nltk.download([
    "names",
    "stopwords",
    "state_union",
    "twitter_samples",
    "movie_reviews",
    "averaged_perceptron_tagger",
    "vader_lexicon",
    "punkt",
    "wordnet",
])


wordList=[]
seconds="0.3s"
sentiment=""
score=""
result=""
result2=""
lang="en-GB"

# function to print sentiments
# of the sentence.
def sentiment_scores(sentence):
    
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
    print("sentence for sentiment processing: " + sentence)
    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
    print("Sentence Overall Rated As", end = " ")
    # decide sentiment as positive, negative and neutral
    
    #TODO: ssml mapping if statements to differentiate low med high ssml tag responses
    
    # positive - happiness
    if sentiment_dict['compound'] >= 0.05 and  sentiment_dict['compound'] < 0.06:
        print("Positive")
        sentiment="positive" 
        sentimentScore=sentiment_dict['compound']
        #logger.warning(sentiment_dict['pos'])  
        return sentiment
    
    if sentiment_dict['compound'] >=  0.06 and sentiment_dict['compound'] < 0.7:
        print("More Positive")
        sentiment="more positive" 
        sentimentScore=sentiment_dict['compound'] 
        return sentiment
    
    if sentiment_dict['compound'] <=  0.7:
        print("Strongly Positive")
        sentiment="strongly positive" 
        sentimentScore=sentiment_dict['compound'] 
        return sentiment
    
    # negative - negative
    if sentiment_dict['compound'] <= - 0.05 and sentiment_dict['compound'] > - 0.06:
        print("Negative")
        sentiment="negative" 
        sentimentScore=sentiment_dict['compound'] 
        return sentiment
    
    if sentiment_dict['compound'] <=  - 0.06 and sentiment_dict['compound'] > - 0.7:
        print("More Negative")
        sentiment="more negative" 
        sentimentScore=sentiment_dict['compound'] 
        return sentiment

    if sentiment_dict['compound'] <=  - 0.7:
        print("Strongly Negative")
        sentiment="strongly negative" 
        sentimentScore=sentiment_dict['compound'] 
        return sentiment
    
    #neutral
    else :
        print("Neutral")
        sentiment="neutral" 
        sentimentScore=sentiment_dict['compound'] 
        return sentiment
            
            
class AlexaConnector(InputChannel):
    """A custom http input channel for Alexa.
    You can find more information on custom connectors in the 
    Rasa docs: https://rasa.com/docs/rasa/user-guide/connectors/custom-connectors/
    """

    @classmethod
    def name(cls):
        return "alexa_assistant"

    # Sanic blueprint for handling input. The on_new_message
    # function pass the received message to Rasa Core
    # after you have parsed it
    def blueprint(self, on_new_message):

        alexa_webhook = Blueprint("alexa_webhook", __name__)
        logger.warning('----------------------------------------------')  # will print a message to the console
        # required route: use to check if connector is live
        @alexa_webhook.route("/", methods=["GET"])
        async def health(request):
            return response.json({"status": "ok"})

        # required route: defines
        @alexa_webhook.route("/webhook", methods=["POST"])
        async def receive(request):
            # get the json request sent by Alexa
            payload = request.json
            
            # check to see if the user is trying to launch the skill
            intenttype = payload["request"]["type"]
            logger.warning(intenttype)
            # if the user is starting the skill, let them know it worked & what to do next
            if intenttype == "LaunchRequest":
                ssml="excited"
                intensity="medium"
                message = "<speak><amazon:emotion name='"+ssml+"' intensity='"+intensity+"'><lang xml:lang='"+lang+"'>Hello! Welcome to chat pal. Start by saying  'hi'.</lang></amazon:emotion></speak>"
                #message = "<speak>Hello! Welcome to chat pal. Start by saying  'hi'.</speak>"
                
                session = "false"
            else:
                # get the Alexa-detected intent
                intent = payload["request"]["intent"]["name"]
        
                # makes sure the user isn't trying to end the skill
                if intent == "AMAZON.StopIntent":
                    session = "true"
                    message = "Talk to you later"
                else:
                    # get the user-provided text from the slot named "text"
                    text = payload["request"]["intent"]["slots"]["text"]["value"]

                    # initialize output channel
                    out = CollectingOutputChannel()
                    
                    # send the user message to Rasa & wait for the
                    # response to be sent back
                    await on_new_message(UserMessage(text, out))
                    # extract the text from Rasa's response
                    logger.warning('#######################################')
                    logger.warning(out.messages)
                    responses = [m["text"] for m in out.messages]
                    #logger.warning(responses)
                    
                    
                   # message=self.processMessages(out.messages)
                    
                    
                    logger.warning("*********testing 1***********")
                    responsestest = [m["text"].split() for m in out.messages]
                    logger.warning(responsestest)
                    logger.warning(responsestest[0])
                   # if responsestest[1]!="":
                   #     logger.warning(responsestest[1])
                    
                    
                    string = ""
                    for item in responsestest[0]:
                        string = string + " " + item
                    #the string is the message as a string
                    logger.warning(string)
                    
                    logger.warning("*********testing 2***********")
                    string_list = string.split()
                    
                    logger.warning(string_list)
                    
                    # TODO: opening the text file to read POSITIVE and NEGATIVE words and then compare for sentiment analysis on word level
                     
                    #count = 0
                    with open("positive-words.txt") as fp:
                        for line in fp:
                            #count += 1
                            #print("Line{}: {}".format(count, line.strip()))
                            wordList.append(line.strip())
                    fp.close()
                    with open("negative-words.txt") as fp:
                        for line in fp:
                            #count += 1
                            #print("Line{}: {}".format(count, line.strip()))
                            wordList.append(line.strip())
                    fp.close()
                    
                   
                    logger.warning("*********testing 3***********")
                    #logger.warning(wordList)
                   
                    logger.warning("*********testing 4***********")
                    stringlist_as_set=set(string_list)
                    intersection = stringlist_as_set.intersection(wordList)
                    intersection_as_list = list(intersection)
                    logger.warning(intersection_as_list)
                    
                    logger.warning("*********testing 6***********")
                    intersectionstring= ' '.join(intersection_as_list)
                    logger.warning(intersectionstring)
                   

                    logger.warning("*********testing 7***********")
                    word_score = sentiment_scores(intersectionstring)
                    result2=word_score
                    logger.warning("test result2 output = "+ result2)
                    
                    
                    
                    global result
                    #text = message;
            
                    if(string !=""):
                        token = word_tokenize(string)
                        #fdist = FreqDist(token)
                        pst = PorterStemmer()
                        pst.stem(string)
                        lemmatizer = WordNetLemmatizer()
                        print("lemmatisation process result : ", lemmatizer.lemmatize(text))
                        #text = text.lower();
                        #sentiment_scores(text)
                    
                    score = sentiment_scores(string)
                    result=score
                    
                    
                    
                    logger.warning("process message before result = "+result)   
                    
                    message2=self.processMessages(out.messages)
                    logger.warning("MESSAGE 2 RETURN FROM PROCESS MESSAGE FUNCTION: "+message2)

                    ##the lines below are done using regex and replaces fullstops with the seconds
                    message3 = re.sub(r'\. +', ". <break time='"+seconds+"'/>", message2)
                    
                    idx = message3.find('... ')
                    longersecond='0.5s'
                    message4 = message3[:idx]+message3[idx:].replace('... ', "... <break time='"+longersecond+"'/>")
                    
                    
                    logger.warning("NO PUNCTUATION BUT PAUSES TOO MAYBE")
                    logger.warning("result = "+result)
                    

                    #swap sentence sentiment to the word level sentiment as it is a stronger indication of the emotion of the sentence
                    if result2!=result:
                        result2==result

                    logger.warning("now our result is = "+ result2)  
                    logger.warning("message3 = "+message3) 
                    message2=message4
                    if result2=="positive":
                        ssml="excited"
                        intensity="low"
                        message2 = message4[:10]+"<amazon:emotion name='"+ssml+"' intensity='"+intensity+"'>" +message4[10:]

                    elif result2=="more positive":
                        ssml="excited"
                        intensity="medium"
                        #message=message+"<amazon:emotion name='"+ssml+"' intensity='"+intensity+"'>" 
                        message2 = message4[:10]+"<amazon:emotion name='"+ssml+"' intensity='"+intensity+"'>" +message4[10:]
            
                    elif result2=="strongly positive":
                        ssml="excited"
                        intensity="high"
                        message2 = message4[:10]+"<amazon:emotion name='"+ssml+"' intensity='"+intensity+"'>" +message4[10:]
                        
                    elif result2=="negative":
                        ssml="disappointed"
                        intensity="low"
                        message2 = message4[:10]+"<amazon:emotion name='"+ssml+"' intensity='"+intensity+"'>" +message4[10:]

                    elif result2=="more negative":
                        ssml="disappointed"
                        intensity="medium"
                        message2 = message4[:10]+"<amazon:emotion name='"+ssml+"' intensity='"+intensity+"'>" +message4[10:]
                        
                    elif result2=="strongly negative":
                        ssml="disappointed"
                        intensity="high"
                        message2 = message4[:10]+"<amazon:emotion name='"+ssml+"' intensity='"+intensity+"'>" +message4[10:]
                    
                    else:
                        message2=message2
                        
                    
                    if result2=="positive" or result2=="more positive" or result2=="strongly positive" or result2=="negative" or result2=="more negative" or result2=="strongly negative":
                        message=message2+"</amazon:emotion></p></speak>"
        
                    else:
                        message=message2+"</p></speak>" 
                        
                    logger.warning("message2 after processing: "+message2)
                    logger.warning("message after processing: "+message)
                    logger.warning("message4 after processing: "+message4)
                    
                                
#                    message = responses[0]
                    session = "false"
            # Send the response generated by Rasa back to Alexa to
            # pass on to the user. For more information, refer to the
            # Alexa Skills Kit Request and Response JSON Reference:
            # https://developer.amazon.com/en-US/docs/alexa/custom-skills/request-and-response-json-reference.html
            r = {
                "version": "1.0",
                "sessionAttributes": {"status": "test"},
                "response": {
                    "outputSpeech": {
                        "type": "SSML",
                        "text": message,
                        "ssml": message,
                        #"ssml": "<speak>This output speech uses SSML.</speak>",
                        "playBehavior": "REPLACE_ENQUEUED",
                    },
                    "reprompt": {
                        "outputSpeech": {
                            "type": "PlainText",
                            "text": message,
                            "playBehavior": "REPLACE_ENQUEUED",
                        }
                    },
                    "shouldEndSession": session,
                },
            }

            return response.json(r)

        return alexa_webhook
        
        
    def processMessages(self, messages):
        message=""
        message="<speak><p>"
           
        logger.warning("process message before result = "+result)    
        

        #  print str(responses)

        logger.warning("PROCESS MESSAGES 2")
        
            
        for m in messages: 
            logger.warning(m)
            logger.warning("TEXT:"+m['text'])
            seconds="0.1s"
            message=message+"<s>"+m['text']+"</s>"
            if 'buttons' in m:
                buttons = m['buttons']
                logger.warning("WITH BUTTONS:"+str(buttons))
                blist=[]
                blistjoin=" "
                for b in buttons:
                    #bstr = b['title']+ " <break time='"+seconds+"'/> "
                    #blist.append(bstr)
                    blist.append(b['title'])
                separator = " <break time='"+seconds+"'/> "+' or '
                blistjoin=' or '.join(blist)
                blistjoin2 = separator.join(blist)
                #orstring = ' or '+ " or <break time='"+seconds+"'/> "
                #sblistjoin=orstring.join(blist)
                #logger.warning("blistjoin " + blistjoin)
                logger.warning("blistjoin2 " + blistjoin2)
                #message = message+ "<s>" + blistjoin2 + "</s>"
                message = message+ "<s> Please choose " + blistjoin2 + " </s>"
            else :
                logger.warning("NO BUTTONS")
#            message=message+", "+m['text']+""
#        message=message+"</p></speak>"
        
        return message
    
