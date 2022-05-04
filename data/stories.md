## options shortcut
* show
	- action_show_menu
	<!-- - utter_ask_permah_short -->
> activity_selection

## goodbye
* goodbye
	- utter_goodbye

## exit
* exit
	- utter_exit


<!-- ## start conversation
* greet
	- action_check_session_start_slots -->

<!-- -------------------------------ONBOARDING STORIES------------------------------- -->

## onboarding happy path
* greet 
  - action_check_session_start_slots
  - utter_ask_know_more
> onboarding_know_more

## onboarding know more
> onboarding_know_more
* affirm
  - action_tell_more
> oboarding_sound_useful

## onboarding agree sound useful
> oboarding_sound_useful
* affirm OR deny
  - utter_explain_funding_and_consent
  - utter_ask_consent
> onboarding_get_consent

## onboarding not know more
> onboarding_know_more
* deny
  - utter_onboarding_not_know_more_response

## onboarding give consent
> onboarding_get_consent
* affirm
  - utter_consent_positive_response
  - user_ageRange_form
  - form{"name": "user_ageRange_form"}
  - form{"name": null}
  - action_reset_name
  - user_name_form
  - form{"name": "user_name_form"}
  - form{"name": null}
  - utter_ask_details
> onboarding_get_details

## onboarding not give consent
> onboarding_get_consent
* deny
  - utter_consent_negative_response
  - user_ageRange_form
  - form{"name": "user_ageRange_form"}
  - form{"name": null}
  - action_reset_name
  - user_name_form
  - form{"name": "user_name_form"}
  - form{"name": null}
  - utter_ask_details
> onboarding_get_details

## onboarding getting details
> onboarding_get_details
* affirm
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
  - utter_ask_to_know_behaviour_change
> onboarding_behaviour_change

## onboarding skip getting details
> onboarding_get_details
* skip
  - utter_no_worries
  - utter_ask_to_know_behaviour_change
> onboarding_behaviour_change

## onboarding explain behaviour change
> onboarding_behaviour_change
* affirm
  - action_explain_behaviour_change
  - utter_ask_permah
> activity_selection

## onboarding not explain behaviour change
> onboarding_behaviour_change
* deny
  - utter_ask_permah
> activity_selection


## restart onboarding
* redo_onboarding
  - action_reset_slots
  - action_check_session_start_slots
  - utter_ask_know_more
> onboarding_know_more

<!-- -------------------------------RELATIONSHIPS STORIES------------------------------- -->

## relationships happy intro
> activity_selection
* relationships{"selectedPermah": "Relationships"}
	- slot{"selectedPermah": "Relationships"}
	- utter_relationships_intro
    - utter_ask_to_know_one_way
> relationships_know_one_way

## relationships user wants to know one way
> relationships_know_one_way
* affirm
	- utter_relationships_start_random_acts_kindness
* moreInfo
    - utter_relationships_explain_random_acts_kindness
    - utter_ask_someone_could_benefit_act
> relationships_someone_could_benefit

## relationships user not want to know one way
> relationships_know_one_way
* deny
	- utter_ask_relationships_tip
> relationships_hear_another_way

## relationships there is someone that could benefit from the act
> relationships_someone_could_benefit
* affirm
	- utter_relationships_think_someone
	- utter_ask_relationships_can_do_something
> relationships_something_can_do_for_person

## relationships there is no one that could benefit from the act
> relationships_someone_could_benefit
* deny
	- utter_relationships_help_think_someone
	- utter_ask_continue
> relationships_someone_could_benefit
<!-- > relationships_something_can_do_for_person -->

## relationships user can do something for person
> relationships_something_can_do_for_person
* affirm
    - utter_ask_something_consider
> relationships_can_consider

## relationships user cannot do something for person
> relationships_something_can_do_for_person
* moreInfo
	- utter_relationship_give_more_info
    - utter_ask_something_consider
