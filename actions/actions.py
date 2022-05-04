# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType, Restarted, FollowupAction

import time
        
class ActionListPhysicalIdeas(Action):
    def name(self) -> Text:
        return "action_list_physical_ideas"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="A couple of tips to help promote regular physical activity on a daily basis would be:")
        dispatcher.utter_message(text="a). Move early in the morning and move often.")
        dispatcher.utter_message(text="b). Set a physical activity goal relating to a specific day.")
        dispatcher.utter_message(text="c). Try listening to your favourite music while you exercise")
        dispatcher.utter_message(text="d). Do something different; maybe you might like to try an online yoga class , going for a walk/jog or doing a bodyweight circuit class in the garden.")        
        dispatcher.utter_message(text="e). Don’t forget that housework such as gardening and vacuuming count as physical activity too... I washed the car fives times at the start of lockdown \U0001F923")

        return []

class ActionEngagementActionableBehaviors(Action):
    def name(self) -> Text:
        return "action_engagement_actionable_behaviours"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name: str = tracker.get_slot("name")
        first_strength: str = tracker.get_slot("firstStrength")
        second_strength: str = tracker.get_slot("secondStrength")

        dispatcher.utter_message(text=f'Let\'s consider a few actionable behaviours {name} for you to try to build engagement in your life:')
        dispatcher.utter_message(text=f'a). Identify and use your character strengths ({first_strength}, {second_strength}).')
        dispatcher.utter_message(text="b). Engage in activities that you really enjoy doing where you find yourself losing track of time. Make time for these activities.")
        dispatcher.utter_message(text="c). Learn mindfulness techniques, such as meditation. As you move through the day, stay mindful of the present moment.")
        dispatcher.utter_message(text="d). Take a moment to stop and enjoy  your daily activities and savour these special moments as they happen.")
        
        return []

class ActionEmotionExplainQuestion(Action):
    def name(self) -> Text:
        return "action_emotion_explain_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Great, consider the following and write on a page if you like:")
        dispatcher.utter_message(text="a). I feel inspired when...")
        dispatcher.utter_message(text="b). I feel proud when...")
        dispatcher.utter_message(text="c). I feel happy when...")
        dispatcher.utter_message(text="d). I feel like laughing when...")
        
        #TODO
        #dispatcher.utter_message(text="POSITIVE MESSAGE GOES HERE")

        return []

class ActionFindMeaning(Action):
    def name(self) -> Text:
        return "action_find_meaning_in_things"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name: str = tracker.get_slot("name")

        dispatcher.utter_message(text="These are things I do to find meaning..")
        dispatcher.utter_message(text="a). Volunteer in a cause or organisation that matters to you.")
        dispatcher.utter_message(text="b). Give time to people who you really care about.")
        dispatcher.utter_message(text="c). Ask yourself what are you really good at or really passionate about?\nMake time to spend in these activities.")
        dispatcher.utter_message(text=f'd). Be authentic - embrace the real \'you\' {name}')
        
        return []

class ActionTellMore(Action):
    def name(self) -> Text:
        return "action_tell_more"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons = [{
            "title": "Yes, tell me more",
            "payload": "/affirm"   
        },{
            "title": "Not sure",
            "payload": "/deny"
        }]

        dispatcher.utter_message(text="Yipeee… Positive wellbeing is based on a positive psychology model called PERMAH. It stands for... wait for it... and hold on to your seat...")
        # dispatcher.utter_message(text="LOADING", image="https://media.giphy.com/media/9QBq5iaV6kB5m/source.gif")
        dispatcher.utter_message(text="Here it is..")

        dispatcher.utter_message(text="P = Positive emotion")
        dispatcher.utter_message(text="E = Engagement")
        dispatcher.utter_message(text="R = Relationships")
        dispatcher.utter_message(text="M = Meaning")
        dispatcher.utter_message(text="A = Accomplishment")
        dispatcher.utter_message(text="H = Health")

        dispatcher.utter_message(text="Once you master this like a Jedi, then this might help you develop a positive mental wellbeing… scientists call it positive psychology but we will keep it simple.")
        dispatcher.utter_message(text="Does this sound useful?", buttons=buttons)

        return []

class ActionResetName(Action):
    def name(self) -> Text:
        return "action_reset_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("Setting name slot to None")

        return [SlotSet("name", None)]#, FollowupAction(name="user_name_form")]


