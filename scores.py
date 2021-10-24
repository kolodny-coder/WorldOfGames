from redis import Redis

from utils import SCORES_FILE_NAME

redis = Redis(host='redis', port=6379)
redis.mset({"num_of_points": 0})

def add_score(difficulty):
    # Calculate the number of points the player won this round
    global last_score_before_update
    number_of_points_won_this_round = (int(difficulty) * 3) + 5

    try:
        # with open(SCORES_FILE_NAME, 'r') as read_file:
        last_score_before_update = redis.get('num_of_points')
        print(last_score_before_update)
    except FileNotFoundError:
        pass
    #     with open(SCORES_FILE_NAME, 'w') as write_file:
    #         write_file.write(str(number_of_points_won_this_round))
    #         return
    updated_points = number_of_points_won_this_round + int(last_score_before_update)
    redis.mset({"num_of_points": updated_points})