> relationships_can_consider

## relationshps user can consider
> relationships_can_consider
* affirm
	- utter_relationships_consider_positive_response
	- utter_ask_relationships_hear_another_way
> relationships_hear_another_way

## relationshps user cannot consider
> relationships_can_consider
* deny
	- utter_no_worries
	- utter_end_permah_option
	- utter_ask_permah_short

## relationships user wants to hear another way
> relationships_hear_another_way
* affirm
    - utter_relationships_explain_another_way
    - utter_ask_heated_conversation
> relationships_heated_conversation

## relationships user not want to hear another way
> relationships_hear_another_way
* deny
    - utter_no_worries
	- utter_end_permah_option
	- utter_ask_permah_short

## relationships user (never) had a heated conversation
> relationships_heated_conversation
* affirm OR deny
	- utter_relationships_heated_conversation_response_a
    - utter_relationships_heated_conversation_response_b
    - utter_relationships_heated_conversation_response_c
    - utter_ask_want_to_hear
> relationships_hear_acronym

## relationships user wants to hear the acronym
> relationships_hear_acronym
* affirm
	- utter_relationships_hear_response_a
    - utter_relationships_introduce_stop
* moreInfo
    - utter_relationships_explain_s
* continueStop
    - utter_relationships_explain_t
	- utter_relationships_t_exercise
	- utter_ask_ready_for_o
* affirm
	- utter_relationships_explain_o
* continueStop
    - utter_relationships_explain_p
	- utter_ask_something_can_try
> relationships_can_try_acronym

## relationships user not want to hear the acronym
> relationships_hear_acronym
* deny
	- utter_relationships_no_stop_response
    - utter_end_permah_option
	- utter_ask_permah_short

## relationships user can try acronym
> relationships_can_try_acronym
* affirm
	- utter_relationships_can_try_response
	- utter_relationships_exit_point
* affirm
	- utter_relationships_exit_phrase
    - utter_end_permah_option
	- utter_ask_permah_short

## relationships user cannot try acronym
> relationships_can_try_acronym
* deny
	- utter_relationships_cannot_try_response
	- utter_end_permah_option
	- utter_ask_permah_short


<!-- -------------------------------MEANING STORIES------------------------------- -->

## meaning intro
> activity_selection
* meaning{"selectedPermah": "Meaning"}
	- slot{"selectedPermah": "Meaning"}
	- utter_meaning_intro 
	- utter_ask_meaning_story
> meaning_tell_story
<!-- utter_meaning_things_to_find -->
## meaning tell story
> meaning_tell_story
* affirm
	- utter_meaning_story_love
	- utter_meaning_story
	- utter_ask_meaning_apply_to_me
> meaning_how_apply_to_user

## meaning not tell story
> meaning_tell_story
* deny
	- utter_meaning_skip_story
    - utter_meaning_after_story
    - utter_meaning_think_task
    - user_passion_form
	- form{"name": "user_passion_form"}
  	- form{"name": null}
    - utter_ask_meaning_list
> meaning_make_list

## meaning how it applies to user
> meaning_how_apply_to_user
* affirm OR deny
	- utter_meaning_after_story
	- utter_meaning_think_task
	- user_passion_form
	- form{"name": "user_passion_form"}
  	- form{"name": null}
    - utter_ask_meaning_list
> meaning_make_list

## meaning make a list
> meaning_make_list
* affirm
	- utter_meaning_task_write_response
    - action_find_meaning_in_things
    - user_meaning_change_form
	- form{"name": "user_meaning_change_form"}
  	- form{"name": null}
	- utter_meaning_exit
	- utter_end_permah_option
	- utter_ask_permah_short

## meaning not make a list
> meaning_make_list
* deny
	- utter_no_worries
	- utter_end_permah_option
	- utter_ask_permah_short

<!-- -------------------------------ENGAGEMENT STORIES------------------------------- -->

