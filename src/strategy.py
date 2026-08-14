def decide_action(state):
    """
    Reactive baseline decision engine. 
    Focuses on rule compliance, basic action validity, and stable behavior.
    """
    
    hole_cards = state["hole_cards"]
    call_amount = state["current_bet_to_call"]
    
    # Fallback default action
    decision = {"type": "action", "action": "FOLD"}
    
    # Scenario A: Free to check
    if call_amount == 0:
        decision = {"type": "action", "action": "CHECK"}
        
    # Scenario B: Basic pre-flop hand strength evaluation
    elif len(hole_cards) == 2:
        # Simplified baseline logic: Play high cards or pairs
        ranks = [card[0] for card in hole_cards]  # e.g., 'A', 'K', '9'
        high_cards = ['A', 'K', 'Q', 'J', '10']
        
        is_pair = ranks[0] == ranks[1]
        has_high_card = any(rank in high_cards for rank in ranks)
        
        if is_pair or has_high_card:
            decision = {"type": "action", "action": "CALL"}
        else:
            decision = {"type": "action", "action": "FOLD"}
            
    return decision