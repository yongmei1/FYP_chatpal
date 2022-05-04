<!-- Rasa does not run custom actions in tests (e.g. action_check_session_start_slots). You have to set slots manually 
to simulate the action's effects where required. -->

## Happy path
* greet: hi
    - action_check_session_start_slots
    - utter_ask_know_more
    - action_listen
* affirm: /affirm
    - action_tell_more
* affirm: yes
    - utter_explain_funding_and_consent
    - utter_ask_consent
* affirm: yeah
    - utter_consent_positive_response
    - user_ageRange_form
    - form{"name": "user_ageRange_form"}
    - form{"name": null}
    - action_reset_name
    - user_name_form
    - form{"name": "user_name_form"}
    - form{"name": null}
    - utter_ask_details
* affirm: /affirm
    - user_details_form
    - form{"name": "user_details_form"}
    - form{"name": null}
    - utter_ask_to_know_behaviour_change
* affirm: /affirm
    - action_explain_behaviour_change
    - utter_ask_permah
    - action_listen


## Redo Onboarding
* greet: hi
    - action_check_session_start_slots
    - utter_ask_know_more
    - action_listen
* affirm: /affirm
    - action_tell_more
* affirm: yes
    - utter_explain_funding_and_consent
    - utter_ask_consent
* affirm: yeah
    - utter_consent_positive_response
    - user_ageRange_form
    - form{"name": "user_ageRange_form"}
    - form{"name": null}
    - action_reset_name
    - user_name_form
    - form{"name": "user_name_form"}
    - form{"name": null}
    - utter_ask_details
* affirm: /affirm
    - user_details_form
    - form{"name": "user_details_form"}
    - form{"name": null}
    - utter_ask_to_know_behaviour_change
* affirm: /affirm
    - action_explain_behaviour_change
    - utter_ask_permah
    - action_listen
* redo_onboarding: /redo_onboarding
    - action_reset_slots
    - action_check_session_start_slots
    - utter_ask_know_more
    - action_listen


## Bye
* goodbye: bye
    - utter_goodbye


## greet test
* greet: hi
    - action_check_session_start_slots
    - utter_ask_know_more
    - action_listen
* deny: /deny
    - utter_onboarding_not_know_more_response


## test 3
* show: show
    - action_show_menu
    - action_listen
* who_intent: /who_intent
    - utter_ask_who_choices
* explain_who: /explain_who
    - utter_who_explain
    - utter_who_more_info
    - utter_ask_who_choices
* show: /show
    - action_show_menu
    - action_listen
* goodbye: /goodbye
    - utter_goodbye
* exit: /exit
    - utter_exit


## Engagement happy path
* show: show
    - action_show_menu
    - action_listen
* engagement: /engagement
    - utter_engagement_intro
    - utter_ask_know_more
    - action_listen
* affirm: /affirm
    - utter_engagement_start_a
    - utter_engagement_start_b
    - utter_engagement_start_c
    - utter_ask_make_sense
* affirm: /affirm
    - utter_engagement_note_before_work
    - utter_engagement_meaning_purpose
    - utter_engagement_work_meaning


## Relationships happy path
* show: show
    - action_show_menu
    - action_listen
* relationships: /relationships
    - utter_relationships_intro
	- utter_ask_to_know_one_way
* affirm: /affirm
	- utter_relationships_start_random_acts_kindness
* moreInfo: /moreInfo
    - utter_relationships_explain_random_acts_kindness
    - utter_ask_someone_could_benefit_act
* affirm: /affirm
	- utter_relationships_think_someone
	- utter_ask_relationships_can_do_something
* moreInfo: /moreInfo
	- utter_relationship_give_more_info
    - utter_ask_something_consider
* affirm: /affirm
	- utter_relationships_consider_positive_response
	- utter_ask_relationships_hear_another_way
* affirm: /affirm
    - utter_relationships_explain_another_way
    - utter_ask_heated_conversation
* affirm: /affirm
	- utter_relationships_heated_conversation_response_a
    - utter_relationships_heated_conversation_response_b
    - utter_relationships_heated_conversation_response_c
    - utter_ask_want_to_hear
* affirm: /affirm
	- utter_relationships_hear_response_a
    - utter_relationships_introduce_stop
* moreInfo: /moreInfo
    - utter_relationships_explain_s
* continueStop: What about the T?
    - utter_relationships_explain_t
	- utter_relationships_t_exercise
* finished: I am finished
    - utter_ask_ready_for_o
* affirm: /affirm
	- utter_relationships_explain_o
* continueStop: What about the P?
    - utter_relationships_explain_p
	- utter_ask_something_can_try
* affirm: /affirm
	- utter_relationships_can_try_response
	- utter_relationships_exit_point
* affirm: /affirm
	- utter_relationships_exit_phrase
    - utter_end_permah_option
	- utter_ask_permah_short
    - action_listen


## Accomplishment
* show: show
    - action_show_menu
    - action_listen
* accomplishment: accomplish
	- utter_accomplishment_intro
    - utter_ask_would_like_to_try
* affirm: /affirm
	- utter_accomplishment_love_energy
    - utter_ask_get_pen
* affirm: /affirm
	- utter_accomplishment_explain_first_task_a
    - utter_accomplishment_explain_first_task_b
	- action_accomplishment_check_all_good
* affirm: /affirm
	- action_accomplishment_next_task
* affirm: /affirm
	- utter_accomplishment_explain_second_task
    - utter_ask_accomplishment_second_task
* affirm: /affirm
	- utter_accomplishment_super
    - utter_ask_accomplishment_think_action
* affirm: /affirm
	- utter_accomplishment_action_positive_response
	- utter_accomplishment_exit_point
    - utter_end_permah_option
    - utter_ask_permah_short
    - action_listen


## Emotion
* show: show
    - action_show_menu
    - action_listen
* emotion: /emotion
	- utter_emotion_intro
    - utter_ask_feeling
* feeling_happy: happy
	- utter_ask_get_happier
* affirm: /affirm
	- utter_emotion_get_happier_response
    - utter_ask_about_attitude
* affirm: /affirm
	- utter_emotion_start_task
    - utter_emotion_grateful_reason_a
	- first_grateful_reason_form
	- form{"name": "first_grateful_reason_form"}
	- form{"name": null}
	- utter_ask_try_one_more
* affirm: /affirm
	- utter_emotion_grateful_reason_b
    - second_grateful_reason_form
	- form{"name": "second_grateful_reason_form"}
	- form{"name": null}
	- utter_emotion_grateful_response
    - utter_ask_hear_questions
* affirm: /affirm
	- utter_emotion_explain_questions
	- utter_emotion_exit_point
	- utter_end_permah_option
	- utter_ask_permah_short
    - action_listen
