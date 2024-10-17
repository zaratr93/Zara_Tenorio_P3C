import random
def main():
    global plural_or_single
    plural_or_single = random.choice([1,2])
    for i in range(6):
        i = (f"{make_sentence()}")
        print(i)
        
def get_determiner():
    if plural_or_single == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    return random.choice(words)

def get_noun():
    if plural_or_single == 1:
        singular_nouns = [
        "apple", "book", "car", "dog", "elephant",
        "flower", "guitar", "house", "island", "jacket",
        "kite", "lamp", "mountain", "notebook", "orange",
        "pencil", "queen", "rabbit", "star", "tree",
        "umbrella", "violin", "whale", "xylophone", "yacht",
        "zebra", "table", "chair", "computer", "phone",
        "bicycle", "clock", "egg", "fish", "grape",
        "hat", "ice", "jewel", "key", "leaf",
        "mirror", "necklace", "ocean", "piano", "quilt",
        "ring", "shoe", "turtle", "uniform", "vase",
        "window", "yarn", "zoo"]
        single_noun = random.choice(singular_nouns)
        return(single_noun)
    else:
        plural_nouns = [
        "apples", "books", "cars", "dogs", "elephants",
        "flowers", "guitars", "houses", "islands", "jackets",
        "kites", "lamps", "mountains", "notebooks", "oranges",
        "pencils", "queens", "rabbits", "stars", "trees",
        "umbrellas", "violins", "whales", "xylophones", "yachts",
        "zebras", "tables", "chairs", "computers", "phones",
        "bicycles", "clocks", "eggs", "fishes", "grapes",
        "hats", "ices", "jewels", "keys", "leaves",
        "mirrors", "necklaces", "oceans", "pianos", "quilts",
        "rings", "shoes", "turtles", "uniforms", "vases",
        "windows", "yarns", "zoos"]
        plural_noun = random.choice(plural_nouns)
        return(plural_noun)
def get_verb():
    if plural_or_single == 1:
        singular_verbs = [
        "walks", "runs", "jumps", "sings", "reads", "writes",
        "plays", "cooks", "dances", "talks", "thinks", "draws",
        "watches", "laughs", "hides", "swims", "drives", "listens",
        "teaches", "builds", "cleans", "shares", "studies", "travels",
        "creates", "opens", "closes", "fixes", "explores", "sends",
        "receives", "remembers", "enjoys", "helps", "shows", "discovers",
        "trains", "paints", "competes", "wishes", "sells", "buys",
        "fishes", "celebrates", "prays", "calls", "sleeps", "searches"]
        single_verb = random.choice(singular_verbs)
        return(single_verb)
    else:
        plural_verbs = [
        "walk", "run", "jump", "sing", "read", "write",
        "play", "cook", "dance", "talk", "think", "draw",
        "watch", "laugh", "hide", "swim", "drive", "listen",
        "teach", "build", "clean", "share", "study", "travel",
        "create", "open", "close", "fix", "explore", "send",
        "receive", "remember", "enjoy", "help", "show", "discover",
        "train", "paint", "compete", "wish", "sell", "buy",
        "fish", "celebrate", "pray", "call", "sleep", "search",
        "collaborate", "communicate"]
        plural_verb = random.choice(plural_verbs)
        return(plural_verb)
def make_sentence():
    sentence = (f"{get_determiner()} {get_noun()} {get_verb()}")
    return(sentence)
main()