## engagement intro
> activity_selection
* engagement{"selectedPermah": "Engagement"}
	- slot{"selectedPermah": "Engagement"}
	- utter_engagement_intro
	- utter_ask_know_more
> engagement_know_more

## engagement user wants to know more
> engagement_know_more
* affirm 
	- utter_engagement_start_a
	- utter_engagement_start_b
	- utter_engagement_start_c
	- utter_ask_make_sense
> engagment_makes_sense

## engagement user not want to know more
> engagement_know_more
* deny 
	- utter_engagement_exit_point
	- utter_end_permah_option
	- utter_ask_permah_short

## engagement does make sense
> engagment_makes_sense
* affirm  
	- utter_engagement_note_before_work
	- utter_engagement_meaning_purpose
	- utter_engagement_work_meaning
> engagement_interest_in_hearing

## engagement does not make sense
> engagment_makes_sense
* deny
	- utter_engagement_give_another_example
    - utter_ask_got_one
> engagement_got_one

## engagement got one
> engagement_got_one
* affirm
	- utter_great
	- utter_engagement_no_sense_explanation
	- utter_engagement_meaning_purpose
	- utter_engagement_work_meaning
> engagement_interest_in_hearing

## engagement not got one
> engagement_got_one
* deny
	- utter_engagement_not_got_one
	<!-- - utter_great -->
	- utter_engagement_no_sense_explanation
	- utter_engagement_meaning_purpose
	- utter_engagement_work_meaning
> engagement_interest_in_hearing

## engagement user is interested in hearing
> engagement_interest_in_hearing
* affirm
	- utter_engagement_giving_go
	- utter_engagement_energise_a
	- first_strength_form
  	- form{"name": "first_strength_form"}
  	- form{"name": null}
	- second_strength_form
  	- form{"name": "second_strength_form"}
  	- form{"name": null}
    - utter_engagement_energise_b
    - utter_engagement_energise_c
    - action_engagement_actionable_behaviours
    - utter_ask_small_change
> engagement_small_change

## engagement user is not interested in hearing
> engagement_interest_in_hearing
* deny
	- utter_engagement_exit_point
	- utter_end_permah_option
	- utter_ask_permah_short

## engagement user chooses something to change
> engagement_small_change
* changeChoice
	- utter_engagement_choice_response
    - utter_end_permah_option
	- utter_ask_permah_short


<!-- -------------------------------ACCOMPLISHMENT STORIES------------------------------- -->

## accomplishment intro
> activity_selection
* accomplishment{"selectedPermah": "Accomplishment"}
	- slot{"selectedPermah": "Accomplishment"}
	- utter_accomplishment_intro
    - utter_ask_would_like_to_try
> accomplishment_try

## accomplishment user would like to try
> accomplishment_try
* affirm
	- utter_accomplishment_love_energy
    - utter_ask_get_pen
* affirm
	- utter_accomplishment_explain_first_task_a
    - utter_accomplishment_explain_first_task_b
	- action_accomplishment_check_all_good
	<!-- NOT TO REMOVE - uncomment the next line and comment the one above when testing locally -->
    <!-- - utter_ask_all_good -->
> accomplishment_all_good

## accomplishment user would not like to try
> accomplishment_try
* deny
	- utter_end_permah_option
	- utter_ask_permah_short

## accomplishment all good
> accomplishment_all_good
* affirm
	- action_accomplishment_next_task
	<!-- NOT TO REMOVE - uncomment the next line and comment the one above when testing locally -->
	<!-- - utter_ask_next_task -->
> accomplishment_next_task

## accomplishment not all good
> accomplishment_all_good
* deny
	- utter_accomplishment_give_exercise_advice
	- action_accomplishment_next_task
	<!-- NOT TO REMOVE - uncomment the next line and comment the one above when testing locally -->
	<!-- - utter_ask_next_task -->
> accomplishment_next_task

