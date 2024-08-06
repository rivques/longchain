quest = Quest(
    name="test",
    paths=[
        Path(
            id="smallberry_initial",
            display_name="Baker Smallberry",
            icon="example.com/smallberry.png",
            action_reolver=LlmActionResolver(
                id="smallberry_initial_llm",
                system_prompt="example prompt",
                use_history_from=["smallberry_initial_llm"],
                clear_history_on_end=False,
                endable_paths=[EndablePath(path_id="traveling_there", scenario="When the player has agreed to the quest")],
            )
        ),
        Path(
            id="travelling_there",
            display_name="travelling...",
            icon="example.com/travelling.png",
            action_resolver=SequentialActionResolver(
                MessageAction(
                    message="You travel over the hill and through the woods" # Resolvable<string>
                ),
                EndAction(
                    dest=lambda p: random.choices(["travelling_there_2", "bandit_encounter"], [0.75, 0.25]) # Resolvable<PathId>
                )
            )
        ),
        Path(
            id="bandit_encounter",
            display_name="Bandit Encounter",
            icon="example.com/bandit.png",
            action_resolver=LlmActionResolver(
                id="bandit_encounter_llm",
                system_prompt="example prompt",
                use_history_from=["bandit_encounter_llm"],
                clear_history_on_end=True,
                endable_paths=[EndablePath(path_id="travelling_there_2", scenario="When the bandits leave, either because the player defeated them or because they're done stealing or because the player scares them off")], # Resolvable<EndablePath[]>
                agent_actions=[
                    LlmTool(
                        name="take_gold",
                        description="Take some amount of gold from the player",
                        params=[
                            LlmToolParam(
                                name="num_gold",
                                description="The number of gold to take",
                                type="int"
                                min=0,
                                max=100
                            )
                        ],
                        available=lambda ctx: ctx.player.gold > 0 and ctx.times_called < 1,
                    )
                ]
            )
        )
    ]
)

class Path:
    def tick(player: Player) -> PathResult:
        action: Action = self.action_resolver.tick(player)
        path_result = action.run(self, player)
        return path_result

class Quest:
    def tick(player):
        path_result: PathResult = self.get_path(player.current_path).tick(player)
        slack.send_messages(path_result.messages)
        if path_result.new_path_id:
            player.current_path = path_result.new_path_id
    
await quest.run()

# so:
# a new message calls quest.tick with that player
# quest.tick calls the current path's tick method
# the current path's tick method calls the action resolver's tick method
# the action resolver's tick method returns an action
# the action's run method is called with the path and player
# the action's run method might have side effects, like changing the player's state, or changing their inventory
# the action's run method returns a path result
# the path result is returned to the quest's tick method
# the quest's tick method deals with the path result by changing the path if needed and sending the messages to slack
# the quest's tick method returns