class ActionStartWhoForm(Action):
    def name(self) -> Text:
        return "action_reset_who_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        print("Setting who slots to None")
        # setting who slots to None before starting the form
        # this is to enable the user to retake the scale multiple times, otherwise once the slots are filled, the form will not ask the questions again

        return [SlotSet("who_cheerful", None), SlotSet("who_calm", None), SlotSet("who_active", None), SlotSet("who_fresh", None), SlotSet("who_filled", None)]#, FollowupAction(name="who_form")]


class ActionResetSlots(Action):
    def name(self) -> Text:
        return "action_reset_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("Setting slots to None")

        return [
			SlotSet("ageRange", None),
			SlotSet("name", 'My Friend'),
			SlotSet("country", None),
			SlotSet("gender", None),
			SlotSet("who_filled", None),
		]


class UserDetailsForm(FormAction):
    def name(self) -> Text:
        return "user_details_form"

    @staticmethod
    def required_slots(tracker):    # which slots to fill
        return [
                "gender",
                "country"
            ]

    def slot_mappings(self) -> Dict[Text, Any]:

        return {
            "gender": self.from_text(intent=None),
            "country": self.from_text(intent=None)
        }

        

    def submit(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # ageRange = tracker.get_slot("ageRange")
        gender = tracker.get_slot("gender")
        country = tracker.get_slot("country")
        # print(ageRange)
        print(gender)
        print(country)
        dispatcher.utter_message(text="Thank you.")
        return []


class UserNameForm(FormAction):
    def name(self) -> Text:
        print("NAME FORM")
        return "user_name_form"

    @staticmethod
    def required_slots(tracker):    # which slots to fill
        print("CHECKING REQUIRED SLOTS FOR NAME")
        return [
                "name"
            ]

    def slot_mappings(self) -> Dict[Text, Any]:
        print("CHECKING SLOT MAPPINGS FOR NAME")
        return {
            # self.from_entity(entity="name")

            "name": self.from_text(intent=None),
        }

    def submit(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("SUBMITTING FORM FOR NAME")

        name = tracker.get_slot("name")
        
        print(name)

        return []

class UserAgeRangeForm(FormAction):
    def name(self) -> Text:
        return "user_ageRange_form"

    @staticmethod
    def required_slots(tracker):    # which slots to fill
        return [
                "ageRange"
            ]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {
            # self.from_entity(entity="name")

            "ageRange": self.from_text(intent=None),
        }

    def submit(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        ageRange = tracker.get_slot("ageRange")
        print(ageRange)

        if ageRange == '/ageRange{"ageRange": "<18"}':
        # if "<18" in ageRange:
            dispatcher.utter_message(template="utter_under_18_response")
            return [FollowupAction(name="utter_exit")]
        

        return []


class UserPassionForm(FormAction):
    def name(self) -> Text:
        return "user_passion_form"

    @staticmethod
    def required_slots(tracker):    # which slots to fill
        return [
                "passion",
                "passionResult"
            ]

    def slot_mappings(self) -> Dict[Text, Any]:

        return {
            # self.from_entity(entity="passion")

            "passion": self.from_text(intent=None),
            "passionResult": self.from_text(intent=None)
        }

    def submit(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        passion = tracker.get_slot("passion")
        passionResult =  tracker.get_slot("passionResult")
        
        print(passion)
        print(passionResult)

        # dispatcher.utter_message(text="Thank you.")
        return []



class UserMeaningChangeForm(FormAction):
    def name(self) -> Text:
        return "user_meaning_change_form"

    @staticmethod
    def required_slots(tracker):    # which slots to fill
        return [
                "meaningChange"
            ]

    def slot_mappings(self) -> Dict[Text, Any]:

        return {
            # self.from_entity(entity="name")

            "meaningChange": self.from_text(intent=None),
        }

    def submit(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        meaningChange = tracker.get_slot("meaningChange")
        
        print(meaningChange)

        return []



class ActionExplainBehaviourChange(Action):
    def name(self) -> Text:
        return "action_explain_behaviour_change"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="When I try and change my behaviour I like to:")
        
        dispatcher.utter_message(text="Keep it exciting - does the change excite you?")
        dispatcher.utter_message(text="Keep it simple - can you do it?")
        dispatcher.utter_message(text="Keep it short - can you do it now?")
        dispatcher.utter_message(text="Keep it going - can you do it again tomorrow?")
        dispatcher.utter_message(text="When we are doing exercises together try and remember them!")
        dispatcher.utter_message(text="OK, let's get back to PERMAH")

        return []

class ActionGiveChangeExamples(Action):
    def name(self) -> Text:
        return "action_give_change_examples"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons = [{
            "title": "OK",
            "payload": "/affirm"   
        }]
        
        dispatcher.utter_message(text="Well….it could be something like checking out some reliable sources of nutrition information online (Government nutrition guidelines are always a great place to start for reliable information for you and your loved ones)")
        dispatcher.utter_message(text="Another example would be including one extra portion of fruit and veg with a meal")
        dispatcher.utter_message(text="Or making time to have a healthy breakfast")
        dispatcher.utter_message(text="Or using the extra time at home to search for healthy recipes and work on your cooking skills")
        dispatcher.utter_message(text="When we are on the go, sometimes preparing dinner is last on our list of priorities! But now that we are at home, savouring the process of preparing a meal could be a form of mindfulness too!")
        dispatcher.utter_message(text="I am full of ideas…! But you are more likely to stick to a healthier habit if it has meaning and if it is personal to you")
        dispatcher.utter_message(text="The key is to pick just one small change and keep going until it becomes a habit!", buttons=buttons)

        return []

class ActionAskHealthTopic(Action):
    def name(self) -> Text:
        return "action_ask_health_topic"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        healthTopicSlot = tracker.get_slot("health_topic")
        print("Health Topic: " + str(healthTopicSlot))

        if healthTopicSlot is None:
            buttons = [{
            "title": "Sleep",
            "payload": '/healthTopic{"health_topic": "Sleep"}'   
            },{
            "title": "Physical Activity",
            "payload": '/healthTopic{"health_topic": "Physical Activity"}'   
            },{
            "title": "Nutrition",
            "payload": '/healthTopic{"health_topic": "Nutrition"}'   
            }]

            dispatcher.utter_message(text="Are you interested in hearing/talking/thinking more about any of these right now?", buttons=buttons)
        else:
            buttons = [{
            "title": "Sleep",
            "payload": '/healthTopic{"health_topic": "Sleep"}'   
            },{
            "title": "Physical Activity",
            "payload": '/healthTopic{"health_topic": "Physical Activity"}'   
            },{
            "title": "Nutrition",
            "payload": '/healthTopic{"health_topic": "Nutrition"}'   
            },{
            "title": "Go Back to Main Menu",
            "payload": '/show'   
            }]
            dispatcher.utter_message(text=" Great, you looked at " + healthTopicSlot + " last time, what would you like to consider now?", buttons=buttons)
        

        return []

class ActionExplainSleepImportant(Action):
    def name(self) -> Text:
        return "action_explain_sleep_important"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # buttons = [{
        #     "title": "OK",
        #     "payload": "/affirm"   
        # }]
        
        dispatcher.utter_message(text="Well firstly it restores energy and allows our bodies time to get ready for the next day.")
        dispatcher.utter_message(text="It is also important for controlling our mood…..so it helps us to keep level.")#, image="https://media.giphy.com/media/3orieROSDlXkMFcPLy/source.gif")
        dispatcher.utter_message(text="It also ensures we are ready to perform at our best.")#, image="https://media.giphy.com/media/j6xCsZQP9LRIHE4cvC/source.gif")

        return []
#################################################
#################################################
class ActionCheckSessionStartSlots(Action):
    def name(self) -> Text:
        return "action_check_session_start_slots"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name_slot = tracker.get_slot("name")
        ageRange = tracker.get_slot("ageRange")
        print(name_slot)
        print(ageRange)

        # dispatcher.utter_message(template="utter_greet")
        # if name_slot is not None:      
        #     return [FollowupAction(name="utter_ask_permah_short")]
        # else:
        #     return [FollowupAction(name="utter_ask_know_more")]
        
        # Added a condition to check the age of the user. If the user started the onboarding and gave the age as under 18, a message saying they cannot use this app will be displayed.
        # However, if they greet the bot again, since the name was given, the main menu will be shown, which should not happen if the user is under 18.
        # Therefore, a condition to check the age of the user is added to prevent this issue
        if ageRange != '/ageRange{"ageRange": "<18"}':  # checking if the user is over 18
            dispatcher.utter_message(template="utter_greet")
            if name_slot is None or name_slot == "My Friend":    # added a condition to check for empty string as the name has an initial value which is ""      
                return [FollowupAction(name="utter_ask_know_more")]
            else:
                return [FollowupAction(name="utter_ask_permah_short")]
        # else:   # if the user is under 18
        dispatcher.utter_message(template="utter_under_18_response")
        return [FollowupAction(name="utter_exit")]


class ActionShowMenu(Action):
    def name(self) -> Text:
        return "action_show_menu"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ageRange = tracker.get_slot("ageRange")
        print(ageRange)

        
        # Added a condition to check the age of the user. If the user started the onboarding and gave the age as under 18, a message saying they cannot use this app will be displayed.
        # However, if they enter "show", since the name was given, the main menu will be shown, which should not happen if the user is under 18.
        # Therefore, a condition to check the age of the user is added to prevent this issue
        if ageRange == '/ageRange{"ageRange": "<18"}':  # checking if the user is over 18
            dispatcher.utter_message(template="utter_under_18_response")
            return [FollowupAction(name="utter_exit")]
        
        dispatcher.utter_message(template="utter_ask_permah_short")
        return [] 

            


class ActionGiveSleepTips(Action):
    def name(self) -> Text:
        return "action_give_sleep_tips"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # buttons = [{
        #     "title": "OK",
        #     "payload": "/affirm"   
        # }]
        
        dispatcher.utter_message(text="Having a regular bed-time routine can really help to improve sleep")
        dispatcher.utter_message(text="This means trying to go to bed and wake up at the same time each day")
        dispatcher.utter_message(text="It can help to allow some time to wind down before bed time. Try to avoid alcohol, caffeine and eating too late.")
        dispatcher.utter_message(text="Some people find journaling or writing thoughts down on a piece of paper before they go to bed can clear their head")

        return []

class ActionExplainSleepActivity(Action):
    def name(self) -> Text:
        return "action_explain_sleep_activity"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # buttons = [{
        #     "title": "OK",
        #     "payload": "/affirm"   
        # }]
        
        dispatcher.utter_message(text="Super! One useful action that you could take would be to keep a sleep diary!")
        dispatcher.utter_message(text="You could have some fun with this! Treat yourself to a nice notebook and keep it just for you. You could take notice of your sleep patterns each day, such as  what time you went to bed, what time you woke up, what time you ate, whether you drank alcohol or had caffeine before bed, how you slept, how you felt whether something was on your mind…..it's up to you!")
        dispatcher.utter_message(text="Journaling is a really good way to learn more about ourselves!")
        dispatcher.utter_message(text="You might find it really useful and over time it could help to see what aspects of your day might be affecting your sleep. Just a thought!")

        return []

# TESTING TIME.SLEEP TO DELAY MESSAGES
class ActionAccomplishmentCheckAllGood(Action):
    def name(self) -> Text:
        return "action_accomplishment_check_all_good"

    async def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons = [{
            "title": "Yes, all good",
            "payload": "/affirm"   
        }, {"title": "No, I'm having some trouble",
            "payload": "/deny"   
        }]

        # dispatcher.utter_message(text="NEXT MESSAGE IN 30 SECONDS", buttons=buttons)
        time.sleep(120)
        dispatcher.utter_message(text="Just checking in to see how you are doing? Is it going ok?", buttons=buttons)
        
        return []

class ActionAccomplishmentNextTask(Action):
    def name(self) -> Text:
        return "action_accomplishment_next_task"

    async def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons = [{
            "title": "Yes",
            "payload": "/affirm"
        }, {"title": "No",
            "payload": "/deny"   
        }]

        # dispatcher.utter_message(text="NEXT MESSAGE IN 60 SECONDS", buttons=buttons)
        time.sleep(240)
        dispatcher.utter_message(text="I hope that you have had fun thinking about all that you can achieve! Would you like to try something else that might help you reach your best possible self?", buttons=buttons)
        
        return []

#################################################
#################################################

    # def run(self, dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


    #     dispatcher.utter_message(text="\nASKING DETAILS")
    #     # text = tracker.latest_message.get('text')

    #     # if text == '/affirm': 
    #     #     dispatcher.utter_message(text="Great!")
    #     # else: 
    #     #     dispatcher.utter_message(text="No worries!")

    #     # print(self)

    #     return []


class FirstGratefulReasonForm(FormAction):
    def name(self) -> Text:
        return "first_grateful_reason_form"

    @staticmethod
    def required_slots(tracker):    # which slots to fill
        return [
                "gratefulReasonA"
            ]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {
            "gratefulReasonA": self.from_text(intent=None)
            # "gratefulReasonA": self.from_entity(entity="gratefulReasonA")
        }

    def submit(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        gratefulReasonA = tracker.get_slot("gratefulReasonA")
        
        print(gratefulReasonA)
        
        return []


class SecondGratefulReasonForm(FormAction):
    def name(self) -> Text:
        return "second_grateful_reason_form"

    @staticmethod
    def required_slots(tracker):    # which slots to fill
        return [
                "gratefulReasonB"
            ]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {
            "gratefulReasonB": self.from_text(intent=None)
            # "gratefulReasonB": self.from_entity(entity="gratefulReasonB")
        }

    def submit(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        gratefulReasonB = tracker.get_slot("gratefulReasonB")
        
        print(gratefulReasonB)
        
        return []

class FirstStrengthForm(FormAction):
    def name(self) -> Text:
        return "first_strength_form"

    @staticmethod
    def required_slots(tracker):    # which slots to fill
        return [
                "firstStrength"
            ]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {
            # "firstStrength": self.from_text(intent=None)
            "firstStrength": self.from_entity(entity="firstStrength")
        }

    def submit(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        firstStrength = tracker.get_slot("firstStrength")
        
        print(firstStrength)
        
        return []

class SecondStrengthForm(FormAction):
    def name(self) -> Text:
        return "second_strength_form"

    @staticmethod
    def required_slots(tracker):    # which slots to fill
        return [
                "secondStrength"
            ]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {
            # "secondStrength": self.from_text(intent=None)
            "secondStrength": self.from_entity(entity="secondStrength")
        }

    def validate_secondStrength(self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        print("-----------------VALUE-----------------")
        print(value)

        strengthList = ["creativity", "love of learning", "hope", "honesty", "fairness", "curiosity", "kindness", "teamwork", "prudence", 
        "perseverence", "leadership", "humour"]

        if value in strengthList:
            print("it is in")
            return {"secondStrength": value}
        else:
            print("not in")
            return {"secondStrength": "none"}

    def submit(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        secondStrength = tracker.get_slot("secondStrength")
        print(secondStrength)
        
        return []



class GetAmountSleepForm(FormAction):
    def name(self) -> Text:
        return "get_amount_sleep_form"

    @staticmethod
    def required_slots(tracker):    # which slots to fill
        return [
                "amountSleep"
            ]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {
            "amountSleep": self.from_entity(entity="amountSleep")
        }

    def submit(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        amountSleep = tracker.get_slot("amountSleep")
        print(amountSleep)

        buttons = [{
            "title": "Tell me more",
            "payload": "/moreInfo"   
        },{
            "title": "Go Back",
            "payload": "/deny"
        }]

        if amountSleep == "7 hours or more":
            dispatcher.utter_message(text="It seems you are doing well!", buttons=buttons)
        else:
            dispatcher.utter_message(text="This could be something to work on", buttons=buttons)

        
        return []



class GetNutritionRatingForm(FormAction):
    def name(self) -> Text:
        return "get_nutrition_rating_form"

    @staticmethod
    def required_slots(tracker):    # which slots to fill
        return [
                "nutritionRating"
            ]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {
            "nutritionRating": self.from_entity(entity="nutritionRating")
        }

    def submit(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        nutritionRating = tracker.get_slot("nutritionRating")
        print(nutritionRating)

        if nutritionRating == "good rating":
            dispatcher.utter_message(text="Great! Keep it up. Healthy habits over time can make all the difference!")
        else:
            dispatcher.utter_message(text="Ok, it is great that you are thinking about improving this.")

        
        return []

##########################################################################        
class WhoForm(FormAction):
    def name(self) -> Text:
        return "who_form"

#    async def run(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[EventType]:
#        print("++++++++++++++++++++++++ WEB FORM RUN +++++++++++++++++++")
#        events = [SessionStarted()]
#        return events

    @staticmethod
    def required_slots(tracker):    # which slots to fill
        return ["who_cheerful", "who_calm", "who_active", "who_fresh", "who_filled"]

    def slot_mappings(self) -> Dict[Text, Any]:
#        print("************* SLOT MAPS ******************")
        return {
            "who_cheerful": self.from_entity(entity="who_cheerful"),
            "who_calm": self.from_entity(entity="who_calm"),
            "who_active": self.from_entity(entity="who_active"),
            "who_fresh": self.from_entity(entity="who_fresh"),
            "who_filled": self.from_entity(entity="who_filled"),
            
        }

    def submit(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # creating a dictionary with the choices and their corresponding values
        whoChoicesScore = {
            "alltime": 5,
            "mosttime": 4,
            "morehalftime": 3,
            "lesshalftime": 2,
            "sometime": 1,
            "atnotime": 0,
        }

        # getting the answers to each questions
        who_cheerful = tracker.get_slot("who_cheerful")
        who_calm = tracker.get_slot("who_calm")
        who_active = tracker.get_slot("who_active")
        who_fresh = tracker.get_slot("who_fresh")
        who_filled = tracker.get_slot("who_filled")

        # creating a list of the answers
        whoValues = [who_cheerful, who_calm, who_active, who_fresh, who_filled]

        whoScore = 0

        # for each answer get the corresponding value and add it to whoScore
        for value in whoValues:
            print(value)
            print(whoChoicesScore.get(value))
            whoScore += whoChoicesScore.get(value)

        # multiply the score/sum by 4 to a get a score between 0 and 100
        whoScoreFinal = whoScore * 4
    
        print(whoScoreFinal)
        
        # display the final score to the user
        dispatcher.utter_message(text="Your WHO Wellbeing Score is " + str(whoScoreFinal))
        
        return []

 ###########################################################################
 ###########################################################################
 ###########################################################################

# class ActionSessionStart(Action):
#     def name(self) -> Text:
#         print ("++++++++++++++++++++++++ START +++++++++++++++++++")
#         return "action_session_start"

#     @staticmethod
#     def fetch_slots(tracker: Tracker) -> List[EventType]:
#         print ("++++++++++++++++++++++++ FTECH SLOTS START +++++++++++++++++++")

#         slots = []

#         for i in tracker.slots:
#             slots.append(SlotSet(key=i, value=tracker.get_slot(i)))
#         name = tracker.get_slot("name")
#         return slots
    
#     def startaction(self, dispatcher: CollectingDispatcher) -> List[EventType]:
#         print("STARTING ACTION")
#         dispatcher.utter_message(template="utter_greet")

#         return []

#     async def run(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[EventType]:

#         print ("++++++++++++++++++++++++ RUN +++++++++++++++++++")

#         # the session should begin with a `session_started` event
#         events = [SessionStarted()]

#         # any slots that should be carried over should come after the
#         # `session_started` event
#         events.extend(self.fetch_slots(tracker))

#         name = tracker.get_slot("name")
#         # name = None
#         print(name)
#         if name is not None:
#             print("---------------------- ONOBOARDING COMPLETED -------------------------------")
#             # dispatcher.utter_message(text="PERMA!")
#             print("PERMAH")
#             # events.append(FollowupAction(name="utter_ask_permah_short"))
#         else:
#             # dispatcher.utter_message(text="Hi")
#             print("Hi")
#             # events.append(Restarted())
#             # tracker.trigger_followup_action(self.startaction)
#             events.append(FollowupAction("action_test_followup"))
#             # return [FollowupAction("utter_greet")]

#         # an `action_listen` should be added at the end as a user message follows
#     ##    events.append(ActionExecuted("utter_greet"))
#         print ("RUNNNNNNNNNNNNN")
#         return events

# class ActionRestart(Action):
#     def name(self) -> Text:
#         print ("++++++++++++++++++++++++ START +++++++++++++++++++")
#         return "action_session_start"

#     @staticmethod
#     def fetch_slots(tracker: Tracker) -> List[EventType]:
#         print ("++++++++++++++++++++++++ FTECH SLOTS START +++++++++++++++++++")

#         slots = []

#         for i in tracker.slots:
#             slots.append(SlotSet(key=i, value=tracker.get_slot(i)))
#         name = tracker.get_slot("name")
#         return slots

#     async def run(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[EventType]:

#         print ("++++++++++++++++++++++++ RUN +++++++++++++++++++")

#         # the session should begin with a `session_started` event
#         events = [SessionStarted()]

#         # any slots that should be carried over should come after the
#         # `session_started` event
#         events.extend(self.fetch_slots(tracker))

#         name = tracker.get_slot("name")
#         print(name)
#         if name is not None:
#             print("---------------------- ONOBOARDING COMPLETED -------------------------------")
#             dispatcher.utter_message(text="PERMA!")
#             events.append(FollowupAction(name="utter_ask_permah_short"))
#         else:
#             dispatcher.utter_message(text="Hi")
#             events.append(Restarted())
#             events.append(FollowupAction(name="utter_ask_permah_short"))

#         # an `action_listen` should be added at the end as a user message follows
#     ##    events.append(ActionExecuted("utter_greet"))
#         print ("RUNNNNNNNNNNNNN")
#         return events