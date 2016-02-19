---
layout: default
img: sudo-make-make-a-sandwich
img_link: http://xkcd.com/149/
title: Term project
active_tab: project
---

<!-- Check whether the assignment is up to date
{% capture this_year %}{{'now' | date: '%Y'}}{% endcapture %}
{% capture due_year %}{{page.due_date | date: '%Y'}}{% endcapture %}
{% if this_year != due_year %} 
<div class="alert alert-danger">
Warning: this assignment is out of date.  It may still need to be updated for this year's class.  Check with your instructor before you start working on this assignment.
</div>
{% endif %}
<!-- End of check whether the assignment is up to date 
-->

### Example final projects from last year

Here are 3 examples of my favorite final projects from last year. You can also check out all of the the final project videos from the [Fall 2014 class](final-projects-2014.html) and the [Fall 2013 class](final-projects-2013.html).


<table class="table table-striped"> 
  <tbody>
    {% for questionnaire in site.data.example_final_projects %}
    {% assign anchor = questionnaire.name_of_your_project | replace:' ', '-' | replace:"'", '' | replace:'.', ''  | replace:'(', '' | replace:')', ''  %}
    {% assign logo = questionnaire.url_to_the_logo_for_your_project | replace:"github.com", "raw.githubusercontent.com" | replace:"blob/", "" %}
   <tr>
      <td>
	<div class="hidden-sm hidden-xs">
		<img src="{{ logo }}" width="200" />
	</div>
      </td>
      <td>
<div class="visible-sm visible-xs">
		<img src="{{ logo }}" width="100" />
</div>
<div class="panel-group" id="accordion{{ anchor }}">
  <div class="panel panel-default">
    <div class="panel-heading">
      <div class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion{{ anchor }}" href="#{{ anchor }}">
{{ questionnaire.give_a_one_sentence_description_of_your_project }} 
        </a>
      </div>
    </div>
    <div id="{{ anchor }}" class="panel-collapse collapse">
      <div class="panel-body">


<b>{{ questionnaire.name_of_your_project }}</b> by 
{% if questionnaire.team_member_1__can_we_list_your_name_listed_alongside_your_project %}
	{{ questionnaire.name_1 }}{% endif %}
{% if questionnaire.team_member_2__can_we_list_your_name_listed_alongside_your_project %}
,	{{ questionnaire.name_2 }}{% endif %}
{% if questionnaire.team_member_3__can_we_list_your_name_listed_alongside_your_project %}
,	{{ questionnaire.name_3 }}{% endif %}
{% if questionnaire.team_member_4__can_we_list_your_name_listed_alongside_your_project %}
,	{{ questionnaire.name_4 }}
{% endif %}

{% assign vimeourl = questionnaire.vimeo_link | split:"/" %}
{% for urlpart in vimeourl %}
	{% capture videonum %}{{ urlpart }}{% endcapture %}
{% endfor %} 

<div align="center" class="hidden-sm hidden-xs">
<iframe src="http://player.vimeo.com/video/{{ videonum }}" width="500" height="281" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe> <br />
</div>
<div align="center" class="visible-sm visible-xs">
<b>Video profile:</b> <a href="http://player.vimeo.com/video/{{ videonum }}">http://player.vimeo.com/video/{{ videonum }}"</a> <br />
</div>

<b>Give a one sentence description of your project.</b> {{ questionnaire.give_a_one_sentence_description_of_your_project }}<br /> 
<b>What type of project is it?</b> {{ questionnaire.what_type_of_project_is_it }}<br /> 
<b>What similar projects exist?</b> {{ questionnaire.what_similar_projects_exist }}<br /> 
<b>How does your project work?</b> {{ questionnaire.how_does_your_project_work}}<br />



<center><b>The Crowd</b></center>
<b>What does the crowd provide for you?</b> {{ questionnaire.what_does_the_crowd_provide_for_you }}<br /> 
<b>Who are the members of your crowd?</b> {{ questionnaire.who_are_the_members_of_your_crowd }}<br />  
<b>How many unique participants did you have?</b> {{ questionnaire.how_many_unique_participants_did_you_have}}<br />
<b>For your final project, did you simulate the crowd or run a real experiment?</b> {{ questionnaire.for_your_final_project_did_you_simulate_the_crowd_or_run_a_real_experiment}}<br />
{% if questionnaire.for_your_final_project_did_you_simulate_the_crowd_or_run_a_real_experiment == "Simulated crowd" %}
	<b>If the crowd was simulated, how did you collect this set of data?</b> {{ questionnaire.if_the_crowd_was_simulated_how_did_you_collect_this_set_of_data}}<br />
	<b>If the crowd was simulated, how would you change things to use a real crowd?</b> {{ questionnaire.if_the_crowd_was_simulated_how_would_you_change_things_to_use_a_real_crowd}}<br />
{% else %}
	<b>If the crowd was real, how did you recruit participants?</b> {{ questionnaire.if_the_crowd_was_real_how_did_you_recruit_participants}}<br />
{% endif %}
<b>Would your project benefit if you could get contributions form thousands of people?</b> {{ questionnaire.would_your_project_benefit_if_you_could_get_contributions_from_thousands_of_people }}<br /> 
<b>Do your crowd workers need specialized skills?</b> {{ questionnaire.do_your_crowd_workers_need_specialized_skills}}<br />
<b>What sort of skills do they need?</b> {{ questionnaire.what_sort_of_skills_do_they_need}}<br />
<b>Do the skills of individual workers vary widely?</b> {{ questionnaire.do_the_skills_of_individual_workers_vary_widely}}<br />
<b>If skills vary widely, what factors cause one person to be better than another? </b> {{ questionnaire.if_skills_vary_widely_what_factors_cause_one_person_to_be_better_than_another_}}<br />
<b>Did you analyze the skills of the crowd?</b> {{ questionnaire.did_you_analyze_the_skills_of_the_crowd}}<br />
<b>If you analyzed skills, what analysis did you perform?</b> {{ questionnaire.if_you_analyzed_skills_what_analysis_did_you_perform}}<br />



