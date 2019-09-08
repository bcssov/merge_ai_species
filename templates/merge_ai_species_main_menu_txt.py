from templates.utils import settings, templater

template_flags = """
		save_event_target_as = mas_target_{target_id}"""

template_flag_assign = """
			{if_statement} = {{
				limit = {{
					event_target:mas_target_{target_id} = {{
						is_same_value = event_target:mas_country
					}}
				}}
				save_event_target_as = mas_target_{target_id}
				set_country_flag = mas_processed
			}}"""

template_options = """
	option = {{
		name = merge_ai_species_main_menu.{event_id}.target_{target_id}

		trigger = {{
			NOT = {{
				event_target:mas_target_{target_id} = {{
					is_same_value = event_target:mas_country
				}}
			}}
		}}

		event_target:mas_target_{target_id} = {{
			save_event_target_as = mas_target
		}}

		country_event = {{
			id = merge_ai_species_main_menu.{cleanup_event_id}
		}}
	}}"""

template_clear_flags = """
			{if_statement} = {{
				limit = {{
					is_same_value = event_target:mas_target_{target_id}
				}}
				remove_country_flag = mas_processed
			}}"""


def process(publish_dir):
    lines_flags = []
    lines_flags_assign = []
    lines_options_10 = []
    lines_options_20 = []
    lines_options_30 = []
    lines_clear_flags = []
    for i in range(1, settings.items_per_page + 1):
        lines_flags.append(template_flags.format(target_id=i))
        lines_options_10.append(template_options.format(
            target_id=i, event_id=10, cleanup_event_id=11))
        lines_options_20.append(template_options.format(
            target_id=i, event_id=20, cleanup_event_id=21))
        lines_options_30.append(template_options.format(
            target_id=i, event_id=30, cleanup_event_id=31))
        if i == 1:
            lines_flags_assign.append(
                template_flag_assign.format(if_statement="if", target_id=i))
            lines_clear_flags.append(template_clear_flags.format(
                if_statement="if", target_id=i))
        else:
            lines_flags_assign.append(
                template_flag_assign.format(if_statement="else_if", target_id=i))
            lines_clear_flags.append(template_clear_flags.format(
                if_statement="else_if", target_id=i))

    templater.process_file(
        publish_dir + "/events/merge_ai_species_main_menu.txt",
        targets=lines_flags, set_targets=lines_flags_assign,
        options=lines_options_10,  cleanup=lines_clear_flags,
        options_2=lines_options_20, options_3=lines_options_30)