## accomplishment user wants to move to the next task
> accomplishment_next_task
* affirm
	- utter_accomplishment_explain_second_task
    - utter_ask_accomplishment_second_task
> accomplishment_think_for_second_task

## accomplishment user does not want to move to the next task
> accomplishment_next_task
* deny
	- utter_end_permah_option
	- utter_ask_permah_short

## accomplishment user wants to think for the second task
> accomplishment_think_for_second_task
* affirm
	- utter_accomplishment_super
    - utter_ask_accomplishment_think_action
> accomplishment_think_action

## accomplishment user does not want to think for the second task
> accomplishment_think_for_second_task
* deny
	- utter_end_permah_option
	- utter_ask_permah_short

## accomplishment user can think of action
> accomplishment_think_action
* affirm
	- utter_accomplishment_action_positive_response
	- utter_accomplishment_exit_point
    - utter_end_permah_option
    - utter_ask_permah_short

## accomplishment user cannot think of action
> accomplishment_think_action
* deny
	- utter_end_permah_option
	- utter_ask_permah_short

<!-- -------------------------------HEALTH STORIES------------------------------- -->

## health
> activity_selection
* health{"selectedPermah": "Health"}
	- slot{"selectedPermah": "Health"}
	- utter_health_intro
	- action_ask_health_topic
    <!-- - utter_ask_health_topic -->
> health_topic_selection

## health go back to menu
>health_topic_selection
* show
	- utter_end_permah_option
	- utter_ask_permah_short

<!-- -------------------------------HEALTH-SLEEP STORIES------------------------------- -->

## health sleep intro
> health_topic_selection
* healthTopic{"health_topic": "Sleep"}
	- slot{"health_topic": "Sleep"}
	- utter_sleep_intro
	- get_amount_sleep_form
	- form{"name": "get_amount_sleep_form"}
	- form{"name": null}
> healthsleep_continue

## health sleep user wants more info
> healthsleep_continue
* moreInfo
	- utter_sleep_explain_average
	- utter_ask_know_why
> healthsleep_know_why

## health sleep user not want more info
> healthsleep_continue
* deny
	- utter_sleep_chat_other_time
	- action_ask_health_topic
	<!-- - utter_end_permah_option
	- utter_ask_permah_short -->
> health_topic_selection

## health sleep user wants to know why
> healthsleep_know_why
* affirm
	- action_explain_sleep_important
	- utter_sleep_before_tips
* moreInfo
	- action_give_sleep_tips
	- utter_ask_tiny_habits
> healthsleep_tiny_habits

## health sleep user not want to know why
> healthsleep_know_why
* deny
	- utter_sleep_chat_other_time
	- action_ask_health_topic
	<!-- - utter_end_permah_option
	- utter_ask_permah_short -->
> health_topic_selection

## health sleep user will try tiny habits
> healthsleep_tiny_habits
* affirm
	- utter_sleep_tiny_habit_yes
	- utter_ask_consider_activity_sleep
> healthsleep_consider_another_activity

## health sleep user will not try tiny habits
> healthsleep_tiny_habits
* deny
	- utter_sleep_chat_other_time
	- action_ask_health_topic
	<!-- - utter_end_permah_option
	- utter_ask_permah_short -->
> health_topic_selection

## health sleep user considers another activity
> healthsleep_consider_another_activity
* affirm
	- action_explain_sleep_activity
	- utter_ask_something_can_try
> healthsleep_can_try

## health sleep user not consider another activity
> healthsleep_consider_another_activity
* deny
	- utter_no_worries
	<!-- - utter_end_permah_option
	- utter_ask_permah_short -->
	- action_ask_health_topic
> health_topic_selection

## health sleep user can try 
> healthsleep_can_try
* affirm
	- utter_exit_best_luck
	<!-- - utter_end_permah_option
	- utter_ask_permah_short -->
	- action_ask_health_topic
> health_topic_selection