<b>Did you create a user interface for the crowd workers?</b> {{ questionnaire.did_you_create_a_user_interface_for_the_crowd_workers}}<br />
<b>If yes, please give the URL to a screenshot of the crowd-facing user interface.</b> {{ questionnaire.if_yes_please_give_the_url_to_a_screenshot_of_the_crowdfacing_user_interface}}<br />
<b>Describe your crowd-facing user interface.</b> {{ questionnaire.describe_your_crowdfacing_user_interface}}<br />




<center><b>Incentives</b></center>

<b>How do you incentivize the crowd to participate?</b> {{ questionnaire.how_do_you_incentivize_the_crowd_to_participate }}<br /> 
<b>Did you perform any analysis comparing different incentives? </b> {{ questionnaire.did_you_perform_any_analysis_comparing_different_incentives_}}<br />
<b>If you compared different incentives, what analysis did you perform? </b> {{ questionnaire.if_you_compared_different_incentives_what_analysis_did_you_perform_}}<br />


<center><b>Aggregation</b></center>

<b>What is the scale of the problem that you are trying to solve? </b> {{ questionnaire.what_is_the_scale_of_the_problem_that_you_are_trying_to_solve_}}<br />


<b>How do you aggregate the results from the crowd?</b>  {{ questionnaire.how_do_you_aggregate_the_results_from_the_crowd }}<br /> 
<b>Did you analyze the aggregated results? </b> {{ questionnaire.did_you_analyze_the_aggregated_results_}}<br />
<b>What analysis did you perform on the aggregated results?</b> {{ questionnaire.what_analysis_did_you_perform_on_the_aggregated_results}}<br />
<b>Did you create a user interface for the end users to see the aggregated results?</b> {{ questionnaire.did_you_create_a_user_interface_for_the_end_users_to_see_the_aggregated_results}}<br />
<b>If yes, please give the URL to a screenshot of the user interface for the end user.</b> {{ questionnaire.if_yes_please_give_the_url_to_a_screenshot_of_the_user_interface_for_the_end_user}}<br />
<b>Describe what your end user sees in this interface.</b> {{ questionnaire.describe_what_your_end_user_sees_in_this_interface}}<br />


<b>If it would benefit from a huge crowd, how would it benefit? </b> {{ questionnaire.if_it_would_benefit_from_a_huge_crowd_how_would_it_benefit_}}<br />
<b>What challenges would scaling to a large crowd introduce?</b> {{ questionnaire.what_challenges_would_scaling_to_a_large_crowd_introduce}}<br />
<b>Did you perform an analysis about how to scale up your project?</b> {{ questionnaire.did_you_perform_an_analysis_about_how_to_scale_up_your_project}}<br />
<b>What analysis did you perform on the scaling up?</b> {{ questionnaire.what_analysis_did_you_perform_on_the_scaling_up}}<br />



<center><b>Quality Control</b></center>

<b>Is the quality of what the crowd gives you a concern?</b> {{ questionnaire.is_the_quality_of_what_the_crowd_gives_you_a_concern}}<br />
<b>How do you ensure the quality of what the crowd provides?</b> 
{{ questionnaire.how_do_you_ensure_the_quality_of_the_crowd_provides__ }}<br />

<b>Did you analyze the quality of what you got back?</b> {{ questionnaire.did_you_analyze_the_quality_of_what_you_got_back}}<br />
<b>What analysis did you perform on quality?</b> {{ questionnaire.what_analysis_did_you_perform_on_quality}}<br />
<b>Is this something that could be automated?</b> {{ questionnaire.is_this_something_that_could_be_automated}}<br />
<b>If it could be automated, say how.  If it is difficult or impossible to automate, say why.</b> {{ questionnaire.if_it_could_be_automated_say_how__if_it_is_difficult_or_impossible_to_automate_say_why}}<br />


<center><b>Additional Analysis</b></center>


<b>Did your project work?</b> {{ questionnaire.did_your_project_work}}<br />
<b>What are some limitations of your project?</b> {{ questionnaire.what_are_some_limitations_of_your_product}}<br />

{% if questionnaire.questionnaire.did_your_results_deviate_from_what_you_would_expect_from_previous_work_or_what_you_learned_in_the_class %}
<b>Did your results deviate from what you would expect from previous work or what you learned in the class?</b> {{ questionnaire.did_your_results_deviate_from_what_you_would_expect_from_previous_work_or_what_you_learned_in_the_class}}<br />
<b>If your results deviated, why might that be?</b> {{ questionnaire.if_your_results_deviated_why_might_that_be}}<br />
{% endif %}

<b>Is there anything else you'd like to say about your project?</b> {{ questionnaire.is_there_anything_else_youd_like_to_say_about_your_project}}<br />

      </div>
    </div>
  </div>
</div>

       </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
 
