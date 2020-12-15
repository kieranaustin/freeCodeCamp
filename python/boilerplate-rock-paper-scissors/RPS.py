# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], play_order={}, mem_size=6):
    if not prev_play:
        prev_play = "S"
    opponent_history.append(prev_play)

    if len(opponent_history)>mem_size:
        last_input = "".join(opponent_history[-mem_size+1:])
        last_plays = "".join(opponent_history[-mem_size:])
        play_order[last_plays] = play_order[last_plays]+1 if last_plays in play_order.keys() else 1
        
        potential_plays = [ last_input+"R", last_input+"P", last_input+"S" ]

        for k in potential_plays:
            if k not in play_order:
                play_order[k] = 0
        sub_order = { k: play_order[k] for k in potential_plays if k in play_order}
        prediction = max(sub_order, key=sub_order.get)[-1:]
        ideal_response = {"R": "P", "P": "S", "S": "R"}
        return ideal_response[prediction]
    else:
        return opponent_history[-1]