## health sleep user cannot try 
> healthsleep_can_try
* deny
	- utter_sleep_negative_exit
	<!-- - utter_end_permah_option
	- utter_ask_permah_short -->
	- action_ask_health_topic
> health_topic_selection


<!-- -------------------------------HEALTH-PHYSICAL STORIES------------------------------- -->

## health physical intro
> health_topic_selection
* healthTopic{"health_topic": "Physical Activity"}
	- slot{"health_topic": "Physical Activity"}
	- utter_physical_intro
	- utter_ask_physical_per_day
* amountTimeMins{"amount_physical": "number mins"}
    - slot{"amount_physical": "number mins"}
	- utter_physical_recommended_time
> healthphysical_know_more

## health physical user wants to know more
> healthphysical_know_more
* moreInfo
    - utter_ask_physical_intensity
* moreInfo
    - utter_physical_explain_intensity
    - utter_ask_physical_ideas
> healthphysical_know_ideas

## health physical user not want to know more
> healthphysical_know_more
* deny
    - utter_no_worries
	<!-- - utter_end_permah_option
	- utter_ask_permah_short -->
	- action_ask_health_topic
> health_topic_selection

## health physical user wants to know the ideas
> healthphysical_know_ideas
* affirm
	- utter_happy_to_hear
* moreInfo
	- action_list_physical_ideas
	- utter_ask_physical_try_one_idea
> healthphysical_try_idea

## health physical user not want to know the ideas
> healthphysical_know_ideas
* deny
	- utter_no_worries
	<!-- - utter_end_permah_option
	- utter_ask_permah_short -->
	- action_ask_health_topic
> health_topic_selection

## health physical user can try idea
> healthphysical_try_idea
* affirm
	- utter_physical_positive_exit
	<!-- - utter_end_permah_option
	- utter_ask_permah_short -->
	- action_ask_health_topic
> health_topic_selection

## health physical user cannot try idea
> healthphysical_try_idea
* deny
	- utter_physical_negative_exit
	<!-- - utter_end_permah_option
	- utter_ask_permah_short -->
	- action_ask_health_topic
> health_topic_selection

<!-- -------------------------------HEALTH-NUTRITION STORIES------------------------------- -->

## health nutrition intro
> health_topic_selection
* healthTopic{"health_topic": "Nutrition"}
	- slot{"health_topic": "Nutrition"}
	- get_nutrition_rating_form
	- form{"name": "get_nutrition_rating_form"}
	- form{"name": null}
	- utter_ask_hear_more
> nutrition_hear_more

## health nutrition user wants to hear more
> nutrition_hear_more
* affirm
	- utter_great
	- utter_nutrition_explain_fuel_body
	- utter_nutrition_explain_creating_habits
	- utter_nutrition_hard
	- utter_ask_consider_change
> nutrition_consider_change

## health nutrition user not want to hear more
> nutrition_hear_more
* deny
	- utter_nutrition_not_hear_response
	<!-- - utter_end_permah_option
	- utter_ask_permah_short -->
	- action_ask_health_topic
> health_topic_selection

## health nutrition user can consider change 
> nutrition_consider_change
* affirm
	- utter_ask_nutrition_examples
> nutrition_examples

## health nutrition user cannot consider change 
> nutrition_consider_change
* deny
	- utter_no_worries
	<!-- - utter_end_permah_option
	- utter_ask_permah_short -->
	- action_ask_health_topic
> health_topic_selection

## health nutrition user needs examples
> nutrition_examples
* affirm
	- action_give_change_examples
* affirm
	- utter_ask_nutrition_commit_diet
> nutrition_commit_diet

## health nutrition user does not need examples
> nutrition_examples
* deny
	- utter_nutrition_no_examples_response
* ready
	- utter_nutrition_positive_exit
	<!-- - utter_end_permah_option
	- utter_ask_permah_short -->
	- action_ask_health_topic
> health_topic_selection

