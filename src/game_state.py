def parse_game_state(turn_payload):
    """
    Translates continuous game telemetry into a structured evaluation state.
    Extracts hole cards, board texture, and pot odds.
    """
    
    state = {
        "round": turn_payload.get("round", "pre-flop"),
        "hole_cards": turn_payload.get("hole_cards", []),
        "community_cards": turn_payload.get("community_cards", []),
        "pot_size": turn_payload.get("pot", 0),
        "current_bet_to_call": turn_payload.get("call_amount", 0),
        "my_stack": turn_payload.get("stack", 0),
        "active_players": turn_payload.get("active_players", 0)
    }
    
    # Calculate basic pot odds if there is a bet to call
    if state["current_bet_to_call"] > 0:
        total_pot_if_called = state["pot_size"] + state["current_bet_to_call"]
        state["pot_odds"] = state["current_bet_to_call"] / total_pot_if_called
    else:
        state["pot_odds"] = 0.0
        
    return state