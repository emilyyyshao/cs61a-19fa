"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    num = 0
    counter = 0
    while counter <= len(paragraphs) - 1:
        if select(paragraphs[counter]):
            num += 1 
        if num - 1 == k:
            return paragraphs[counter]
        counter += 1
    if num - 1 < k:
            return ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def select(paragraph):
        new_split = split(paragraph)
        i = 0
        while i < len(new_split):
            for word in topic:
                if remove_punctuation(lower(new_split[i])) == word:
                    return True
            i += 1
        return False            
    return select
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    correct_sum = 0
    i = 0
    if len(typed_words) == 0 or len(reference_words) == 0:
        return 0.0
    while i < min(len(reference_words),len(typed_words)):
        if typed_words[i] == reference_words[i]:
            correct_sum += 1
        i += 1
    return (correct_sum / len(typed_words)) * 100.0
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    return (len(typed)/5)/(elapsed/60)
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than or equal to LIMIT.
    """
    # BEGIN PROBLEM 5
    if user_word in valid_words:
        return user_word
    min_diff = diff_function(user_word,valid_words[0],limit)
    k = 0
    for i in range(len(valid_words)):
        if diff_function(user_word,valid_words[i],limit) < min_diff:
            min_diff = diff_function(user_word,valid_words[i],limit)
            k = i
    if min_diff > limit:
        return user_word
    return valid_words[k]

    # END PROBLEM 5


def swap_diff(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    diff_length = abs(len(start)-len(goal))
    def swap_diff_helper(typed,target,k=0):
        if k > limit:
            return k
        if typed == '' or target == '':
            return diff_length
        if typed == target:
            return 0
        elif typed[0] == target[0]:
            return swap_diff_helper(typed[1:],target[1:],k)
        else:
            k += 1
            return 1 + swap_diff_helper(typed[1:],target[1:],k)
    return swap_diff_helper(start,goal)
    # END PROBLEM 6

def edit_diff(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    def edit_diff_helper(start,goal,k=0):
        if k > limit:
            return k
        elif start == goal: 
            return 0
        elif start == '' or goal == '':
            return abs(len(start)-len(goal))
        else:
            add_diff = 1 + edit_diff_helper(start,goal[1:],k+1)
            remove_diff = 1 + edit_diff_helper(start[1:],goal,k+1) 
            substitute_diff = (start[0] != goal[0]) + edit_diff_helper(start[1:],goal[1:],k+(start[0] != goal[0])) 
            return min(add_diff,remove_diff,substitute_diff)
    return edit_diff_helper(start,goal)


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'




###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    ratio = min([i/len(prompt) for i in range(len(typed)) if typed[i] != prompt[i]]+[len(typed)/len(prompt)])
    send({'id': id, 'progress': ratio})
    return ratio
    # END PROBLEM 8


def fastest_words_report(word_times):
    """Return a text description of the fastest words typed by each player."""
    fastest = fastest_words(word_times)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def fastest_words(word_times, margin=1e-5):
    """A list of which words each player typed fastest."""
    n_players = len(word_times)
    n_words = len(word_times[0]) - 1
    assert all(len(times) == n_words + 1 for times in word_times)
    assert margin > 0
    # BEGIN PROBLEM 9
    fasted_word_list = [[] for k in range(n_players)]
    def time_spend_typing_word(i,player):
        word_processing = word( word_times[player][i] )
        spend_time = elapsed_time(word_times[player][i]) - elapsed_time(word_times[player][i-1])
        return [word_processing,spend_time] 

    for i in range(1,n_words+1):
        for player in range(n_players):
            min_time = min([time_spend_typing_word(i,player)[1] for player in range(n_players)])
            adopted_time = min_time + margin
        for player in range(n_players):
            if time_spend_typing_word(i,player)[1] <= adopted_time:
                fasted_word_list[player] += [time_spend_typing_word(i,player)[0]]
    return fasted_word_list
    # END PROBLEM 9


def word_time(word, elapsed_time):
    """A data abstrction for the elapsed time that a player finished a word."""
    return [word, elapsed_time]


def word(word_time):
    """An accessor function for the word of a word_time."""
    return word_time[0]


def elapsed_time(word_time):
    """An accessor function for the elapsed time of a word_time."""
    return word_time[1]


enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)