## health nutrition user can commit to diet
> nutrition_commit_diet
* affirm
	- utter_nutrition_positive_exit
	<!-- - utter_end_permah_option
	- utter_ask_permah_short -->
	- action_ask_health_topic
> health_topic_selection

## health nutrition user cannot commit to diet
> nutrition_commit_diet
* deny
	- utter_nutrition_negative_exit
	<!-- - utter_end_permah_option
	- utter_ask_permah_short -->
	- action_ask_health_topic
> health_topic_selection


<!-- -------------------------------POSITIVE EMOTIONS STORIES------------------------------- -->

## positive emotion intro
> activity_selection
* emotion{"selectedPermah": "Positive Emotion"}
	- slot{"selectedPermah": "Positive Emotion"}
	- utter_emotion_intro
    - utter_ask_feeling
> emotion_feeling

## positive emotion user feeling happy
> emotion_feeling
* feeling_happy
	- utter_ask_get_happier
> emotion_get_happier

## positive emotion user feeling unhappy
> emotion_feeling
* feeling_unhappy
	- utter_emotion_sad_response
	- utter_emotion_cannot_recognise_everything
	- utter_ask_sad_to_happy
> emotion_get_happier

## positive emotion user feeling neutral
> emotion_feeling
* feeling_neutral
	- utter_ask_neutral_to_happy
> emotion_get_happier

## positive emotion user wants to get happier 
> emotion_get_happier
* affirm
	- utter_emotion_get_happier_response
    - utter_ask_about_attitude
> emotion_attitude

## positive emotion user not want to get happier 
> emotion_get_happier
* deny
	- utter_emotion_not_get_happier_response
	- utter_end_permah_option
	- utter_ask_permah_short

## positive emotion user (not) knows about attitude
> emotion_attitude
* affirm OR deny
	- utter_emotion_start_task
    - utter_emotion_grateful_reason_a
	- first_grateful_reason_form
	- form{"name": "first_grateful_reason_form"}
	- form{"name": null}
<!-- * grateful -->
	- utter_ask_try_one_more
> emotion_try_one_more

## positive emotion user wants to try one more
> emotion_try_one_more
* affirm
	- utter_emotion_grateful_reason_b
    - second_grateful_reason_form
	- form{"name": "second_grateful_reason_form"}
	- form{"name": null}
<!-- * grateful -->
	- utter_emotion_grateful_response
    - utter_ask_hear_questions
> emotion_hear_questions

## positive emotion user not want to try one more
> emotion_try_one_more
* deny
	- utter_emotion_not_trying_again
    - utter_emotion_exit_point
	- utter_end_permah_option
	- utter_ask_permah_short

## positive emotion user wants to hear questions
> emotion_hear_questions
* affirm
	- action_emotion_explain_question
	- utter_emotion_exit_point
	- utter_end_permah_option
	- utter_ask_permah_short

## positive emotion user not want to hear questions
> emotion_hear_questions
* deny
	- utter_emotion_no_questions_response
    - utter_emotion_exit_point
	- utter_end_permah_option
	- utter_ask_permah_short

<!-- -------------------------------DEFAULT FALLBACK ------------------------------- -->

## default fallback
* out_of_scope
	- action_default_fallback

<!-- -------------------------------WHO STORIES ------------------------------- -->

## who activity selection story
> activity_selection
* who_intent
	- utter_ask_who_choices
> who_activity_selection

## about who
> who_activity_selection
* explain_who
	- utter_who_explain
	- utter_who_more_info
	- utter_ask_who_choices

## who complete scale
> who_activity_selection
* completeScale
	- action_reset_who_slots
	- who_form
	- form{"name": "who_form"}
	- form{"name": null}
	- utter_who_score_exit
	- utter_ask_who_choices

## from who go back to menu
> who_activity_selection
* show
	- utter_ask_permah_short

## restart
* intent_restart
	- action_restart
