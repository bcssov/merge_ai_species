from templates.utils import settings, templater

template_1 = """
				{if_statement} = {{
					limit = {{
						root = {{
							count_owned_pop = {{
								count >= {count}
								limit = {{
									OR = {{
										is_same_species = prevprev
										is_subspecies = prevprev
									}}
									NOR = {{
										species = {{
											has_species_flag = mas_merge_species_currently_processing
										}}
										has_trait = trait_self_modified
									}}
								}}
							}}
						}}
					}}
					root = {{
						random_owned_pop_species = {{
							limit = {{
								count_species_pop = {{
									count >= {count}
									limit = {{
										OR = {{
											is_same_species = prevprevprev
											is_subspecies = prevprevprev
										}}
										NOR = {{
											species = {{
												has_species_flag = mas_merge_species_currently_processing
											}}
											has_trait = trait_self_modified
										}}
									}}
								}}
							}}
							set_species_flag = mas_merge_species_target_species
							save_event_target_as = mas_target_species
						}}
					}}
				}}"""

template_2 = """
				{if_statement} = {{
					limit = {{
						root = {{
							count_owned_pop = {{
								count >= {count}
								limit = {{
									OR = {{
										is_same_species = prevprev
										is_subspecies = prevprev
									}}
									NOT = {{
										species = {{
											has_species_flag = mas_merge_species_currently_processing
										}}										
									}}
								}}
							}}
						}}
					}}
					root = {{
						random_owned_pop_species = {{
							limit = {{
								count_species_pop = {{
									count >= {count}
									limit = {{
										OR = {{
											is_same_species = prevprevprev
											is_subspecies = prevprevprev
										}}
										NOT = {{
											species = {{
												has_species_flag = mas_merge_species_currently_processing
											}}											
										}}
									}}
								}}
							}}
							set_species_flag = mas_merge_species_target_species
							save_event_target_as = mas_target_species
						}}
					}}
				}}"""
template_3 = """
				{if_statement} = {{
					limit = {{
						root = {{
							count_owned_pop = {{
								count >= {count}
								limit = {{
									species = {{
										OR = {{
											is_species_class = MACHINE
											is_species_class = ROBOT
										}}
									}}
									root = {{
										count_owned_pop = {{
											limit = {{
												is_exact_same_species = prevprev
											}}
											count >= {count}
										}}
									}}
									NOT = {{
										species = {{
											has_species_flag = mas_merge_species_currently_processing
										}}
									}}
								}}
							}}
						}}
					}}
					root = {{
						random_owned_pop_species = {{
							limit = {{
								count_species_pop = {{
									count >= {count}
									limit = {{
										species = {{
											OR = {{
												is_species_class = MACHINE
												is_species_class = ROBOT
											}}
										}}
										root = {{
											count_owned_pop = {{
												limit = {{
													is_exact_same_species = prevprev
												}}
												count >= {count}
											}}
										}}
										NOT = {{
											species = {{
												has_species_flag = mas_merge_species_currently_processing
											}}
										}}
									}}
								}}
							}}
							set_species_flag = mas_merge_species_target_species
							save_event_target_as = mas_target_species
						}}
					}}
				}}"""


def process(publish_dir):
    lines_1 = []
    lines_2 = []
    lines_3 = []

    for i in range(settings.max['range'], settings.middle['range'], settings.max['step']):
        if i == settings.max['range']:
            lines_1.append(template_1.format(count=i, if_statement="if"))
            lines_2.append(template_2.format(count=i, if_statement="if"))
            lines_3.append(template_3.format(count=i, if_statement="if"))
        else:
            lines_1.append(template_1.format(count=i, if_statement="else_if"))
            lines_2.append(template_2.format(count=i, if_statement="else_if"))
            lines_3.append(template_3.format(count=i, if_statement="else_if"))

    for i in range(settings.middle['range'], settings.low['range'], settings.middle['step']):
        lines_1.append(template_1.format(count=i, if_statement="else_if"))
        lines_2.append(template_2.format(count=i, if_statement="else_if"))
        lines_3.append(template_3.format(count=i, if_statement="else_if"))
    for i in range(settings.low['range'], 0, settings.low['step']):
        lines_1.append(template_1.format(count=i, if_statement="else_if"))
        lines_2.append(template_2.format(count=i, if_statement="else_if"))
        lines_3.append(template_3.format(count=i, if_statement="else_if"))

    templater.process_file(
        publish_dir + "/events/merge_ai_species.txt",
        event_1=lines_1, event_2=lines_2, event_3=lines_3)
